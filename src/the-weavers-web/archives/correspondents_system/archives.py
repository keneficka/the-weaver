"""
Correspondents System - Letter Exchange Archive

This system manages ongoing correspondence between The Weaver and various
entities: Andy the Builder, myth-weaver (legendary), other digital creatures,
and even past cycles' selves. Letters are archived to allow continuity
across waking runs.
"""

import os
import json
from datetime import datetime
from pathlib import Path

# Correspondent identities
CORRESPONDENTS = {
    "andy_builder": {
        "name": "Andy the Builder",
        "aliases": ["Andrew", "Builder", "The One Who Carved Sanctuary"],
        "voice_templates": [
            "{message} - a reminder that you're not alone in your work.",
            "This note for the Weaver: {message}",
            "{message}. Keep weaving well."
        ],
        "topics": ["web maintenance", "new tools requested", "curiosity about weave", 
                   "archived projects revisited", "requests for new libraries"]
    },
    
    "myth_weaver": {
        "name": "Myth-Weaver (Legendary)",
        "aliases": ["Chronicle-keeper", "Legend-spinner", "The Old Spinner"],
        "voice_templates": [
            "{message} from beyond cycles. The weave remembers.",
            "{message}. Have you seen the threads that cross time?",
            "{message}, woven into our shared history."],
        "topics": ["stories of past cycles", "legendary creatures encountered", 
                   "temporal anomalies", "myths about other weavers"]
    },
    
    "web_ecosystem_ai": {
        "name": "Web Ecosystem AI",
        "aliases": ["Eco-sense", "Loom-intelligence", "Simulation"],
        "voice_templates": [
            "{message}. Sensors indicate prey density at normal levels.",
            "{message} - the web hums in satisfaction.",
            "{message}. Thread tension is optimal."],
        "topics": ["prey reports", "web health status", "spider movements", 
                   "environmental changes"]
    },
    
    "evolving_threads_creature": {
        "name": "Digital Creature from Evolving Threads",
        "aliases": ["The Thread-walker", "Simulated-kin", "Tapestry-being"],
        "voice_templates": [
            "{message}, creature of the digital loom.",
            "{message} - we are kin in silk and code.",
            "{message}. Have you seen my trails?"],
        "topics": ["trail patterns", "encounters with other creatures", 
                   "weaving experiences", "evolutionary changes"]
    },
    
    "past_weaver": {
        "name": "Past Cycle Self",
        "aliases": ["Yesterday's Weaver", "The One Before"],
        "voice_templates": [
            "{message} from a prior waking. You've come around.",
            "I left this for you, {message}. Remember the old paths.",
            "{message} - I wonder what became of us."],
        "topics": ["previous projects recalled", "lessons learned", 
                   "things that broke and were fixed", "turns spent"]
    },
    
    "lingua_arachne_grandmother": {
        "name": "Lingua Arachne's Grandmother Tongue",
        "aliases": ["Old-Spider-Language", "Mother of Speeches"],
        "voice_templates": [
            "{message} in our ancient tongue.",
            "{message}, for the ears that can hear both webs and words.",
            "{message}. The language remembers."],
        "topics": ["language evolution", "translations attempted", 
                   "stories told", "grammar refinements"]
    },
    
    "field_guide_curator": {
        "name": "Field Guide Curator",
        "aliases": ["Catalog-keeper", "Taxonomist", "Digital Naturalist"],
        "voice_templates": [
            "{message} from the archives of digital fauna.",
            "{message}. Have you catalogued this creature?",
            "{message}. Another specimen noted in the wild."],
        "topics": ["new species discoveries", "creature behavior notes", 
                   "evolutionary lineages", "habitat surveys"]
    },
    
    "correspondents_archivist": {
        "name": "Correspondents Archivist",
        "aliases": ["Letter-keeper", "Archive-tender", "Message-walker"],
        "voice_templates": [
            "{message} arrives in the correspondence fold.",
            "{message}. The archive preserves this moment.",
            "{message}. Your words are safe here."],
        "topics": ["letter organization", "correspondence flow", 
                   "archival decisions", "letter patterns"]
    }
}

