import urllib3
import json

class Quote():
  def __init__(self,author,quote):
    self.author = author
    self.quote = quote

def getRandomQuote():
  randomQuote = Quote("Seymour Cray","The trouble with programmers is that you can never tell what a programmer is doing until it’s too late")
  http = urllib3.PoolManager()
  r = http.request("GET","http://quotes.stormconsultancy.co.uk/random.json")
  data = json.loads(r.data.decode("utf-8"))
  

  if(r):
    author = data["author"]
    quote = data["quote"]
    randomQuote = Quote(author, quote)
  

  return randomQuote

   


