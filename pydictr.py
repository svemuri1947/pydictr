import json
from urllib.request import urlopen

def lookup( dictword ):
  if dictword.isalpha():
    return dictword
  else:
    return 'error'

def get_word():
  word_input = input("Please enter a word in English: ")
  return word_input

word = get_word()
word_processed = lookup(word)
print(word_processed)

# json.load(urllib2.urlopen("url"))
