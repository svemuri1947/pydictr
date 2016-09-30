import json
from http.client import HTTPConnection
from urllib.request import Request, urlopen
from pprint import pprint

api_url = 'http://owlbot.info/api/v1/dictionary/'
api_suffix = '?format=json'

# lookup that word
def web_call( dictword ):
  dictword = dictword.rstrip()
  if check_alpha( dictword ):
    api_request_url = api_url + dictword + api_suffix
    req = Request(api_request_url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    return webpage
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
json_string = web_call(word)
json_parsed = json.loads(json_string)
print(json_parsed[0]['defenition'])

# json.load(urllib2.urlopen("url"))
