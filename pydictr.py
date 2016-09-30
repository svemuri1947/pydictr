import json
from http.client import HTTPConnection
from urllib.request import Request, urlopen
from pprint import pprint
import sys

api_url = 'http://owlbot.info/api/v1/dictionary/'
api_suffix = '?format=json'

# lookup that word
def web_call( dictword ):
  dictword = dictword.rstrip()
  if check_alpha( dictword ):
    api_request_url = api_url + dictword + api_suffix
    req = Request(api_request_url, headers= {'User-Agent': 'Mozilla/5.0'} )
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
  print(json_parsed[word]['defenition'])
  print(json_parsed[word]['example'])
  print('')

json_parsed = json.loads(web_call(get_word()))
def_nums = len(json_parsed)

if len(json_parsed) > 0:
  for x in range(def_nums):
    output_def(x)
else:
  print("That's not an English word")
