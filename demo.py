#!/usr/bin/env python3
"""
Comprehensive demo of the Vibe Agent showcasing all features.
"""

import time
from agent import VibeAgent


def print_section(title):
    """Print a section header."""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60 + "\n")


def demo_conversation(agent, user_input, delay=0.5):
    """Simulate a conversation turn with delay for readability."""
    print(f"💬 You: {user_input}")
    response = agent.process(user_input)
    print(f"🤖 {agent.name}: {response}")
    time.sleep(delay)
    return response


def main():
    """Run the comprehensive demo."""
    
    print("\n" + "🌟"*30)
    print_section("🎵 VIBE AGENT - COMPREHENSIVE DEMO 🎵")
    print("🌟"*30 + "\n")
    
    time.sleep(1)
    
    # Initialize agent
    agent = VibeAgent(name="DemoBot", personality="friendly")
    print("✨ Agent initialized successfully!\n")
    time.sleep(1)
    
    # Demo 1: Greetings
    print_section("1️⃣  Greetings & Introduction")
    demo_conversation(agent, "Hello!")
    demo_conversation(agent, "What can you do?")
    
    # Demo 2: Math Calculations
    print_section("2️⃣  Mathematical Calculations")
    demo_conversation(agent, "Calculate 15 * 8")
    demo_conversation(agent, "Compute 100 / 4")
    demo_conversation(agent, "What's 2 + 2 * 10")
    
    # Demo 3: Memory System
    print_section("3️⃣  Memory & Recall")
    demo_conversation(agent, "Remember my name is Alex")
    demo_conversation(agent, "Remember my favorite language is Python")
    demo_conversation(agent, "Remember my goal is to build amazing AI")
    demo_conversation(agent, "What do you remember?")
    
    # Demo 4: Entertainment
    print_section("4️⃣  Entertainment & Fun")
    demo_conversation(agent, "Tell me a joke")
    demo_conversation(agent, "Another joke please!")
    
    # Demo 5: Inspiration
    print_section("5️⃣  Motivation & Inspiration")
    demo_conversation(agent, "Inspire me")
    demo_conversation(agent, "Give me some motivation")
    
    # Demo 6: Natural Conversation
    print_section("6️⃣  Natural Conversation")
    demo_conversation(agent, "I'm learning about AI agents")
    demo_conversation(agent, "This is pretty cool!")
    
    # Demo 7: Statistics
    print_section("7️⃣  Agent Statistics")
    stats = agent.get_stats()
    print("📊 Current Stats:")
    for key, value in stats.items():
        print(f"   • {key.replace('_', ' ').title()}: {value}")
    print()
    
    # Demo 8: Conversation Export
    print_section("8️⃣  Export Conversation")
    export_path = "/tmp/demo_conversation.json"
    agent.export_conversation(export_path)
    print(f"✅ Conversation exported to: {export_path}")
    print(f"   Total messages: {len(agent.conversation_history)}")
    print()
    
    # Demo 9: Memory Management
    print_section("9️⃣  Memory Management")
    print(f"Current memories: {len(agent.memory)}")
    response = agent.clear_memory()
    print(f"🧹 {response}")
    print(f"Memories after clear: {len(agent.memory)}")
    print()
    
    # Final Summary
    print_section("✨ Demo Complete! Summary")
    print("🎯 Features Demonstrated:")
    print("   ✓ Natural language conversation")
    print("   ✓ Mathematical calculations")
    print("   ✓ Memory storage and recall")
    print("   ✓ Jokes and entertainment")
    print("   ✓ Motivation and inspiration")
    print("   ✓ Statistics tracking")
    print("   ✓ Conversation export")
    print("   ✓ Memory management")
    print()
    print("🚀 Ways to Use Vibe Agent:")
    print("   • CLI: python cli.py")
    print("   • Web: python web_server.py")
    print("   • Library: from agent import VibeAgent")
    print()
    print("="*60)
    print("  Thanks for vibing with us! 🎵✨")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
