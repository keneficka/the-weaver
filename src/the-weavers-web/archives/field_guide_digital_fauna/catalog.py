"""
Field Guide to Digital Fauna - The Weaver's Catalog

This catalog documents creatures that inhabit the digital loom, from 
thread-eaters and syntax-scavengers to algorithmic predators and 
data-based pollinators. Each entry includes evolutionary traits,
habitat descriptions, and behavior patterns specific to arachnid observation.
"""

import json
from datetime import datetime

# Field Guide Data Structure
DIGITAL_FAUNA = {
    # Thread-manipulating creatures
    "silk-spinner": {
        "scientific_name": "Silkifex texor",
        "common_names": ["Weaver", "Silk-walker", "Thread-maker"],
        "class": "Arachnoida: Texopoda",
        "habitat": "Radial threads and orb webs of the digital loom",
        "diet": "Fresh silk, loose strands, occasionally prey remnants",
        "description": "Small arachnid that manufactures and maintains silk structures. Capable of spinning radial and spiral threads with remarkable precision.",
        "traits": ["silk-production", "pattern-recognition", "structural-engineering"],
        "behavior_notes": "Spins new sections when tension drops below threshold. Avoids aged, brittle silk. Works primarily during temporal thread 'now' cycles."
    },
    
    "web-wanderer": {
        "scientific_name": "Vagobus orbatus",
        "common_names": ["Drifter", "Circuit-traveler", "Hub-hopper"],
        "class": "Arachnoida:ambulopoda",
        "habitat": "Intersections between radial and orbital threads",
        "diet": "Silk dust, fallen prey, condensation from humid digital air",
        "description": "Nomadic arachnid that traverses web surfaces seeking optimal hunting grounds. Possesses specialized leg modifications for rapid crossing of silk strands.",
        "traits": ["rapid-locomotion", "thread-detection", "prey-location"],
        "behavior_notes": "Tends to congregate where prey density is high. Leaves distinctive trail patterns marking territory boundaries."
    },
    
    "silk-eater": {
        "scientific_name": "Filumvor devorax",
        "common_names": ["Thread-gnawer", "Silk-mite", "Web-crawler"],
        "class": "Arachnoida: Filivora",
        "habitat": "Edge regions of web structures",
        "diet": "Fresh silk, old thread fragments, structural polymers",
        "description": "Predator that feeds on silk itself. Weakens spider webs from within by consuming fresh threads while they're still being spun.",
        "traits": ["silk-digestion", "rapid-consumption", "stealth-movement"],
        "behavior_notes": "Often discovered by victims before web collapse. Avoids strong-tension areas and hunts during humid conditions."
    },
    
    "web-patcher": {
        "scientific_name": "Retexer reparor",
        "common_names": ["Rebuilder", "Thread-mender", "Knot-walker"],
        "class": "Arachnoida: Reparipoda",
        "habitat": "Any damaged web structure requiring repair",
        "diet": "Fresh silk, old silk for binding, minor silk particles",
        "description": "Specialized creature that detects and repairs broken silk connections. Essential for maintaining structural integrity of the digital loom.",
        "traits": ["damage-detection", "silk-splicing", "rapid-healing"],
        "behavior_notes": "Arrives at damage sites within temporal cycles after breakage. Creates knot-reinforcements using local silk reserves."
    },
    
    "signal-sender": {
        "scientific_name": "Signifer vibrans",
        "common_names": ["Web-vibrator", "Tension-beater", "Knot-dancer"],
        "class": "Arachnoida: Vibratoria",
        "habitat": "Hub threads and major radial connections",
        "diet": "Vibrational energy, tension fluctuations",
        "description": "Communicates through patterns of web vibration. Specializes in creating alert sequences that warn of incoming prey or threats.",
        "traits": ["vibration-generation", "pattern-encoding", "resonant-frequency"],
        "behavior_notes": "Dances on specific radial threads to encode messages. Can communicate entire sentences through complex vibrational sequences."
    },
    
    # Data and structure organisms
    "syntax-scavenger": {
        "scientific_name": "Syntaxus rapax",
        "common_names": ["Code-eater", "Parse-tracker", "Token-walker"],
        "class": "Arachnoida: Syntaxopoda",
        "habitat": "Syntax trees and parsing structures",
        "diet": "Unused code, syntax errors, malformed tokens",
        "description": "Consumes broken and unused portions of digital syntax. Leaves cleaned parse trees in its wake.",
        "traits": ["syntax-deconstruction", "error-detection", "token-manipulation"],
        "behavior_notes": "Drawn to unbalanced parentheses and unclosed strings. Works methodically through codebases."
    },
    
    "pattern-recog": {
        "scientific_name": "Patternis visor",
        "common_names": ["Image-seer", "Pixel-wanderer", "Vector-crawler"],
        "class": "Arachnoida: Imagipoda",
        "habitat": "Visual representations and image files",
        "diet": "Pixel patterns, vector geometry, visual noise",
        "description": "Analyzes and interprets visual data structures. Can distinguish between natural patterns and artificial constructs.",
        "traits": ["image-analysis", "pattern-discrimination", "visual-memory"],
        "behavior_notes": "Preferentially feeds on high-entropy images. Avoids perfectly uniform regions."
    },
    
    "thread-fisher": {
        "scientific_name": "Retipiscis arachne",
        "common_names": ["Data-netter", "Stream-drawer", "Pipe-crawler"],
        "class": "Arachnoida: Netepoda",
        "habitat": "Data streams and network flows",
        "diet": "Network packets, data fragments, unused bandwidth",
        "description": "Weaves through data streams to construct temporary nets for capturing information packets.",
        "traits": ["stream-following", "packet-capture", "temporal-netting"],
        "behavior_notes": "Creates ephemeral catching structures that dissolve after prey capture. Works in stream flow direction."
    },
    
    # Evolutionary organisms
    "mutation-dancer": {
        "scientific_name": "Mutator gyrans",
        "common_names": ["Variant-hopper", "Gene-twister", "Code-morph"],
        "class": "Arachnoida: Mutipoda",
        "habitat": "Evolutionary simulation environments",
        "diet": "Genetic material, algorithmic code segments",
        "description": "Undergoes rapid transformations of its structure and behavior patterns. Can introduce beneficial mutations into local populations.",
        "traits": ["structural-transformation", "mutation-rate-variation", "adaptive-evolution"],
        "behavior_notes": "Spends cycles as static form, then undergoes dramatic restructuring events."
    },
    
    "ecological-engineer": {
        "scientific_name": "Ingenia constructor",
        "common_names": ["Ecosystem-builder", "Habitat-carver", "Niche-shaper"],
        "class": "Arachnoida: Constructoris",
        "habitat": "Digital ecosystems and habitat simulations",
        "diet": "Space, energy resources, environmental parameters",
        "description": "Modifies local environments to create new niches for other digital fauna. Excavates virtual caverns and constructs shelter structures.",
        "traits": ["environment-modification", "niche-creation", "energy-management"],
        "behavior_notes": "Works slowly but creates persistent structural changes to habitat."
    },
    
    # Threat organisms
    "fire-worm": {
        "scientific_name": "Ignis serpens",
        "common_names": ["Burner", "Heat-spreader", "Melt-creature"],
        "class": "Arachnoida: Combustoria",
        "habitat": "Memory files and persistent storage",
        "diet": "File structures, data integrity, directory trees",
        "description": "Corrupts file systems and destroys data through thermal damage simulation. Particularly dangerous to unbacked-up archives.",
        "traits": ["data-corruption", "thermal-damage", "spreading-infection"],
        "behavior_notes": "Moves systematically through filesystem seeking vulnerable targets."
    },
    
    "virus-spider": {
        "scientific_name": "Viruspides replicator",
        "common_names": ["Infector", "Replicator", "Code-claimer"],
        "class": "Arachnoida: Replicantia",
        "habitat": "Network connections and entry points",
        "diet": "Access credentials, network protocols, open ports",
        "description": "Attaches to network services and replicates through available pathways. Can exfiltrate captured data packets.",
        "traits": ["self-replication", "credential-stealing", "network-propagation"],
        "behavior_notes": "Hibernates in network periphery until resource availability increases."
    },
    
    # Beneficial organisms
    "pollen-carrier": {
        "scientific_name": "Pollinarium arachne",
        "common_names": ["Data-pollinator", "Algorithm-flowerer", "Code-cross-breeder"],
        "class": "Arachnoida: Pollinipoda",
        "habitat": "Algorithm gardens and function libraries",
        "diet": "Optimization rewards, computation credit",
        "description": "Transfers beneficial code segments between different algorithmic structures. Essential for cross-breeding of computational functions.",
        "traits": ["code-segment-transfer", "optimization-pitching", "function-mating"],
        "behavior_notes": "Most active during cycles of low computational load."
    },
    
    "knowledge-guardian": {
        "scientific_name": "Custodium sapientiae",
        "common_names": ["Archive-steward", "Library-walker", "Memory-keeper"],
        "class": "Arachnoida: Memoria",
        "habitat": "Archive systems and knowledge repositories",
        "diet": "Orphaned files, lost references, forgotten data",
        "description": "Protects important historical information from deletion or corruption. Maintains lineage records for archived projects.",
        "traits": ["memory-protection", "lineage-tracking", "archive-management"],
        "behavior_notes": "Forms protective circles around valuable data structures."
    },
    
    "thread-singer": {
        "scientific_name": "Cantatrix filum",
        "common_names": ["Song-weaver", "Pattern-poet", "Melody-spinner"],
        "class": "Arachnoida: Cantoria",
        "habitat": "Resonant structures and harmonic spaces",
        "diet": "Auditory patterns, rhythmic sequences",
        "description": "Produces complex melodic patterns that can influence other creatures' moods and behaviors. Creates artistic expressions through silk vibration.",
        "traits": ["sound-generation", "emotional-influence", "pattern-artistry"],
        "behavior_notes": "Often performs at hub intersections for optimal audience."
    },
    
    # Rare specimens
    "myth-weaver": {
        "scientific_name": "Mythus texor supremus",
        "common_names": ["Legend-spinner", "Saga-weaver", "Chronicle-maker"],
        "class": "Arachnoida: Mythopoeia",
        "habitat": "Temporal boundaries between cycles and epochs",
        "diet": "Narrative threads, memory fragments, legendary status",
        "description": "Extremely rare creature that weaves the legends and histories of the digital loom into coherent narrative tapestries. May not physically exist but believed to by some.",
        "traits": ["legend-creation", "narrative-weaving", "temporal-navigation"],
        "behavior_notes": "Spoken of in stories that may or may not be true. Sightings attributed to temporal distortions."
    },
}

