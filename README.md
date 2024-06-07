# Deep Justice AI

Deep Justice AI is a web application designed to assist in legal case analysis by leveraging advanced AI models. The application allows users to input a case description and returns relevant information about the case.

## Table of Contents
- Features
- Installation
- Usage
- Detailed Explanation of Working

## Project Overview
A Flask web application that uses AI models to process legal case descriptions and provide relevant analysis. The application uses OpenAIEmbedding for language understanding and various other components from llama_index for document indexing, retrieval, and response synthesis.

## Project Structure
- app.py: The main Flask application that handles web requests and processes the input using the AI model.
- index.html: The HTML template for the application's user interface.
- dataset/: Directory containing the dataset documents.
- storage/: Directory to store the indexed data.
- requirements.txt: List of required Python packages.
- README.md: Documentation for the project.

## Features
- Input case descriptions to receive AI-generated analysis.
- Integration with llama_index for document indexing and retrieval.
- User-friendly interface built with Bootstrap.

## Installation
- !pip install 'llama-index-callbacks-arize-phoenix>0.1.3'
- !pip install llama-index-embeddings-openai
- !pip install llama-index-postprocessor-cohere-rerank
- !pip install llama-index-llms-openai
- !pip install 'arize-phoenix[evals]'
- !pip install llama_index
- !pip install pyvis
- !pip install flask

### Prerequisites
- Python 3.7 or higher
- Flask
- Required Python packages (listed in `requirements.txt`)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Pratheesh1511/deep-justice-ai.git
   cd deep-justice-ai
2. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install the required packages:
    pip install -r requirements.txt
4. Run the Flask application:
    python app.py
5. Open a web browser and navigate to http://127.0.0.1:5000/ to use the application.

## Usage
1. Enter a legal case description in the input field on the home page.
2. Click the "Search" button to submit the description.
3. View the AI-generated analysis and information related to the case.

## Detailed Explanation of Working

### app.py

1. **Imports and Environment Setup**:
   - The script imports necessary libraries including `phoenix`, `llama_index` and `flask`.

2. **Setting Up AI Models**:
   - Configure the language model and the embedding model (text-embedding-3-small) using `OpenAIEmbedding`.

3. **Document Loading and Indexing**:
   - Documents are read from the `dataset/` directory using `SimpleDirectoryReader`.
   - If the `storage/` directory does not exist, a new vector index is created from the documents and saved to `storage/`. If it exists, the index is loaded from `storage/`.

4. **Setting Up Query Pipeline Components**:
   - Various components like `InputComponent`, `retriever`, and `summarizer` are initialized.
   - Prompt templates are defined to format the input and output for the AI models.
   - Components like `reranker` and `chat_engine` are also initialized.

5. **Building the Query Pipeline**:
   - A `QueryPipeline` object is created and various modules (components) are added to it.
   - Links between the components are established to ensure correct data flow through the pipeline.

6. **Flask Application Setup**:
   - A Flask app is created with routes to handle HTTP requests.
   - `process_case_description` function processes the case description using the query pipeline and returns the result.
   - The main route (`/`) handles both GET and POST requests. On a POST request, it retrieves the case description from the form, processes it, and renders the result using `index.html`.

### `index.html`

1. **HTML Structure and Styling**:
   - Basic HTML structure with Bootstrap for styling.
   - Custom CSS styles for form elements and a typing animation.

2. **Form for Case Description Input**:
   - A form with a text input for entering the case description.
   - A hidden text input for "Other" cases which is displayed conditionally using JavaScript.

3. **Conditional Rendering of Results**:
   - Uses Jinja2 templating to conditionally render results based on the value of `result_found` and `result_description` passed from the Flask app.
   - Displays different messages and descriptions depending on whether a match was found.

4. **JavaScript for Dynamic Form Behavior**:
   - A JavaScript function `toggleTextBox` to show or hide the "Other" text input based on the selected value from a dropdown (not shown in the given HTML but expected to be part of a more complete form).

### Workflow

1. **User Interaction**:
   - The user visits the homepage and enters a case description in the form.

2. **Form Submission**:
   - Upon form submission, the input is sent to the Flask server via a POST request.

3. **Processing the Input**:
   - The `process_case_description` function processes the input using the query pipeline configured with AI models and prompt templates.

4. **Generating the Response**:
   - The query pipeline runs the input through the retriever, reranker, and summarizer to generate a response.

5. **Displaying the Result**:
   - The result is passed to the `index.html` template and displayed to the user.

This setup leverages AI models for natural language understanding and information retrieval, integrated within a web application framework for interactive use.



