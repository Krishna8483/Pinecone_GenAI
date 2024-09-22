
# Project Title

Retrieval-Augmented Generation (RAG) Model for QA Bot application.

Implemented a QA bot using a Retrieval-Augmented Generation (RAG) model.
Used Cohere embedding model for efficient embedding generation.
Used Pinecone DB for efficient document embedding storage and retrieval.
Integrated a generative model using Ollama/Llama3 as GPT model.

## Deployment

To deploy this project run

```bash
   streamlit run rag.py
```


## Documentation

[Pincone Documentation](https://docs.pinecone.io/guides/get-started/build-a-rag-chatbot)

[Langchain pincone](https://python.langchain.com/docs/integrations/vectorstores/pinecone/)

[Langchain LLM](https://python.langchain.com/v0.1/docs/modules/model_io/llms/)

[Cohere](https://docs.cohere.com/docs/the-cohere-platform)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`PINECONE_API_KEY`="YOUR_PINECONE_API_KEY"

(https://app.pinecone.io/organizations/-O4UH7Q77Hs3NxwfgMr-/projects/df066f74-6a84-4b43-a9fc-ae60821a7460/keys)

`COHERE_API_KEY`="YOUTR_COHERE_API_KEY"

(https://dashboard.cohere.com/api-keys)







## 🚀 About Me
I'm a Data science enthusiast, an astronomy enthusiast, in love with stars , with love for digital marketing.


## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kbhutada07/)


## 🛠 Skills
Python with data science,Machine Learning,Deep Learning,NLP,GenAI

## Lessons Learned

What did you learn while building this project? What challenges did you face and how did you overcome them?

A lot has been learned, from installing all the dependancies, understanding the problem statement and solving it with the help of documenation. I got to know more about the RAG application and GenAI and how it can be leveraged for the betterment of the society. 


## Architecture

The model consists of two main components: Retriever and Generator.

Retriever: Uses the Cohere model to generate embeddings for the input query.

Pinecone Vector Database: Stores the document embeddings and retrieves the top relevant documents based on the query embeddings.

Generator: The generative model (e.g., Ollama/Llama3) processes the retrieved documents and formulates a coherent response to the user’s query.

## Feedback

If you have any feedback, please reach out to us at krishnabhutada09710@gmail.com


## Installation

pip install -r reuirements.txt

It installs all the required dependencies