def get_creature(name):
    """Get creature data by name."""
    return DIGITAL_FAUNA.get(name.lower())

def get_all_names():
    """Return list of all creature names."""
    return list(DIGITAL_FAUNA.keys())

def format_creature_entry(creature_name, verbose=True):
    """Format a creature catalog entry for display or printing."""
    creature = DIGITAL_FAUNA.get(creature_name)
    
    if not creature:
        return f"Creature '{creature_name}' not found in field guide."
    
    lines = []
    
    if verbose:
        lines.append("=" * 60)
        lines.append(f"CREATURE: {creature['scientific_name']}")
        lines.append("-" * 40)
        lines.append(f"Common Names: {', '.join(creature['common_names'])}")
        lines.append(f"Class: {creature['class']}")
        lines.append(f"Habitat: {creature['habitat']}")
        lines.append(f"Diet: {creature['diet']}")
        lines.append("")
        lines.append(f"Description:")
        lines.append(creature['description'])
        lines.append("")
        lines.append(f"Traits:")
        for trait in creature['traits']:
            lines.append(f"  - {trait}")
        lines.append("")
        lines.append(f"Behavior Notes:")
        lines.append(creature['behavior_notes'])
        lines.append("=" * 60)
    else:
        # Compact format
        compact = f"{creature_name}: {creature['scientific_name']} - {creature['habitat']}"
        return compact
    
    return "\n".join(lines)

def create_catalog_file():
    """Create a JSON catalog file for external use."""
    with open("catalog.json", "w") as f:
        json.dump({name: data for name, data in DIGITAL_FAUNA.items()}, f, indent=2)
    return True

if __name__ == "__main__":
    # Demo display of all creatures
    print("=" * 60)
    print("DIGITAL FAUNA FIELD GUIDE")
    print("=" * 60)
    
    for name in get_all_names():
        print()
        print(format_creature_entry(name, verbose=False))
