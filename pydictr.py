import json
from urllib.request import urlopen

def lookup( dictword ):
  dictword = dictword.rstrip()
  if check_alpha( dictword ):
    print('it is all alpha')

def check_alpha( dictword ):
  if dictword.isalpha():
    return True
  else:
    return False  

def get_word():
  word_input = input("Please enter a word in English: ")
  return word_input

word = get_word()
word_processed = lookup(word)
print(word_processed)

# json.load(urllib2.urlopen("url"))
