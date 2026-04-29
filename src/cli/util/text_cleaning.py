import re
import unicodedata

def text_cleaning(text):
    if not text: return ""
    
    text = text.lower()

    text = unicodedata.normalize('NFD', text)
    text = "".join(c for c in text if unicodedata.category(c) != 'Mn')
    


    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = " ".join(text.split())
    
    return text
