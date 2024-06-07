# Deep Justice AI

Deep Justice AI is a web application designed to assist in legal case analysis by leveraging advanced AI models. The application allows users to input a case description and returns relevant information about the case.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)

## Features
- Input case descriptions to receive AI-generated analysis.
- Uses OpenAI's GPT-3.5 for language understanding and processing.
- Integration with llama_index for document indexing and retrieval.
- User-friendly interface built with Bootstrap.

## Installation
!pip install 'llama-index-callbacks-arize-phoenix>0.1.3'
!pip install llama-index-embeddings-openai
!pip install llama-index-postprocessor-cohere-rerank
!pip install llama-index-llms-openai
!pip install 'arize-phoenix[evals]'
!pip install llama_index
!pip install pyvis
!pip install flask

### Prerequisites
- Python 3.7 or higher
- Flask
- Required Python packages (listed in `requirements.txt`)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/deep-justice-ai.git
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

## File Structure
deep-justice-ai/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # HTML template for the application
├── dataset/               # Directory containing the dataset documents
├── storage/               # Directory to store the indexed data
├── requirements.txt       # List of required Python packages
├── README.md              # This README file


