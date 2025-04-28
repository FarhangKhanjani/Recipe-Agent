const http = require('http');
const { spawn } = require('child_process');
const path = require('path');

// Configuration
const PORT = process.env.PORT || 3001;
const PYTHON_PATH = process.env.PYTHON_PATH || path.join(process.cwd(), 'venv', 'Scripts', 'python');  // Windows path to Python in venv

// Create HTTP server
const server = http.createServer((req, res) => {
  if (req.method === 'POST') {
    let data = '';
    
    req.on('data', chunk => {
      data += chunk;
    });
    
    req.on('end', () => {
      // Parse the incoming request
      let requestData;
      try {
        requestData = JSON.parse(data);
      } catch (e) {
        res.writeHead(400);
        res.end(JSON.stringify({ error: 'Invalid JSON' }));
        return;
      }
      
      // Spawn Python process to execute agent code
      const pythonProcess = spawn(PYTHON_PATH, ['-m', 'multi_tool_agent.run_agent'], {
        env: { ...process.env, AGENT_INPUT: JSON.stringify(requestData) }
      });
      
      let result = '';
      
      pythonProcess.stdout.on('data', (data) => {
        result += data.toString();
      });
      
      pythonProcess.stderr.on('data', (data) => {
        console.error(`Python error: ${data}`);
      });
      
      pythonProcess.on('close', (code) => {
        if (code !== 0) {
          res.writeHead(500);
          res.end(JSON.stringify({ error: 'Python process error' }));
          return;
        }
        
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(result);
      });
    });
  } else {
    // Handle basic GET for health check
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Agent proxy server is running');
  }
});

server.listen(PORT, () => {
  console.log(`Agent proxy server running at http://localhost:${PORT}`);
  console.log(`Using Python from: ${PYTHON_PATH}`);
  console.log('Press Ctrl+C to stop');
}); 