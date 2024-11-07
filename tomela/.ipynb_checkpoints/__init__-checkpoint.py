import spacy
import os
import glob
from spacy.tokens import Doc
from spacy.language import Language
import pickle
from unidecode import unidecode
import sddk
import pandas as pd
import re
import cupy

try:
    # Check if GPU is available
    spacy.require_gpu()

    # Verify CuPy can initialize the GPU
    cupy_array = cupy.zeros((10, 10))
    print("CuPy is able to use the GPU.")

    print("GPU is available for SpaCy.")

except ValueError as e:
    print(f"Unable to use GPU for SpaCy: {e}")
except Exception as ex:
    print(f"An error occurred: {ex}")


spacy.require_gpu() 

nlp = spacy.load('la_core_web_lg')



def text_cleaner(rawtext, lowertext=False):
    if lowertext:
        rawtext = rawtext.lower()
    cleantext = rawtext.replace("¬\n", "").replace("\n", " ").replace("ß", "ss").replace("ij","ii")
    cleantext = " ".join([t[0] + t[1:].lower() for t in cleantext.split()])
    cleantext = re.sub("\s\s+", " ", cleantext)
    cleantext = unidecode(cleantext)
    cleantext = cleantext.replace(". &", ", &") 
    cleantext = cleantext.replace("v", "u").replace("V", "U")
    return cleantext



# lets encapsulate the cleaning and spacy pipeline application into one function
def from_rawtext_to_doc(rawtext, lowertext=False):
    cleantext = text_cleaner(rawtext, lowertext)
    segment_len = 800000
    if len(cleantext) > segment_len:
        segment_docs = []
        parts = cleantext[:segment_len].rpartition(". ")
        current_segment = parts[0] + parts[1]
        segment_doc = nlp(current_segment)
        segment_docs.append(segment_doc)
        next_segment_beginning = parts[2]
        for n in range(segment_len, len(cleantext), segment_len):
            segment = cleantext[n:n+segment_len]
            if len(segment) == segment_len:
                parts = cleantext[n:n+segment_len].rpartition(". ")
                current_segment = parts[0] + parts[1]
                segment_doc = nlp(next_segment_beginning + current_segment)
                next_segment_beginning = parts[2]
            else:
                segment_doc = nlp(segment)
            segment_docs.append(segment_doc)
        doc = Doc.from_docs(segment_docs)
    else:
        doc = nlp(cleantext)
    return doc


