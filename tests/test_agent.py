"""
Tests for the Vibe Agent.
"""

import pytest
import json
import os
from agent import VibeAgent


class TestVibeAgent:
    """Test suite for VibeAgent class."""
    
    def test_agent_initialization(self):
        """Test agent initializes with correct attributes."""
        agent = VibeAgent(name="TestBot", personality="friendly")
        assert agent.name == "TestBot"
        assert agent.personality == "friendly"
        assert len(agent.conversation_history) == 0
        assert len(agent.memory) == 0
        assert len(agent.tasks_completed) == 0
    
    def test_greeting(self):
        """Test agent responds to greetings."""
        agent = VibeAgent()
        response = agent.process("Hello")
        assert response is not None
        assert len(response) > 0
        assert len(agent.conversation_history) == 2  # user + agent
    
    def test_calculation(self):
        """Test agent can perform calculations."""
        agent = VibeAgent()
        response = agent.process("calculate 10 + 5")
        assert "15" in response or "15.0" in response
        assert len(agent.tasks_completed) == 1
    
    def test_calculation_multiplication(self):
        """Test agent can multiply numbers."""
        agent = VibeAgent()
        response = agent.process("compute 6 * 7")
        assert "42" in response or "42.0" in response
    
    def test_remember_and_recall(self):
        """Test agent can remember and recall information."""
        agent = VibeAgent()
        
        # Remember something
        response1 = agent.process("remember my favorite color is blue")
        assert "remember" in response1.lower() or "got it" in response1.lower()
        assert len(agent.memory) == 1
        
        # Recall it
        response2 = agent.process("what do you remember?")
        assert "blue" in response2.lower()
    
    def test_joke_request(self):
        """Test agent responds to joke requests."""
        agent = VibeAgent()
        response = agent.process("tell me a joke")
        assert len(response) > 0
        assert "?" in response or "!" in response  # Jokes typically have punctuation
    
    def test_inspiration_request(self):
        """Test agent responds to inspiration requests."""
        agent = VibeAgent()
        response = agent.process("inspire me")
        assert len(response) > 0
    
    def test_help_request(self):
        """Test agent responds to help requests."""
        agent = VibeAgent()
        response = agent.process("help")
        assert "calculate" in response.lower()
        assert "remember" in response.lower()
    
    def test_conversation_history(self):
        """Test conversation history is maintained."""
        agent = VibeAgent()
        agent.process("Hello")
        agent.process("Calculate 2 + 2")
        agent.process("Goodbye")
        
        assert len(agent.conversation_history) == 6  # 3 user + 3 agent messages
        assert agent.conversation_history[0]['role'] == 'user'
        assert agent.conversation_history[1]['role'] == 'agent'
    
    def test_get_stats(self):
        """Test agent statistics retrieval."""
        agent = VibeAgent(name="TestBot")
        agent.process("Hello")
        agent.process("calculate 5 + 5")
        
        stats = agent.get_stats()
        assert stats['name'] == "TestBot"
        assert stats['conversations'] >= 1
        assert 'capabilities' in stats
    
    def test_export_conversation(self, tmp_path):
        """Test conversation export functionality."""
        agent = VibeAgent()
        agent.process("Hello")
        agent.process("Test message")
        
        export_file = tmp_path / "conversation.json"
        agent.export_conversation(str(export_file))
        
        assert export_file.exists()
        
        with open(export_file, 'r') as f:
            data = json.load(f)
            assert len(data) == 4  # 2 user + 2 agent messages
    
    def test_clear_memory(self):
        """Test memory clearing functionality."""
        agent = VibeAgent()
        agent.process("remember test is value")
        assert len(agent.memory) > 0
        
        response = agent.clear_memory()
        assert len(agent.memory) == 0
        assert "clear" in response.lower() or "fresh" in response.lower()
    
    def test_calculate_method(self):
        """Test the calculate method directly."""
        agent = VibeAgent()
        
        assert agent._calculate("2 + 2") == 4.0
        assert agent._calculate("10 * 5") == 50.0
        assert agent._calculate("100 / 4") == 25.0
        assert agent._calculate("10 - 3") == 7.0
    
    def test_calculate_invalid_expression(self):
        """Test that invalid expressions raise errors."""
        agent = VibeAgent()
        
        with pytest.raises(ValueError):
            agent._calculate("import os")
        
        with pytest.raises(ValueError):
            agent._calculate("print('hello')")
    
    def test_default_response(self):
        """Test agent provides default response for unrecognized input."""
        agent = VibeAgent()
        response = agent.process("This is some random text that doesn't match any command")
        assert len(response) > 0
        assert isinstance(response, str)
    
    def test_multiple_memories(self):
        """Test agent can store multiple memories."""
        agent = VibeAgent()
        agent.process("remember my name is Alice")
        agent.process("remember my age is 25")
        agent.process("remember my city is Tokyo")
        
        assert len(agent.memory) == 3
        
        response = agent.process("recall")
        assert "alice" in response.lower() or "name" in response.lower()