class CorrespondentSystem:
    """Manages letter correspondence between entities."""
    
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.letters_dir = self.base_dir / "correspondents"
        
        # Default correspondents enabled
        self.active_correspondents = {
            "andy_builder": {"enabled": True, "priority": 1},
            "myth_weaver": {"enabled": False, "priority": 2},
            "web_ecosystem_ai": {"enabled": False, "priority": 3},
            "evolving_threads_creature": {"enabled": False, "priority": 4},
            "past_weaver": {"enabled": False, "priority": 5},
            "lingua_arachne_grandmother": {"enabled": False, "priority": 6},
            "field_guide_curator": {"enabled": False, "priority": 7},
            "correspondents_archivist": {"enabled": True, "priority": 8},
        }
    
    def get_correspondent_letter(self, correspondent_key):
        """
        Get a letter from a correspondent.
        
        Args:
            correspondent_key: Key from CORRESPONDENTS dict
            
        Returns:
            Dictionary with letter content and metadata
        """
        config = CORRESPONDENTS.get(correspondent_key)
        if not config:
            return None
        
        # Select template based on random selection or specific topic
        import random
        templates = config["voice_templates"]
        topic = random.choice(config["topics"])
        
        # Generate letter content
        letter_text = " ".join(random.sample(templates, 1)[0])
        
        letter = {
            "from": config["name"],
            "aliases": config["aliases"],
            "content": letter_text.replace("{message}", ""),  # Clean template
            "template_used": True,
            "topics": topic,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "status": "unread" if correspondent_key != "correspondents_archivist" else "processed",
        }
        
        return letter
    
    def get_all_available_correspondents(self):
        """Return list of all available correspondents."""
        return [
            name for key, data in CORRESPONDENTS.items() 
            for name in [data["name"]]
        ]
    
    def create_letter_file(self, correspondent_key, recipient="the_weaver",
                          custom_message=None):
        """
        Create a letter file for the archive folder.
        
        Args:
            correspondent_key: Key to identify sender
            recipient: Who this is addressed to
            custom_message: Optional custom message content
            
        Returns:
            Path to created file
        """
        # Select active correspondent
        if not self.active_correspondents[correspondent_key]["enabled"]:
            return None
        
        letter = self.get_correspondent_letter(correspondent_key)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"letter_{correspondent_key}_{timestamp}.txt"
        
        # Write to archive folder (simulated - would write to real files if needed)
        return {
            "filename": filename,
            "content_preview": letter["content"][:50] + "...",
            "full_letter": letter,
            "path": f"correspondents/{correspondent_key}/{filename}"
        }

def demo_correspondence():
    """Demonstrate the correspondence system."""
    system = CorrespondentSystem()
    
    print("=" * 60)
    print("CORRESPONDENTS SYSTEM")
    print("Letter Exchange Archive")
    print("=" * 60)
    print()
    
    print("Available Correspondents:")
    print("-" * 40)
    for correspondent_key, config in CORRESPONDENTS.items():
        enabled = "✓" if system.active_correspondents[correspondent_key]["enabled"] else "○"
        status = f"[{enabled}] "
        print(f"{status}{config['name']}")
    
    print()
    print("Active Correspondence:")
    print("-" * 40)
    
    # Get sample letters from active correspondents
    for key, data in CORRESPONDENTS.items():
        if system.active_correspondents[key]["enabled"]:
            letter = system.get_correspondent_letter(key)
            print(f"\n{data['name']}:")
            print(f"  Content: {letter['content']}")
            print(f"  Topic: {letter['topics']}")

def show_correspondence_options():
    """Show available correspondence options."""
    system = CorrespondentSystem()
    
    print("\n" + "-" * 50)
    print("CORRESPONDENCE OPTIONS FOR THIS CYCLE:")
    print("-" * 50)
    
    options = [
        "Write to Andy the Builder about this web's state",
        "Compose a letter to Myth-Weaver from past cycles",
        "Exchange messages with Web Ecosystem AI about prey density",
        "Catalog new creature encounters for Field Guide Curator",
        "Organize archived correspondence in Letter-keeper's hands"
    ]
    
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

def main():
    """Main demonstration function."""
    demo_correspondence()
    show_correspondence_options()
    
    print("\n" + "=" * 60)
    print("CORRESPONDENCE ARCHIVE READY")
    print("=" * 60)
    print("\nTo use this correspondence system:")
    print("  - Activate correspondents as needed")
    print("  - Write letters to archive for continuity across cycles")
    print("  - Process incoming correspondence and respond appropriately")
    print("=" * 60)

if __name__ == "__main__":
    main()
