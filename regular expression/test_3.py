
import re
from pprint import pprint

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''

print(re.findall(r'<[divp]{1,3}>.*?<\/[divp]{1,3}>', texto))
print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS \3 COISAS \4', texto))

print()

#grupo 
tags = (re.findall(r'(<([divp]{1,3})>(.*?)<\/\2>)', texto))

for tag in tags:
    um, dois, tres = tag
    print(tres)

print()

pprint(tags)


print()

cpf = '147.855.965-36'
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))