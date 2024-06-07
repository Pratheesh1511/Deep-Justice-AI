import os
from flask import Flask, render_template, request, redirect, url_for

import llama_index.core
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings
from llama_index.core import SimpleDirectoryReader
from llama_index.core import (
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
)
from llama_index.core.query_pipeline import QueryPipeline
from llama_index.core import PromptTemplate
from llama_index.core.postprocessor import LLMRerank
from llama_index.core.response_synthesizers import TreeSummarize


# Initialize the LLM and embedding models
Settings.llm = OpenAI(model="gpt-3.5-turbo")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

# Load documents and create/load the index
reader = SimpleDirectoryReader("C:/Users/Pratheesh/Desktop/minpro/dataset/")
docs = reader.load_data()

if not os.path.exists("storage"):
    index = VectorStoreIndex.from_documents(docs)
    index.set_index_id("vector_index")
    index.storage_context.persist("./storage")
else:
    storage_context = StorageContext.from_defaults(persist_dir="storage")
    index = load_index_from_storage(storage_context, index_id="vector_index")

retriever = index.as_retriever(similarity_top_k=10)
summarizer = TreeSummarize()

# Define prompt templates
prompt_str_1 = '{inpu}'
prompt_tmpl_1 = PromptTemplate(prompt_str_1)
prompt_str_2 = (
    "Please write a passage to answer the question\n"
    "Try to include as many key details as possible.\n"
    "Answer according to what is in the given data.\n"
    "\n"
    "{query_str}\n"
    "\n"
    'Passage:"""\n'
)
prompt_tmpl_2 = PromptTemplate(prompt_str_2)

qa_prompt_tmpl = (
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given the context information and not prior knowledge, "
    "answer the query.\n"
    "If the context does not answer the question, simply state that it does not answer the question.\n"
    "Query: {query_str}\n"
    "Answer: "
)
qa_prompt = PromptTemplate(qa_prompt_tmpl)

llm = OpenAI(model="gpt-3.5-turbo")
retriever = index.as_retriever(similarity_top_k=10)
reranker = LLMRerank()
summarizer = TreeSummarize(llm=llm, summary_template=qa_prompt)

# Build the query pipeline
p = QueryPipeline(verbose=True)
p.add_modules(
    {
        "llm_1": llm,
        "llm_2": llm,
        "prompt_tmpl_1": prompt_tmpl_1,
        "prompt_tmpl_2": prompt_tmpl_2,
        "retriever": retriever,
        "summarizer": summarizer,
        "reranker": reranker,
    }
)
p.add_link("prompt_tmpl_1", "llm_1")
p.add_link("llm_1", "prompt_tmpl_2")
p.add_link("prompt_tmpl_2", "llm_2")
p.add_link("llm_2", "retriever")
p.add_link("retriever", "reranker", dest_key="nodes")
p.add_link("llm_2", "reranker", dest_key="query_str")
p.add_link("reranker", "summarizer", dest_key="nodes")
p.add_link("prompt_tmpl_1", "summarizer", dest_key="query_str")

# Initialize Flask app
app = Flask(__name__)

def process_case_description(case_description):
    output = p.run(case_description)
    return {
        "result_found": True,
        "result_description": str(output)
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        case_description = request.form.get('case_description')
        if not case_description:
            return redirect(url_for('index'))

        result = process_case_description(case_description)
        return render_template('index.html', **result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
