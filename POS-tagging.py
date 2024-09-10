# prompt: generate a programm of part of speech tagging using python 

import nltk
nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize

def pos_tagging(text):
  """
  Performs Part-of-Speech tagging on the given text.

  Args:
    text: The input text.

  Returns:
    A list of tuples where each tuple contains a word and its POS tag.
  """
  tokens = word_tokenize(text)
  tags = nltk.pos_tag(tokens)
  return tags

# Example usage
text = "This is an example sentence for POS tagging."
tagged_text = pos_tagging(text)
print(tagged_text)
