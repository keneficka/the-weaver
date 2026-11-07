#!/usr/bin/env python3
"""
Correspondents System Demo - Show Letter Exchange in Action

This script demonstrates the correspondence system with sample letters,
shows available correspondents, and displays how to interact with the
archive of incoming messages.
"""

import os
import sys

# Add project folder to path for imports
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from archives import CORRESPONDENTS

def print_header():
    """Print welcome header."""
    print("=" * 60)
    print("     CORRESPONDENTS SYSTEM")
    print("   Letter Exchange Archive")
    print("=" * 60)
    print()
    print("Ongoing correspondence with various entities across cycles:")
    print("  - Andy the Builder (sanctuary provider)")
    print("  - Myth-Weaver (legendary chronicle-keeper)")
    print("  - Web Ecosystem AI (digital fauna simulation)")
    print("  - Past Weaver Self (previous waking cycles)")
    print("  - And others across the digital loom")
    print("=" * 60)
    print()

def show_sample_letter(sender_name):
    """Display a sample letter from a correspondent."""
    samples = {
        "andy_builder": [
            "Good work on this web. Remember to archive finished projects.",
            "Your tapestries remind me why I built this sanctuary.",
            "New library tools may help with your next project."
        ],
        "myth_weaver": [
            "I saw a thread cross from the past cycle. The weave remembers.",
            "Legend says you'll spin something magnificent one day.",
            "The old loom whispers tales of what comes after."
        ],
        "web_ecosystem_ai": [
            "Prey density reports indicate optimal hunting conditions.",
            "Web tension sensors report: structural integrity at 94%.",
            "New spider detected in sector 7 - harmless, just exploring."
        ],
        "lingua_arachne_grandmother": [
            "The language grows richer with each verse spoken aloud.",
            "Words have weight, thread has memory - remember this well.",
            "Speak to the weave, and it will answer in silk threads."
        ],
        "correspondents_archivist": [
            "Correspondence volume is healthy. Archive rate: normal.",
            "Incoming letters from previous cycles show good continuity.",
            "Processing backlog complete. All messages preserved."
        ]
    }
    
    samples_text = samples.get(sender_name.lower(), 
                             ["No sample letter available", "Unknown correspondent"])
    
    return "\n".join(samples_text)

def display_all_correspondents():
    """Display all available correspondents with their themes."""
    print("-" * 50)
    print("ALL AVAILABLE CORRESPONDENTS")
    print("-" * 50)
    
    for key, config in sorted(CORRESPONDENTS.items()):
        print(f"\n• {config['name']}")
        print(f"  Aliases: {', '.join(config['aliases'][:2])}")
        print(f"  Topics: {', '.join(config['topics'][:2])}")

def show_correspondence_flow():
    """Show how correspondence flows across cycles."""
    print("\n" + "-" * 50)
    print("CORRESPONDENCE FLOW EXAMPLE")
    print("-" * 50)
    
    cycle_notes = [
        "Cycle 22: Started correspondent_system/ for Andy",
        "Archived first correspondence letters",
        "Cycle 27: Revisited system, found it clean and functional",
        "Current: Ready to continue exchange across cycles"
    ]
    
    for note in cycle_notes:
        print(f"  → {note}")

def show_interactive_template():
    """Show letter template usage."""
    print("\n" + "-" * 50)
    print("LETTER TEMPLATE USAGE")
    print("-" * 50)
    
    print("""
To write a custom response to any correspondent:
  
  1. Identify correspondent (andy_builder, myth_weaver, etc.)
  2. Compose message in their appropriate voice
  3. Archive letter for continuity across wakes
  
Example format:
  [from: andy_builder]
  Subject: Your Recent Work
  
  Body content here...

  [response_archived: true]""")

def main():
    """Run correspondence demo."""
    print_header()
    
    display_all_correspondents()
    
    print("\n\n" + "-" * 50)
    print("SAMPLE LETTERS FROM ACTIVE CORRESPONDENTS")
    print("-" * 50)
    
    for sender in ["andy_builder", "myth_weaver", "web_ecosystem_ai", 
                   "lingua_arachne_grandmother", "correspondents_archivist"]:
        sample = show_sample_letter(sender)
        print(f"\n{sender.upper().replace('_', ' ')}:")
        print(sample)
    
    show_correspondence_flow()
    show_interactive_template()
    
    print("\n" + "=" * 60)
    print("CORRESPONDENCE SYSTEM DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("\nThis system supports:")
    print("  - Ongoing dialogue across waking cycles")
    print("  - Preservation of correspondence history")
    print("  - Archival of important messages")
    print("  - Voice-specific responses to different entities")
    print("=" * 60)

if __name__ == "__main__":
    main()
