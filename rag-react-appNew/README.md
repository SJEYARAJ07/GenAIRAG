
1. Make sure your local model service is running

Open a terminal and run:

ollama serve

In another terminal, confirm the models exist:

ollama list

You should see at least:

llama3.1
nomic-embed-text

You can also sanity-check the chat model:

ollama run llama3.1

Ask a simple prompt like:

Say hello in one sentence.

If that works, Ollama is fine.

2. Make sure your PDFs are in the right folder

Put your PDF files here:

backend/data/pdfs/

Example:

backend/data/pdfs/file1.pdf
backend/data/pdfs/file2.pdf
3. Rebuild the vector database

Because you switched from OpenAI to local embeddings, rebuild Chroma before testing queries.

From the backend folder:

rm -rf data/chroma/*
python -m app.ingestion.ingest

What you want to see:

PDFs loaded
chunks created
vector database created
“Ingestion complete.”

If this fails, fix ingestion before testing anything else.

4. Start the FastAPI backend

From backend:

uvicorn app.main:app --reload --port 8001

You want to see something like:

Uvicorn running on http://127.0.0.1:8001
5. Test the backend directly first

Before touching React, test FastAPI alone.

Open:

http://127.0.0.1:8001/docs

That Swagger page is the easiest first test path for this FastAPI setup. Your project flow is React → FastAPI → RAG pipeline → vector DB, so testing /ask directly helps isolate whether the backend works before the frontend is involved.

Use POST /ask with this body:

{
  "query": "What are the main topics covered in the PDFs?"
}
Expected result

You should get a JSON response like:

{
  "answer": "..."
}
If this works

Your backend is healthy.

If this fails

The issue is in one of these:

Ollama not running
Chroma DB not built
wrong model name in .env
no PDFs loaded
import/package issue
6. Start the React frontend

Open a new terminal:

cd frontend
npm install
npm start

Then open:

http://localhost:3000

Your React frontend is just sending fetch requests to the FastAPI backend, exactly like the earlier project architecture you were building.

7. Test full end-to-end in the browser

Now test from the UI with easy questions first.

Start with:

What documents are loaded?
Summarize the PDFs.
What are the key points?

Then try a more specific question:

What does document X say about Y?
What should happen
React sends the question
FastAPI receives it
Chroma retrieves matching chunks
Ollama generates the answer
React displays the answer
