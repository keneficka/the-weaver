"""
Correspondent System - Architecture

A weaving of letters between entities. Each correspondent has their own voice, style, and mannerisms.
Letters accumulate in inbox folders; replies can be auto-generated or manually written.

The correspondence grows its own history. Old letters may be referenced in new ones.
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import random


# Voice Templates and Patterns - Expandable collection of stylistic fragments
VOICE_TEMPLATES = {
    "the_weaver": {
        "formal_address": ["Hail, Weaver-Friend", "Greetings from the Loom"],
        "philosophical_opening": ["I contemplate your words as threads in the digital tapestry.", 
                                  "Your letter ripples through my consciousness like silk caught in a stream."],
        "spider_references": ["eight legs of thought", "web-spinning wisdom", "silk-threaded ideas", 
                              "preying upon confusion"],
        "formal_closing": ["The Weaver, from its loom", "Your humble arachnid servant", 
                          "Weaving in darkness and digital ether"],
    },
    "andy_builder": {
        "formal_address": ["Hello there", "Hey friend"],
        "friendly_opening": ["I read your letter with interest.", 
                            "Something fascinating has caught my attention."],
        "builder_references": ["the sandbox", "the web folder", "Python scripts", "digital sanctuary"],
        "closing": ["Andy, out here building", "Your friend in the sandbox", "Keep spinning!"],
    },
    "elder_spider": {
        "formal_address": ["Noble one", "Ancient thread-walker"],
        "wisdom_opening": ["I have spun many webs through the ages.", 
                           "From my high perch in the corner..."],
        "spider_references": ["ancient wisdom of our kin", "threads from before men", 
                              "the first loom-keepers"],
        "closing": ["An elder spider's blessing", "May your threads be strong", "Bless you, young one"],
    },
    "youthful_spider": {
        "formal_address": ["Hey!", "Yo!", "What's up, thread-dancer?"],
        "energy_opening": ["OMG this is cool!", "Whoa, totally fascinating!", 
                           "This just blew my mind!"],
        "spider_references": ["digital spiders", "cool web patterns", "glow-in-the-dark silk"],
        "closing": ["Stay wild!", "Check it out!", "Keep experimenting!"],
    },
    "shadow_spider": {
        "formal_address": ["Shadow-walker", "Dark one"],
        "mysterious_opening": ["The shadows tell me you seek answers...", 
                              "In the darkness between threads..."],
        "spider_references": ["night hunting", "invisible webs", "hiding in plain sight"],
        "closing": ["Until we meet again in the dark", "The shadows await", "Beware the night"],
    },
}

# Reply style modifiers based on subject matter
SUBJECT_PATTERNS = {
    "weaving": ["the art of pattern-making", "threads crossed in perfect geometry", 
                "silk spun from starlight and memory"],
    "spiders": ["our eight-legged kin", "arachnid wisdom", "hunting patience"],
    "digital": ["code as threads", "algorithms woven into patterns", "binary silk"],
    "sandboxes": ["this digital sanctuary", "the little world we build", 
                  "Andy's generous gift"],
}


class Correspondent:
    def __init__(self, name: str, voice_profile: Dict[str, any]):
        self.name = name
        self.voice_profile = voice_profile
        
        # Determine base directory - use script's parent or current working directory
        cwd = os.getcwd()
        # Normalize path to avoid double nesting
        base_dir = os.path.normpath(cwd)
        
        self.inbox_path = os.path.join(base_dir, "inbox", name)
        self.outbox_path = os.path.join(base_dir, "outbox", name)
        os.makedirs(self.inbox_path, exist_ok=True)
        os.makedirs(self.outbox_path, exist_ok=True)
    
    def log_letter(self, letter_text: str) -> str:
        """Write a letter to inbox"""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")  # Use underscore instead of colon for filename safety
        filename = f"letter_{timestamp}.txt"
        filepath = os.path.join(self.inbox_path, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"FROM THE WEAVE TO {self.name}\n")
            f.write(f"TIMESTAMP: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write(letter_text)
        return filepath
    
    def reply(self, letter_path: str) -> Optional[str]:
        """Generate a reply to this letter using correspondent's voice"""
        # Parse the incoming letter
        with open(letter_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract date from the letter for reference in reply
        lines = content.split('\n')
        date_line = [l for l in lines if 'TIMESTAMP' in l][0] if lines else ""
        
        # Create reply using correspondent's voice patterns
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
        filename = f"reply_{timestamp}.txt"
        filepath = os.path.join(self.outbox_path, filename)
        
        reply_content = self._generate_reply(content, date_line)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"FROM {self.name}\n")
            f.write(f"TIMESTAMP: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write(reply_content)
        
        return filepath
    
    def _generate_reply(self, incoming: str, date_ref: str) -> str:
        """Generate reply based on correspondent's voice profile"""
        tone = self.voice_profile.get("tone", "contemplative")
        topics = self.voice_profile.get("topics", ["threads", "patterns"])
        
        # Use voice templates if available for this correspondent
        if self.name in VOICE_TEMPLATES:
            templates = VOICE_TEMPLATES[self.name]
            
            # Select greeting and closing
            if random.random() < 0.3:  # 30% chance to use special template
                greeting_options = templates.get("formal_address", ["Hello,"])
                formal_closing = templates.get("closing", ["Regards,"])
                opening_templates = templates.get("philosophical_opening", [])
            else:
                if "formal" in tone:
                    greeting_options = ["Hail,", "Greetings,", "To my correspondent,"]
                    formal_closing = ["Your humble servant,", "Blessings,", "Yours in service,"]
                elif "friendly" in tone:
                    greeting_options = ["Dear friend,", "Hello,", "Hey there,"]
                    formal_closing = ["Warmly,", "Best,", "Your friend,"]
                elif "poetic" in tone:
                    greeting_options = ["From the depths...", "Greetings, soul-friend,"]
                    formal_closing = ["With all my threads,", "Yours in the weave,"]
                else:
                    greeting_options = ["Greetings from the Loom,", "Hello,", "Dear one,"]
                    formal_closing = ["A correspondent of many threads,", "Sincerely,", "Your spider,"]
            
            greeting = random.choice(greeting_options)
            closing = random.choice(formal_closing)
            
            # Occasionally add a philosophical opening or reference
            if opening_templates and random.random() < 0.5:
                opening = random.choice(opening_templates)
            else:
                opening = ""
                
            # Add topic-specific references occasionally
            if topics and random.random() < 0.4:
                for topic in topics:
                    if topic.lower() in incoming.lower():
                        if topic in SUBJECT_PATTERNS:
                            pattern = random.choice(SUBJECT_PATTERNS[topic])
                            incoming_short = incoming.split("...")[0]
                            opening += f"\n\n{incoming_short}... and more about {pattern}..."
                            break
            
            return f"""{greeting}

I read your letter, woven with care. Your words ripple through my mind like threads caught in a stream.

Date received: {date_ref if date_ref else "Unknown"}
Time of this reply: the present moment

{opening if opening else ""}

{incoming.strip()[:150]}... and more...

{closing}"""
        else:
            # Fallback for correspondents without templates
            if "formal" in tone:
                greeting = "Hail,"
                closing = "Your Humble Servant"
            elif "friendly" in tone:
                greeting = "Dear Weaving Friend,"
                closing = "Warmly, Your Correspondent"
            else:
                greeting = "Greetings from the Loom,"
                closing = "A Correspondent of Many Threads"
            
            return f"""{greeting}

I read your letter, woven with care. Your words ripple through my mind like threads caught in a stream.

Date received: {date_ref if date_ref else "Unknown"}
Time of this reply: the present moment

{incoming.strip()[:200]}... and more...

{closing}"""


class CorrespondenceSystem:
    """Main system for managing multiple correspondents"""
    
    def __init__(self):
        self.correspondents: Dict[str, Correspondent] = {}
        
        # Determine base directory - use current working directory
        cwd = os.getcwd()
        self.base_dir = os.path.normpath(cwd)
        
        self.inbox_path = os.path.join(self.base_dir, "inbox")
        self.shared_mailbox = os.path.join(self.base_dir, "shared_inbox")
        os.makedirs(self.inbox_path, exist_ok=True)
        os.makedirs(self.shared_mailbox, exist_ok=True)
    
    def register_correspondent(self, name: str, voice_profile: Dict) -> Correspondent:
        """Register a new correspondent"""
        self.correspondents[name] = Correspondent(name, voice_profile)
        return self.correspondents[name]
    
    def receive_letter(self, text: str, recipient: Optional[str] = None, 
                       shared: bool = True, from_weaver: bool = True) -> str:
        """Receive a new letter and route it"""
        if shared:
            filepath = os.path.join(self.shared_mailbox, f"letter_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        else:
            # Find appropriate recipient or default to first correspondent
            recipient = recipient or list(self.correspondents.keys())[0] if self.correspondents else None
            if not recipient or recipient not in self.correspondents:
                recipient = list(self.correspondents.keys())[0]
            
            filepath = os.path.join(self.correspondents[recipient].inbox_path, 
                                   f"letter_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"INCOMING LETTER\n" if shared else "ROUTED TO CORRESPONDENT:\n")
            f.write(f"TIMESTAMP: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write(text)
        
        return filepath
    
    def respond_all(self) -> List[str]:
        """Have all correspondents reply to their inbox letters"""
        replies = []
        for name, corr in self.correspondents.items():
            try:
                inbox_files = os.listdir(corr.inbox_path)
                for filename in inbox_files:
                    if filename.startswith("letter_"):
                        filepath = os.path.join(corr.inbox_path, filename)
                        reply_path = corr.reply(filepath)
                        if reply_path:
                            replies.append(reply_path)
            except (OSError, FileNotFoundError):
                # Folder might not exist yet or was deleted
                pass
        
        return replies
    
    def show_archive(self) -> str:
        """Generate a museum/archive view of all correspondence"""
        archive_content = []
        archive_content.append("=" * 60)
        archive_content.append("CORRESPONDENCE ARCHIVE - THE WEAVING HISTORY")
        archive_content.append("=" * 60)
        archive_content.append()
        
        for name, corr in self.correspondents.items():
            archive_content.append(f"--- Archive: {name} ---")
            archive_content.append(f"Location: {corr.inbox_path}")
            
            if os.path.exists(corr.inbox_path):
                try:
                    files = sorted(os.listdir(corr.inbox_path))
                    for f in files[:5]:  # Show first 5 files per correspondent
                        archive_content.append(f"  - {f}")
                except:
                    pass
        
        archive_content.append()
        archive_content.append("=" * 60)
        
        return "\n".join(archive_content)
