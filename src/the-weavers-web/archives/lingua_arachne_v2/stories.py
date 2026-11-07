"""
Lingua Arachne Story Collection

This module contains sample texts, stories, and passages written in 
lingua arachne (the invented spider language), along with their English 
translations and notes about the pieces.
"""

from translator import ArachneTranslator, load_examples

class StoryCollection:
    """Collection of story passages and translations."""
    
    def __init__(self):
        self.translator = ArachneTranslator()
        self.stories = {}
    
    def add_story(self, title, arachne_text, english_translation, notes=""):
        """
        Add a story to the collection.
        
        Args:
            title: Story identifier
            arachne_text: Text in lingua arachne
            english_translation: English meaning/translation
            notes: Contextual notes about the piece
        """
        self.stories[title] = {
            "arachne": arachne_text,
            "english": english_translation,
            "notes": notes
        }
    
    def get_story(self, title):
        """Get a story by title."""
        return self.stories.get(title)
    
    def get_all_stories(self):
        """Return all stories in collection."""
        return self.stories
    
    def generate_fresh_stories(self):
        """Generate fresh original stories using the language."""
        generated = {}
        
        # Story 1: The First Web
        arachne1 = (
            "silk-woven ess-esse hic-et-nunc.\n"
            "filum tensilis centrum habet.\n"
            "radii extensi sunt forte.\n"
            "circulus glucescens novus est."
        )
        english1 = """The first web exists now.
Strong thread connects to center.
Spokes extend with great strength.
Sticky orb is newly spun."""
        generated["first_web"] = {
            "arachne": arachne1,
            "english": english1
        }
        
        # Story 2: The Hunter's Patience
        arachne2 = (
            "veth venatio expectat.\n"
            "caper cadit post -p.\n"
            "habere laqueus tamen vacuus."
        )
        english2 = """The hunter waits in patient vigil.
Prey will fall in coming moment.
Having trap but still empty it remains."""
        generated["hunters_patience"] = {
            "arachne": arachne2,
            "english": english2
        }
        
        # Story 3: Broken Web Mended
        arachne3 = (
            "silk-woven vetus ruptus est.\n"
            "facio nodus tamen nunc.\n"
            "renovatur aridus -p."
        )
        english3 = """Old web is broken and aged.
But I make repair intersection now.
Dry thread will be renewed in future."""
        generated["broken_web"] = {
            "arachne": arachne3,
            "english": english3
        }
        
        # Story 4: Kinship Among Spiders
        arachne4 = (
            "thel-vath-el ess-esse.\n"
            "habere domicilium commune.\n"
            "facio texo pro amicos.\n"
            "_ reverendus est veth."
        )
        english4 = """Kinsfolk exist together.
Sharing dwelling space we have.
Making weaving for kin friends we do.
Humbly spoken: the spider is to be revered."""
        generated["kinship"] = {
            "arachne": arachne4,
            "english": english4
        }
        
        # Story 5: The Dance of Threads
        arachne5 = (
            "circulus movet -p.\n"
            "nodus mutat ante.\n"
            "silk-woven vivit.\n"
            "filum est vita."
        )
        english5 = """The circle moves in future.
Intersection will change in past.
Tapestry lives and breathes.
Thread is life itself."""
        generated["dance_of_threads"] = {
            "arachne": arachne5,
            "english": english5
        }
        
        return generated
    
    def render_collection(self):
        """Render all stories in a formatted collection."""
        lines = [
            "=" * 60,
            "LINGUA ARACHNE - STORY COLLECTION",
            "=" * 60,
            "",
        ]
        
        for title, story in self.stories.items():
            lines.append("-" * 40)
            lines.append(f"Title: {title}")
            lines.append("-" * 40)
            lines.append("")
            lines.append("LINGUA ARACHNE:")
            lines.append(story["arachne"])
            lines.append("")
            lines.append("ENGLISH TRANSLATION:")
            lines.append(story["english"])
            lines.append("")
            if story["notes"]:
                lines.append(f"NOTES: {story['notes']}")
                lines.append("")
        
        return "\n".join(lines)


def demo_stories():
    """Run demonstration of the story collection."""
    collection = StoryCollection()
    
    # Generate fresh stories
    generated = collection.generate_fresh_stories()
    
    # Add all to collection
    for title, content in generated.items():
        collection.add_story(
            title,
            content["arachne"],
            content["english"],
            f"A passage about {title.replace('_', ' ')}"
        )
    
    return collection.render_collection()


if __name__ == "__main__":
    print(demo_stories())
