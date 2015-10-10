from lxml import html
import requests
import math

def prod(l):
	a = 1
	for term in l:
		a *= int(term)
	return a

page = requests.post('https://projecteuler.net/problem=8',verify=False)
data = html.document_fromstring(page.text)
num = data.xpath('//p[@style="font-family:courier new;text-align:center;"]/text()')
num = ''.join(num).replace('\r','').replace('\n','')
res = []
for i,n in enumerate(num):
	if i+13 < len(num):
		r = num[i:i+13]
		res.append(prod(r))
	else:
		break
print max(res)