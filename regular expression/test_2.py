# | OU
# . Qualquer caracter no lugar do ponto
# [] Conjunto de caracteres 

# encontra sempre a esquerda da expression
# * 0 ou n
# + 1 ou n
# ? 0 ou n
# {n}
# {min, max}
#{10,} 10 ou mias
#{,10} de 0 a 10
#{5,10} de 5 a 10


import re


texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem"!
'''

print(re.findall(r'João|Maria', texto))
print(re.findall(r'João|Maria|ad....', texto))
print(re.findall(r'João|Maria|ad....', texto))
print(re.findall(r'[Jj]oão|[a-zA-Z0-9_]aria|ad....', texto))
print(re.findall(r'jOãO|mAriA', texto, flags=re.I))

print(re.findall(r'J[a-zA-Z]+ão', texto, flags=re.I))
print(re.findall(r'Jo+ão+', texto, flags=re.I))
print(re.findall(r'Jo{1,}ão{1,}', texto, flags=re.I))
print(re.sub(r'Jo+ão+', 'Felipe', texto, flags=re.I))

print(re.findall(r've{3}m{1,2}', texto, flags=re.I))

texto2 = " João ama ser amado"

print(re.findall(r'ama[do]*', texto2, flags=re.I))