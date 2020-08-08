'''Phrase Encryption Doc Version
Programmed by Dylan Walker 8/3/2020'''

import string
import secrets

Pass1 = open(r"Encryption test.txt", "r")

List1 = Pass1.read()
#List1 = List1.pop()
List1 = list(List1)

alphabet = string.ascii_letters + string.digits
Pass2 = ''.join(secrets.choice(alphabet) for i in range((len(List1))))

List2 = list(Pass2)
#print (Pass2)

"""for chars1 in range(0, len(List1)):
    List1split = list(List1[chars1])"""



#printS (List1)
#print (List2)  
    
Exor1_L = []

for x in range(0, len(List2)):
    List2[x] = ord(List2[x])

for y in range(0, len(List1)):
    List1[y] = ord(List1[y])    

#print (List1)

for i in range(0, len(List1)):
    Exor1 = List1[i] ^ List2[i]
    Exor2 = Exor1 ^ List2[i]
    Exor1_L.append(Exor2)
    Exor1_L[i] = chr(Exor1_L[i])


Exor1_L = "".join(Exor1_L)
print (Exor1_L)

Pass1.close()
