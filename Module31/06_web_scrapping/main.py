import requests
from bs4 import BeautifulSoup

def gen(lst):
    for i in lst:
        yield i

web = requests.get('http://www.columbia.edu/~fdc/sample.html')

page_content = BeautifulSoup(web.content, "html.parser")
prices = page_content.find_all('h3')
my_list = []
for i in gen(prices):
    my_list.append(i.text)

print(my_list)