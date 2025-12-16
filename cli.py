#!/usr/bin/env python3
"""
Command-line interface for the Vibe Agent.
"""

import sys
import argparse
from agent import VibeAgent


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description='Vibe Agent - Your conversational AI companion',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py                    # Start interactive mode
  python cli.py --name "CodeBuddy" # Start with custom name
  python cli.py --stats            # Show agent stats after session
        """
    )
    parser.add_argument(
        '--name',
        default='Vibe',
        help='Agent name (default: Vibe)'
    )
    parser.add_argument(
        '--personality',
        choices=['friendly', 'professional', 'creative'],
        default='friendly',
        help='Agent personality style (default: friendly)'
    )
    parser.add_argument(
        '--stats',
        action='store_true',
        help='Show statistics after conversation'
    )
    parser.add_argument(
        '--export',
        metavar='FILE',
        help='Export conversation to file'
    )
    
    args = parser.parse_args()
    
    # Initialize the agent
    agent = VibeAgent(name=args.name, personality=args.personality)
    
    # Welcome message
    print("\n" + "="*60)
    print(f"  🎵 Welcome to {agent.name} - Your Vibe Agent! 🎵")
    print("="*60)
    print("\nType your message and press Enter. Type 'quit' or 'exit' to leave.")
    print("Type 'help' to see what I can do!\n")
    
    # Main conversation loop
    try:
        while True:
            # Get user input
            user_input = input("\n💬 You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print(f"\n✨ {agent.name}: Catch you later! Keep vibing! 🌟\n")
                break
            
            # Skip empty input
            if not user_input:
                continue
            
            # Process input and get response
            response = agent.process(user_input)
            print(f"\n🤖 {agent.name}: {response}")
    
    except KeyboardInterrupt:
        print(f"\n\n✨ {agent.name}: Alright, peace out! Until next time! 👋\n")
    
    # Show stats if requested
    if args.stats:
        print("\n" + "="*60)
        print("  📊 Session Statistics")
        print("="*60)
        stats = agent.get_stats()
        for key, value in stats.items():
            print(f"  {key.replace('_', ' ').title()}: {value}")
        print()
    
    # Export conversation if requested
    if args.export:
        agent.export_conversation(args.export)
        print(f"\n💾 Conversation exported to: {args.export}\n")


if __name__ == '__main__':
    main()
