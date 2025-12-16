#!/usr/bin/env python3
"""
Example usage of the Vibe Agent as a Python library.
"""

from agent import VibeAgent


def main():
    """Demonstrate various agent capabilities."""
    
    print("="*60)
    print("  🎵 Vibe Agent - Library Usage Example 🎵")
    print("="*60)
    print()
    
    # Create an agent
    agent = VibeAgent(name="CodeBuddy", personality="friendly")
    
    # Example 1: Greetings
    print("1️⃣  Greeting:")
    response = agent.process("Hello!")
    print(f"   {response}\n")
    
    # Example 2: Calculations
    print("2️⃣  Mathematics:")
    response = agent.process("calculate 15 * 8")
    print(f"   {response}\n")
    
    # Example 3: Memory
    print("3️⃣  Memory:")
    response1 = agent.process("remember my favorite framework is Django")
    print(f"   {response1}")
    response2 = agent.process("remember my IDE is VS Code")
    print(f"   {response2}")
    response3 = agent.process("what do you remember?")
    print(f"   {response3}\n")
    
    # Example 4: Entertainment
    print("4️⃣  Entertainment:")
    response = agent.process("tell me a joke")
    print(f"   {response}\n")
    
    # Example 5: Inspiration
    print("5️⃣  Inspiration:")
    response = agent.process("inspire me")
    print(f"   {response}\n")
    
    # Example 6: Statistics
    print("6️⃣  Agent Statistics:")
    stats = agent.get_stats()
    for key, value in stats.items():
        print(f"   • {key.replace('_', ' ').title()}: {value}")
    print()
    
    # Example 7: Export conversation
    print("7️⃣  Exporting Conversation:")
    agent.export_conversation("/tmp/example_conversation.json")
    print("   ✅ Conversation exported to /tmp/example_conversation.json\n")
    
    print("="*60)
    print("  ✨ Example complete! ✨")
    print("="*60)


if __name__ == '__main__':
    main()
