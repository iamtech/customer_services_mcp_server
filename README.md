# customer_services_mcp_server

A lightweight Python server for the Customer Services MCP (Message/Management/Processing) backend. This repository provides the minimal server entrypoint and modular components for account handling, API endpoints, and local data.

Project structure
- server.py — main server entrypoint (starts the application).
- requirements.txt — Python dependencies.
- accounts/ — account-related code (authentication, user management, etc.).
- api/ — API endpoint implementations and routing.
- data/ — data files, fixtures, or local storage used by the server.
- .gitignore — ignored files.

Requirements
- Python 3.8+
- Install dependencies:
  pip install -r requirements.txt

Setup
1. Clone the repo:
   git clone https://github.com/iamtech/customer_services_mcp_server.git
   cd customer_services_mcp_server

2. Create and activate a virtual environment (recommended):
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. (Optional) Configure environment variables required by the application. Check server.py and modules in accounts/ and api/ for any config keys.

Run
Start the server from the repository root:

python server.py

The server should log its listening port or endpoint on startup. If you deploy with a production server, run under a WSGI/ASGI server (e.g., gunicorn, uvicorn) as appropriate.

Development notes
- Code is organized into modular packages (accounts, api, data) to keep business logic separated from the server bootstrap.
- Add new endpoints under api/ and handlers in accounts/ as needed.

