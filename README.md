# infinite-experiments
A space for coding experiments, ML and AI prototypes, and small projects.

## 🎵 Vibe Agent

A fun, conversational AI agent built for experimentation and learning. Vibe Agent is a lightweight, extensible agent that can chat, calculate, remember things, and bring good vibes to your coding sessions!

### ✨ Features

- **Natural Conversation**: Chat naturally with the agent
- **Math Calculations**: Ask it to compute mathematical expressions
- **Memory System**: The agent can remember and recall information
- **Personality**: Friendly, vibing personality with jokes and inspiration
- **Multiple Interfaces**: CLI and Web UI (no external dependencies!)
- **No External Dependencies**: Built using Python standard library only
- **Extensible**: Easy to add new capabilities

### 🚀 Quick Start

#### Command Line Interface

```bash
# Run the agent interactively
python cli.py

# Run with a custom name
python cli.py --name "CodeBuddy"

# Show statistics after your session
python cli.py --stats

# Export conversation to a file
python cli.py --export conversation.json
```

#### Web Interface

```bash
# Start the web server (no external dependencies!)
python web_server.py

# Or specify a custom port
python web_server.py 8080

# Then open your browser to http://localhost:8000
```

### 💬 Example Conversations

```
💬 You: Hello!
🤖 Vibe: Hey there! I'm Vibe, your vibe agent! Ready to explore? ✨

💬 You: Calculate 42 * 1.5
🤖 Vibe: ✨ The answer is 63.0! Math is my jam! 🎵

💬 You: Remember my favorite language is Python
🤖 Vibe: Got it! I'll remember that my favorite language is Python 🧠

💬 You: Tell me a joke
🤖 Vibe: Why do programmers prefer dark mode? Because light attracts bugs! 🐛

💬 You: What do you remember?
🤖 Vibe: Here's what I remember:
• my favorite language: python
```

### 🛠️ Usage as a Library

You can also use Vibe Agent programmatically:

```python
from agent import VibeAgent

# Create an agent
agent = VibeAgent(name="MyAgent", personality="friendly")

# Process messages
response = agent.process("Hello!")
print(response)

# Check stats
stats = agent.get_stats()
print(f"Conversations: {stats['conversations']}")

# Export conversation history
agent.export_conversation("chat_history.json")
```

### 🎯 Available Commands

- **Greetings**: Say "hello", "hi", or "hey"
- **Calculate**: "calculate 10 + 5" or "compute 2 * 3"
- **Remember**: "remember my name is Alice"
- **Recall**: "what do you remember?" or "recall"
- **Jokes**: "tell me a joke" or "make me laugh"
- **Inspiration**: "inspire me" or "motivate me"
- **Help**: "help" or "what can you do?"

### 📁 Project Structure

```
.
├── agent/
│   ├── __init__.py      # Package initialization
│   └── agent.py         # Core agent implementation
├── tests/
│   ├── __init__.py      # Test configuration
│   └── test_agent.py    # Comprehensive test suite
├── cli.py               # Command-line interface
├── web_server.py        # Web interface (no dependencies!)
├── example.py           # Library usage examples
├── setup.py             # Package installation script
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

### 🧪 Testing

To run tests (if you have pytest installed):

```bash
# Install dev dependencies
pip install -r requirements.txt

# Run tests
pytest tests/
```

### 🎨 Extending the Agent

Adding new capabilities is easy! Just add a new method to the `VibeAgent` class:

```python
def _custom_capability(self, input_data: str) -> str:
    """Your custom capability."""
    return "Your response here"

# Register it in __init__
self.capabilities['custom'] = self._custom_capability
```

### 🤝 Contributing

This is an experimental project! Feel free to:
- Add new capabilities
- Improve the conversation logic
- Create new personalities
- Build integrations with other tools

### 📝 License

MIT License - See LICENSE file for details

### 🌟 Future Ideas

- [ ] Integration with LLM APIs (OpenAI, Anthropic, etc.)
- [ ] Task scheduling and reminders
- [ ] File operations and code analysis
- [ ] Web search capabilities
- [ ] Multi-agent collaboration
- [ ] Voice interface
- [ ] GUI application

---

*Built with Python and good vibes* 🎵✨
