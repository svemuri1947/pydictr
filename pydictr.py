import json
import sys
from http.client import HTTPConnection
from urllib.request import Request, urlopen
from pprint import pprint

api_url = 'https://owlbot.info/api/v2/dictionary/owl'
api_suffix = '?format=json'

try:
  print (sys.argv[1])
except IndexError:
  prompt_for_input = True
else:
  prompt_for_input = False
  word_input = sys.argv[1]

# lookup that word
def web_call( dictword ):
  dictword = dictword.rstrip()
  if check_alpha( dictword ):
    api_request_url = api_url + dictword + api_suffix
    req = Request(api_request_url, headers = {'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    return webpage
  else:
    print('Naw, use an ENGLISH word')
    sys.exit()

# check that it's all alpha
def check_alpha( dictword ):
  if dictword.isalpha():
    return True
  else:
    return False

# Get user input for word
def get_word():
  word_input = input("Please enter a word in English: ")
  print('')
  return word_input

# This prints the output
def output_def(word):
  print(word+1)
  print(json_parsed[word]['type'])
  print(json_parsed[word]['definition'])
  print(json_parsed[word]['example'])
  print('')

if 'word_input' in vars():
  json_parsed = json.loads(web_call(word_input))
else:
  json_parsed = json.loads(web_call(get_word()))

if len(json_parsed) > 0:
  for x in range(len(json_parsed)):
    output_def(x)
else:
  print("That's not an English word")
