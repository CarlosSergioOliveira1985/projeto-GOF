import re
from pprint import pprint

senha_forte_regexp = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[ -\/:-@[-`{-~]).{12,}$', flags=re.M)



texto = '''
VÁLIDAS
*8?s8=tM3iZS
qL}uO5~q6L`9
$f2g}08%LGLy
6es;cN7~V;5J
3ENlN?t]86n~

SEM MINÚSCULAS
_3L;8Z_V{37S
61O8|2}&Z}GA
39_X@GW_7O5;
1!~7MW~%U27Y
ZA9;975.|U=Q

SEM MINÚSCULAS E NÚMEROS
~|{KC}WH<K~W
U&C:{FD`>G-A
SGFXJ]X_`{@`
?~P`{BRZ[HD?
REV.K?K]A~\}

SEM NÚMEROS CARACTERES E MINÚSCULAS
HZVGFCFAQGCE
ZDTCRBUZYXXX
LOJZMCYUJAIM
OLQFFZITJFUX
MZXMKRKAPNBY

QUANTIDADE INVÁLIDA (6)
|z2k1K
6g9=Pl
8y~f4S
N9;rd2
w23qF^
'''

for senha in senha_forte_regexp.findall(texto):
    pprint(senha)
