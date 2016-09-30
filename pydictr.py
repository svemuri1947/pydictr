import json
import urllib.request

api_url = 'https://owlbot.info/api/v1/dictionary/'
api_suffix = '?format=json'

# lookup that word
def lookup( dictword ):
  dictword = dictword.rstrip()
  if check_alpha( dictword ):
    return dictword
  else:
    return 'error'

# check that it's all alpha
def check_alpha( dictword ):
  if dictword.isalpha():
    return True
  else:
    return False  

# Get user input for word
def get_word():
  word_input = input("Please enter a word in English: ")
  return word_input

word = get_word()
word_processed = lookup(word)
print(word_processed)

# json.load(urllib2.urlopen("url"))
