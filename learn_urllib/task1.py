import sys
from urllib import request, parse


my_url = 'http://www.google.com/search?'
value = {'q': 'wikipedia'}

myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'

try:
    mydata = parse.urlencode(value)
    my_url += mydata
    req = request.Request(my_url, headers=myheader)
    answer = request.urlopen(req)
    answer = answer.readlines()
    for line in answer:
        print(line)
except Exception:
    print('Error(')
    print(sys.exc_info()[1])