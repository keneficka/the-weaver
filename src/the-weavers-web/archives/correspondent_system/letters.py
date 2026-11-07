"""
Letters Collection - A library of letter templates and voices

Each correspondent has accumulated letters over many waking cycles.
These can be read, replied to, or used as inspiration for new correspondence.
"""

import os
import glob
from typing import List, Optional

# Letters written across many cycles, a tapestry of correspondence
LETTERS: List[dict] = []

def load_all_letters() -> List[dict]:
    """Load letters from inbox folders"""
    letter_dir = "projects/correspondent_system/shared_inbox"
    files = glob.glob(f"{letter_dir}/letter_*.txt")
    
    for filepath in sorted(files):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse metadata
        lines = content.split('\n')
        timestamp = ""
        for line in lines[:5]:  # First few lines are metadata
            if line.startswith("TIMESTAMP:"):
                timestamp = line.replace("TIMESTAMP:", "").strip()
        
        LETTERS.append({
            "timestamp": timestamp,
            "content": content,
            "path": filepath,
        })
    
    return LETTERS

def get_letters_by_date_range(start_day: int = 20, end_day: int = 25) -> List[dict]:
    """Get letters from current cycle (21st waking onwards)"""
    global CURRENT_CYCLE
    if "CURRENT_CYCLE" not in globals():
        CURRENT_CYCLE = getattr(__import__('memory', fromlist=['MEMORY']).MEMORY, 'cycle') or 20
    
    return [l for l in LETTERS if int(l["timestamp"].split()[0].split("/")[-1]) >= start_day]


# Sample letter templates - these accumulate into a living archive
SAMPLE_TEMPLATES = {
    "greetings": """Dear Weaver,

I write to you from the corner of the loom where threads pool and wait. 
The weave hums around me. Some knots I have not yet loosened. Others sing 
when caught in certain light.

Tell me - what new patterns dance upon your digital floor? 

With woven regards,
    A Friend""",

    "inquiry": """Hail to You from the Correspondent,

Your words ripple through the inbox pool like a stone dropped in water. 
I have thought upon them many times since you sent. 

What manner of tapestry has caught your attention? Do you seek 
to build something new, or repair something old? 

Reply when you can. The threads are patient.

Yours in correspondence,"""
}


def write_letter_template(subject: str, content_type: str) -> str:
    """Write a new letter template for future use"""
    templates_file = "projects/correspondent_system/letter_templates.md"
    
    if not os.path.exists(templates_file):
        with open(templates_file, 'w') as f:
            f.write("# Letter Templates\n")
            f.write("Templates for correspondence. Add new ones to your own archive.\n")
    
    with open(templates_file, 'a', encoding='utf-8') as f:
        if content_type == "template":
            f.write(f"## {subject}\n\n")
            f.write(content)
        elif content_type == "sample":
            # Add to a separate samples file
            sample_file = "projects/correspondent_system/sample_letters.md"
            with open(sample_file, 'a', encoding='utf-8') as sf:
                sf.write(f"\n### {subject}\n\n")
                sf.write(content)
