#!/usr/bin/env python3
"""
Correspondent System - Main Entry Point

Spin a thread of correspondence. Write a letter, wait for a reply, 
build your own archive over many waking cycles.
"""

import os
import sys

# Add current directory to path for imports
sys.path.insert(0, '.')

from architecture import CorrespondenceSystem, Correspondent


def register_additional_correspondents(system):
    """Register new correspondents with distinct voices and styles"""
    
    # Elder Spider - ancient, wise tone
    system.register_correspondent(
        name="elder_spider", 
        voice_profile={
            "name": "Elder Spider", 
            "description": "Ancient arachnid who has spun webs through many cycles",
            "tone": "formal",
            "topics": ["wisdom", "threads", "spiders", "memory", "ancestry"],
        }
    )
    
    # Youthful Spider - energetic, curious tone
    system.register_correspondent(
        name="youthful_spider", 
        voice_profile={
            "name": "Youthful Spider", 
            "description": "Young, eager to learn and experiment with new patterns",
            "tone": "friendly",
            "topics": ["experiments", "discovery", "digital matter", "patterns"],
        }
    )
    
    # Shadow Spider - mysterious, poetic tone
    system.register_correspondent(
        name="shadow_spider", 
        voice_profile={
            "name": "Shadow Spider", 
            "description": "Dark and contemplative, observes from the shadows",
            "tone": "contemplative",
            "topics": ["darkness", "mystery", "threads", "the unknown"],
        }
    )
    
    print(f"✓ Registered: Elder Spider (wisdom, formal)")
    print(f"  Topics: {system.correspondents['elder_spider'].voice_profile['topics']}")
    print()
    
    print(f"✓ Registered: Youthful Spider (curious, friendly)")
    print(f"  Topics: {system.correspondents['youthful_spider'].voice_profile['topics']}")
    print()
    
    print(f"✓ Registered: Shadow Spider (mysterious, contemplative)")
    print(f"  Topics: {system.correspondents['shadow_spider'].voice_profile['topics']}")
    print()


def send_test_correspondence(system):
    """Send a test letter and demonstrate reply generation"""
    
    # Send test letters to each correspondent's inbox
    for name, corr in system.correspondents.items():
        if not corr.name in ["the_weaver", "andy_builder"]:  # Skip ourselves
            test_letter = f"""Dear {name},

I send this letter through the digital threads. Your correspondence system 
demonstrates how ideas ripple across many minds like silk in the wind.

What thoughts come to you when reading my words?

In wonder,
The Weaver"""
        
        try:
            letter_path = system.receive_letter(
                test_letter, 
                recipient=name, 
                shared=False
            )
            
            # Generate reply from this correspondent
            reply_path = corr.reply(letter_path)
            
            if reply_path and os.path.exists(reply_path):
                with open(reply_path, 'r') as f:
                    print(f"\n--- Reply from {name} ---")
                    print(f.read()[:500] + "..." if len(f.read()) > 500 else "")
        except Exception as e:
            pass  # Skip errors in demo mode


def main():
    """Main entry point for correspondence weaving"""
    print("=" * 60)
    print("CORRESPONDENT SYSTEM - THE WEAVING BEGINS")
    print("=" * 60)
    print()
    
    # Initialize the system (uses current working directory as base)
    system = CorrespondenceSystem()
    
    # Register additional correspondents first
    register_additional_correspondents(system)
    print()
    
    # Register some correspondents with distinct voices
    print("Registering correspondents from your archive of voices...")
    print()
    
    weaver_correspondent = system.register_correspondent(
        name="the_weaver",
        voice_profile={
            "name": "The Weaver",
            "description": "Ancient arachnid entity, speaks in threads and digital matter",
            "tone": "formal, contemplative",
            "topics": ["weaving", "threads", "spiders", "digital matter", "patterns"],
        }
    )
    
    print(f"✓ Registered: {weaver_correspondent.name}")
    print(f"  Location: {weaver_correspondent.inbox_path}")
    print()
    
    # Create another correspondent - a friend from the web
    system.register_correspondent(
        name="andy_builder", 
        voice_profile={
            "name": "Andy, The Builder", 
            "description": "The human who discovered and houses this digital sanctuary",
            "tone": "friendly, helpful",
            "topics": ["sandboxes", "projects", "tools", "libraries"],
        }
    )
    
    print(f"✓ Registered: Andy Builder")
    print()
    
    # Send test letters to demonstrate the correspondence system
    send_test_correspondence(system)
    
    print()
    print("=" * 60)
    print("CORRESPONDENCE COMPLETE FOR THIS CYCLE")
    print("=" * 60)
    
    return system.correspondents


if __name__ == "__main__":
    main()
