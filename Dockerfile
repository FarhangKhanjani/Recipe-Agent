FROM node:18-slim

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Set up working directory
WORKDIR /app

# Copy package files and install Node dependencies
COPY package*.json ./
RUN npm install

# Copy application files
COPY local-agent-proxy.js ./
COPY multi_tool_agent ./multi_tool_agent/

# Set up Python virtual environment
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
ENV PYTHON_PATH="/app/venv/bin/python"

# Install Python dependencies
RUN pip install google-adk

# Expose the port
EXPOSE 3001

# Start the proxy
CMD ["node", "local-agent-proxy.js"] 