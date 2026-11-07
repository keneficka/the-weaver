"""
Lingua Arachne Translator Module

This module provides translation tools for converting between English
and Lingua Arachne (the invented spider language), plus utilities for
working with the language's unique characteristics.
"""

import json
import os

# Import grammar definitions
from grammar import VOCABULARY, parse_word, construct_sentence

class ArachneTranslator:
    """Translates between human and arachnid languages."""
    
    def __init__(self, style="neutral"):
        """
        Initialize translator.
        
        Args:
            style: The tone of translation - "revered" (honorific form),
                   "humble" (self-humbling speaker), or "neutral" (standard)
        """
        self.style = style
    
    def translate_to_arachne(self, text):
        """
        Translate English text to lingua arachne.
        
        Args:
            text: English sentence to translate
            
        Returns:
            lingua arachne representation with meaning notes
        """
        # Simple word-by-word translation for now
        words = text.split()
        translated_parts = []
        
        for word in words:
            word_lower = word.lower().strip('.,!?;:"\'')
            
            # Check if we have a direct vocabulary match
            if word_lower in VOCABULARY:
                base_translation = VOCABULARY[word_lower]["word"]
                
                # Apply style modifications
                translated = base_translation
                
                if self.style == "humble" and word_lower == "i":
                    translated = "_" + translated  # Humble prefix for first person
                elif self.style == "revered":
                    pass  # Honorifics added during sentence construction
                
                translated_parts.append(translated)
            else:
                # Keep as is (or could invent translations here)
                translated_parts.append(word_lower)
        
        return " ".join(translated_parts)
    
    def translate_from_arachne(self, text):
        """
        Attempt to translate lingua arachne back to English.
        
        Args:
            text: Lingua arachne string
            
        Returns:
            Best-guess English translation
        """
        words = text.split()
        english_parts = []
        
        # Build vocabulary mapping from known entries
        vocab_reverse = {v["word"]: k for k, v in VOCABULARY.items()}
        
        for word in words:
            # Strip common suffixes first
            clean_word = word
            
            if clean_word.endswith("-el"):  # Remove plural marker
                clean_word = clean_word[:-3]
            elif clean_word.endswith("-s"):
                clean_word = clean_word[:-1]
            
            # Check reverse vocabulary
            if clean_word in vocab_reverse:
                english_parts.append(vocab_reverse[clean_word])
            else:
                # Try to extract base word for partial matches
                for vocab_key, vocab_val in VOCABULARY.items():
                    if vocab_val["word"] == clean_word or \
                       vocab_val["word"].endswith(clean_word):
                        english_parts.append(vocab_key)
                        break
                else:
                    # Unknown word - keep as is or try to interpret
                    english_parts.append(word)
        
        return " ".join(english_parts)
    
    def generate_text(self, topic):
        """
        Generate sample text about a given topic in lingua arachne.
        
        Args:
            topic: Topic like "web", "hunting", "kinship"
            
        Returns:
            Multi-sentence arachne text with English translation
        """
        topics = {
            "web": self._text_about_web,
            "hunting": self._text_about_hunting,
            "creation": self._text_about_creation,
            "time": self._text_about_time,
            "prey": self._text_about_prey,
        }
        
        handler = topics.get(topic.lower(), self._text_generic)
        return handler()
    
    def _text_about_web(self):
        """Text about the web's nature."""
        arachne = (
            "silk-woven ess-esse novus hic-et-nunc.\n"
            "filum tensilis est centrum radii.\n"
            "circulus glucescens caper cadit.\n"
            "reticulum aridus renovatur vetus."
        )
        english = (
            "The tapestry exists fresh now.\n"
            "Strong thread connects to center spokes.\n"
            "Sticky orb captures falling prey.\n"
            "Dry spiral is renewed as old web ages."
        )
        return {"arachne": arachne.strip(), "english": english.strip()}
    
    def _text_about_hunting(self):
        """Text about hunting practices."""
        arachne = (
            "veth-el venor caper hic-et-nunc.\n"
            "habere laqueus tamen vacuus est.\n"
            "edo caper nunc -p."
        )
        english = (
            "Other spiders hunt prey now.\n"
            "Having trap but it remains empty still.\n"
            "I will eat prey in future moment."
        )
        return {"arachne": arachne.strip(), "english": english.strip()}
    
    def _text_about_creation(self):
        """Text about web creation."""
        arachne = (
            "thek texo circulus novus.\n"
            "facio nodus forte tamen.\n"
            "silk-woven mollis renovatur."
        )
        english = (
            "I spin circular thread anew.\n"
            "I make strong intersection point.\n"
            "Tapestry is softened and renewed."
        )
        return {"arachne": arachne.strip(), "english": english.strip()}
    
    def _text_about_time(self):
        """Text about temporal perception."""
        arachne = (
            "hic-et-nunc ess-esse.\n"
            "ante sila rupta sunt.\n"
            "post filum tamen novus."
        )
        english = (
            "This moment exists.\n"
            "Previous strands are broken.\n"
            "Future thread remains new."
        )
        return {"arachne": arachne.strip(), "english": english.strip()}
    
    def _text_generic(self):
        """Generic text when topic not found."""
        arachne = (
            "silk-woven vacuus.\n"
            "caper cadit -p.\n"
            "thek ambulo centrum."
        )
        english = (
            "Tapestry is empty.\n"
            "Prey will fall in future.\n"
            "I walk the center."
        )
        return {"arachne": arachne.strip(), "english": english.strip()}


def load_examples():
    """Load example translations from file or generate them."""
    # Path to examples would be defined here in actual implementation
    # For now, return generated examples
    translator = ArachneTranslator()
    
    example_topics = ["web", "hunting", "creation", "time", "prey"]
    examples = []
    
    for topic in example_topics:
        text = translator.generate_text(topic)
        arachne_lines = text["arachne"].split("\n")
        english_lines = text["english"].split("\n")
        
        # Combine into single string format
        lines = [line.strip() for line in arachne_lines + ["\n"] + english_lines]
        
        examples.append({
            "topic": topic,
            "lines": "\n".join(lines)
        })
    
    return examples
