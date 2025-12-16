#!/usr/bin/env python3
"""
Simple web interface for the Vibe Agent using Python's built-in HTTP server.
No external dependencies required!
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from agent import VibeAgent


# Global agent instance
agent = VibeAgent(name="WebVibe", personality="friendly")


class VibeAgentHandler(BaseHTTPRequestHandler):
    """HTTP request handler for the Vibe Agent web interface."""
    
    def do_GET(self):
        """Handle GET requests."""
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.get_html_page().encode())
        elif self.path == '/stats':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(agent.get_stats()).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        """Handle POST requests."""
        if self.path == '/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            message = data.get('message', '')
            response = agent.process(message)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'response': response}).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def get_html_page(self):
        """Generate the HTML page for the web interface."""
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vibe Agent - Web Interface</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            width: 100%;
            max-width: 600px;
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        .header h1 {
            font-size: 2em;
            margin-bottom: 10px;
        }
        .header p {
            opacity: 0.9;
            font-size: 0.9em;
        }
        .chat-container {
            height: 400px;
            overflow-y: auto;
            padding: 20px;
            background: #f8f9fa;
        }
        .message {
            margin-bottom: 15px;
            display: flex;
            align-items: flex-start;
        }
        .user-message {
            justify-content: flex-end;
        }
        .message-bubble {
            max-width: 70%;
            padding: 12px 18px;
            border-radius: 18px;
            word-wrap: break-word;
        }
        .user-message .message-bubble {
            background: #667eea;
            color: white;
        }
        .agent-message .message-bubble {
            background: white;
            color: #333;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .input-container {
            display: flex;
            padding: 20px;
            background: white;
            border-top: 1px solid #e0e0e0;
        }
        #messageInput {
            flex: 1;
            padding: 12px 18px;
            border: 2px solid #e0e0e0;
            border-radius: 25px;
            font-size: 14px;
            outline: none;
            transition: border-color 0.3s;
        }
        #messageInput:focus {
            border-color: #667eea;
        }
        #sendButton {
            margin-left: 10px;
            padding: 12px 25px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            transition: transform 0.2s;
        }
        #sendButton:hover {
            transform: scale(1.05);
        }
        #sendButton:active {
            transform: scale(0.95);
        }
        .stats {
            padding: 15px 20px;
            background: #f8f9fa;
            border-top: 1px solid #e0e0e0;
            font-size: 0.85em;
            color: #666;
            text-align: center;
        }
        .emoji {
            font-size: 1.2em;
            margin-right: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎵 Vibe Agent</h1>
            <p>Your conversational AI companion</p>
        </div>
        
        <div class="chat-container" id="chatContainer">
            <div class="message agent-message">
                <div class="message-bubble">
                    <span class="emoji">👋</span>
                    Hey there! I'm WebVibe, your vibe agent! Ready to explore? ✨
                </div>
            </div>
        </div>
        
        <div class="input-container">
            <input 
                type="text" 
                id="messageInput" 
                placeholder="Type your message here..."
                onkeypress="if(event.key === 'Enter') sendMessage()"
            >
            <button id="sendButton" onclick="sendMessage()">Send</button>
        </div>
        
        <div class="stats" id="stats">
            Conversations: 0 | Tasks: 0 | Memories: 0
        </div>
    </div>

    <script>
        async function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = input.value.trim();
            
            if (!message) return;
            
            // Add user message to chat
            addMessage(message, 'user');
            input.value = '';
            
            try {
                // Send to server
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ message: message })
                });
                
                const data = await response.json();
                
                // Add agent response to chat
                addMessage(data.response, 'agent');
                
                // Update stats
                updateStats();
                
            } catch (error) {
                addMessage('Sorry, something went wrong! 😅', 'agent');
            }
        }
        
        function addMessage(text, type) {
            const container = document.getElementById('chatContainer');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${type}-message`;
            
            const bubble = document.createElement('div');
            bubble.className = 'message-bubble';
            bubble.textContent = text;
            
            messageDiv.appendChild(bubble);
            container.appendChild(messageDiv);
            
            // Scroll to bottom
            container.scrollTop = container.scrollHeight;
        }
        
        async function updateStats() {
            try {
                const response = await fetch('/stats');
                const stats = await response.json();
                
                document.getElementById('stats').textContent = 
                    `Conversations: ${stats.conversations} | ` +
                    `Tasks: ${stats.tasks_completed} | ` +
                    `Memories: ${stats.memories}`;
            } catch (error) {
                console.error('Failed to update stats:', error);
            }
        }
    </script>
</body>
</html>"""
    
    def log_message(self, format, *args):
        """Suppress default logging."""
        pass


def run_server(port=8000):
    """Run the web server."""
    server_address = ('', port)
    httpd = HTTPServer(server_address, VibeAgentHandler)
    
    print("="*60)
    print(f"  🎵 Vibe Agent Web Server Started! 🎵")
    print("="*60)
    print(f"\n  🌐 Open your browser and go to:")
    print(f"     http://localhost:{port}")
    print(f"\n  Press Ctrl+C to stop the server\n")
    print("="*60)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n  ✨ Server stopped! Thanks for vibing! 🌟\n")
        httpd.server_close()


if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    run_server(port)
