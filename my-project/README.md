# FastAPI + n8n Integration Project

This project provides a simple integration between a FastAPI backend and [n8n](https://n8n.io/), an open-source workflow automation tool. The backend exposes an endpoint to interact with a local LLM (Large Language Model) via the Ollama API, and both services are orchestrated using Docker Compose.

## Project Structure

- `fastapi-backend/`: FastAPI app that exposes an endpoint to query a local LLM.
- `n8n-local/`: Contains a Docker Compose file to run n8n locally.
- `docker-compose.yml`: Orchestrates both FastAPI and n8n services.
- `test.py`: Example script to test the FastAPI endpoint.

## FastAPI Backend

- **Endpoint:** `POST /ask-llm`
- **Description:** Accepts a prompt and returns a response from the LLM (configured for Ollama's API).
- **Dependencies:** See `fastapi-backend/requirements.txt`.
- **Dockerized:** Yes, see `fastapi-backend/Dockerfile`.

## n8n

- **Service:** Runs in a Docker container.
- **Port:** 5678
- **Authentication:** Disabled by default for local development.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/)
- (Optional) Python 3.10+ for running scripts locally

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone  https://github.com/gothamza/simple-FastAPI-n8n-Integration.git
   cd my-project
   ```

2. **Start the services:**
   ```sh
   docker-compose up --build
   ```
   This will start both the FastAPI backend (on port 8000) and n8n (on port 5678).

3. **Test the FastAPI endpoint:**
   You can use the provided `test.py` script:
   ```sh
   python test.py
   ```
   Or use `curl`:
   ```sh
   curl -X POST http://localhost:8000/ask-llm -H "Content-Type: application/json" -d '{"prompt": "Tell me a fun fact about space."}'
   ```

4. **Access n8n:**
   Open [http://localhost:5678](http://localhost:5678) in your browser.

## Customization

- **Ollama LLM URL and Model:**
  - Change `OLLAMA_URL` and `MODEL` in `fastapi-backend/main.py` as needed.
- **n8n Data Persistence:**
  - Data is stored in a Docker volume (`n8n_data`).

## License

This project is provided as-is for educational and prototyping purposes. 