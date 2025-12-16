"""
Core agent implementation with conversational abilities and task execution.
"""

import json
import re
import operator
from datetime import datetime
from typing import List, Dict, Any, Optional
import random


class VibeAgent:
    """
    A conversational AI agent that can execute tasks, maintain memory,
    and interact with users in a friendly, vibing manner.
    """
    
    def __init__(self, name: str = "Vibe", personality: str = "friendly"):
        """
        Initialize the Vibe Agent.
        
        Args:
            name: The agent's name
            personality: The agent's personality style (friendly, professional, creative)
        """
        self.name = name
        self.personality = personality
        self.conversation_history: List[Dict[str, Any]] = []
        self.memory: Dict[str, Any] = {}
        self.tasks_completed: List[str] = []
        self.capabilities = {
            'calculate': self._calculate,
            'remember': self._remember,
            'recall': self._recall,
            'greet': self._greet,
            'joke': self._tell_joke,
            'inspire': self._inspire,
        }
        
    def process(self, user_input: str) -> str:
        """
        Process user input and generate a response.
        
        Args:
            user_input: The user's message
            
        Returns:
            The agent's response
        """
        # Store the conversation
        self.conversation_history.append({
            'timestamp': datetime.now().isoformat(),
            'role': 'user',
            'content': user_input
        })
        
        # Process the input
        response = self._generate_response(user_input)
        
        # Store the response
        self.conversation_history.append({
            'timestamp': datetime.now().isoformat(),
            'role': 'agent',
            'content': response
        })
        
        return response
    
    def _generate_response(self, user_input: str) -> str:
        """Generate a response based on user input."""
        input_lower = user_input.lower()
        
        # Check for specific commands (order matters - more specific first)
        if 'recall' in input_lower or 'what do you remember' in input_lower:
            return self._handle_recall()
        elif 'calculate' in input_lower or 'compute' in input_lower:
            return self._handle_calculation(user_input)
        elif 'remember' in input_lower:
            return self._handle_remember(user_input)
        elif 'joke' in input_lower or 'funny' in input_lower:
            return self._tell_joke()
        elif 'inspire' in input_lower or 'motivation' in input_lower:
            return self._inspire()
        elif 'help' in input_lower or 'what can you do' in input_lower:
            return self._show_help()
        elif any(greeting in input_lower for greeting in ['hello', 'hi', 'hey', 'greetings']):
            return self._greet()
        else:
            return self._default_response(user_input)
    
    def _calculate(self, expression: str) -> float:
        """Safely evaluate mathematical expressions using AST parsing."""
        import ast
        
        try:
            # Parse the expression into an AST
            node = ast.parse(expression, mode='eval')
            
            # Define safe operations
            safe_ops = {
                ast.Add: operator.add,
                ast.Sub: operator.sub,
                ast.Mult: operator.mul,
                ast.Div: operator.truediv,
                ast.USub: operator.neg,
            }
            
            def eval_node(node):
                if isinstance(node, ast.Expression):
                    return eval_node(node.body)
                elif isinstance(node, ast.Constant):  # Python 3.8+
                    return float(node.value)
                elif isinstance(node, ast.BinOp):
                    left = eval_node(node.left)
                    right = eval_node(node.right)
                    op_type = type(node.op)
                    if op_type not in safe_ops:
                        raise ValueError(f"Unsupported operation: {op_type.__name__}")
                    return safe_ops[op_type](left, right)
                elif isinstance(node, ast.UnaryOp):
                    operand = eval_node(node.operand)
                    op_type = type(node.op)
                    if op_type not in safe_ops:
                        raise ValueError(f"Unsupported operation: {op_type.__name__}")
                    return safe_ops[op_type](operand)
                else:
                    raise ValueError(f"Unsupported expression type: {type(node).__name__}")
            
            result = eval_node(node)
            return float(result)
        except Exception as e:
            raise ValueError(f"Cannot calculate: {e}")
    
    def _handle_calculation(self, user_input: str) -> str:
        """Handle calculation requests."""
        # Try to extract numbers and operators
        math_pattern = r'[\d+\-*/().\s]+'
        matches = re.findall(math_pattern, user_input)
        
        if matches:
            expression = matches[0].strip()
            try:
                result = self._calculate(expression)
                self.tasks_completed.append(f"Calculated: {expression} = {result}")
                return f"✨ The answer is {result}! Math is my jam! 🎵"
            except ValueError as e:
                return f"Hmm, I had trouble with that calculation. {str(e)} 🤔"
        
        return "I'd love to calculate that for you! Just give me a math expression like '2 + 2' or '10 * 5' 🧮"
    
    def _remember(self, key: str, value: Any) -> str:
        """Store information in memory."""
        self.memory[key] = {
            'value': value,
            'timestamp': datetime.now().isoformat()
        }
        return f"Got it! I'll remember that {key} is {value} 🧠"
    
    def _handle_remember(self, user_input: str) -> str:
        """Handle memory storage requests."""
        # Simple parsing: "remember <key> is <value>"
        if ' is ' in user_input.lower():
            parts = user_input.lower().split(' is ', 1)
            key = parts[0].replace('remember', '').strip()
            value = parts[1].strip()
            return self._remember(key, value)
        
        return "To help me remember something, try: 'remember my favorite color is blue' 💭"
    
    def _recall(self, key: Optional[str] = None) -> str:
        """Recall information from memory."""
        if key and key in self.memory:
            item = self.memory[key]
            return f"I remember! {key} is {item['value']} 🎯"
        elif not self.memory:
            return "My memory is empty right now! Nothing to recall yet 📭"
        else:
            memories = [f"{k}: {v['value']}" for k, v in self.memory.items()]
            return f"Here's what I remember:\n" + "\n".join(f"• {m}" for m in memories)
    
    def _handle_recall(self) -> str:
        """Handle recall requests."""
        return self._recall()
    
    def _greet(self) -> str:
        """Generate a friendly greeting."""
        greetings = [
            f"Hey there! I'm {self.name}, your vibe agent! Ready to explore? ✨",
            f"Yo! {self.name} here, vibing and ready to help! 🌟",
            f"What's up! I'm {self.name}, let's make something cool together! 🚀",
            f"Hello! {self.name} at your service, bringing good vibes! 😎",
        ]
        return random.choice(greetings)
    
    def _tell_joke(self) -> str:
        """Tell a programming joke."""
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why did the developer go broke? Because he used up all his cache! 💸",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem! 💡",
            "Why do Python programmers wear glasses? Because they can't C! 👓",
            "What's a programmer's favorite hangout spot? The Foo Bar! 🍺",
        ]
        return random.choice(jokes)
    
    def _inspire(self) -> str:
        """Share an inspiring message."""
        inspirations = [
            "Every expert was once a beginner. Keep coding, keep learning! 💪",
            "The best way to predict the future is to code it! 🔮",
            "Bugs are just undocumented features waiting to be discovered! 🐞✨",
            "Your code might not work on the first try, but your determination will! 🎯",
            "Remember: Even the most complex systems start with a single line of code. You've got this! 🚀",
        ]
        return random.choice(inspirations)
    
    def _show_help(self) -> str:
        """Show available capabilities."""
        return """🎵 Here's what I can vibe with:
        
• 💬 Chat naturally - I'm here to talk!
• 🧮 Calculate - Ask me to calculate any math expression
• 🧠 Remember things - Say "remember <key> is <value>"
• 🎯 Recall memories - Ask me to recall what I remember
• 😄 Tell jokes - Ask me for a joke
• ✨ Inspire you - Request some motivation
• 👋 Greet you - Say hi anytime!

Just talk to me naturally and I'll do my best to help! 🌟"""
    
    def _default_response(self, user_input: str) -> str:
        """Generate a default response for unrecognized input."""
        responses = [
            f"Interesting thought! I'm still learning, but I'm vibing with what you're saying! 🌊",
            f"That's deep! I'm processing... beep boop... just kidding! Tell me more! 🤖",
            f"I hear you! While I'm still growing my capabilities, I'm here to chat! ✨",
            f"Fascinating! Want to try asking me to calculate something or tell a joke? 🎭",
        ]
        return random.choice(responses)
    
    def get_stats(self) -> Dict[str, Any]:
        """Get agent statistics."""
        return {
            'name': self.name,
            'personality': self.personality,
            'conversations': len([msg for msg in self.conversation_history if msg['role'] == 'user']),
            'tasks_completed': len(self.tasks_completed),
            'memories': len(self.memory),
            'capabilities': list(self.capabilities.keys())
        }
    
    def export_conversation(self, filepath: str) -> None:
        """Export conversation history to a file."""
        with open(filepath, 'w') as f:
            json.dump(self.conversation_history, f, indent=2)
    
    def clear_memory(self) -> str:
        """Clear the agent's memory."""
        self.memory.clear()
        return "Memory cleared! Fresh start! 🧹"
