# Recipe Agent

An AI-powered recipe generator agent that creates recipes based on provided ingredients.

## Features

- Generate recipes from a list of ingredients
- RESTful API for recipe generation
- Containerized for easy deployment

## Setup

### Prerequisites

- Node.js
- Python 3.x
- Docker (optional, for containerized deployment)

### Local Development

1. Clone the repository
   ```
   git clone [your-repo-url]
   cd recipe-agent
   ```

2. Set up Python environment
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Start the proxy server
   ```
   node local-agent-proxy.js
   ```

4. Access the API at `http://localhost:3001`

### Docker Deployment

1. Build the Docker image
   ```
   docker build -t recipe-agent .
   ```

2. Run the container
   ```
   docker run -p 3001:3001 recipe-agent
   ```

## API Usage

### Generate a Recipe

**Request:** 