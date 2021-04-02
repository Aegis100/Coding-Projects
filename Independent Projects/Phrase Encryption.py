'''Phrase Encryption
Programmed by Dylan Walker 8/3/2020'''

Pass1 = "A Lion swam."
Pass2 = ".l@"



List1 = Pass1.split(" ")
List2 = Pass2.split(" ")

print (Pass1_L)

for chars2 in range(0, len(List2)): 
    List2split = list(List2[chars2])
    for splitchars2 in range(0, len(List2split)):
        List2split[splitchars2] = ord(List2split[splitchars2])
        if str(List2split[len(List2split) - 1]) == False: 
            break

for chars1 in range(0, len(List1)):
    List1split = list(List1[chars1])
    print (List1split)
    for splitchars1 in range(0, len(List1split)):
        List1split[splitchars1] = ord(List1split[splitchars1])
        if str(List1split[len(List1split) - 1]) == False:
            Exor1(List1split)
  

    
Exor1_L = []
  
Exor2_L = []
  
Exor3_L = []


def Exor1(List1split):
    for i in range(0, len(List1split)):
        Exor1 = List1split[i] ^ List2split[i]
        Exor2 = Exor1 ^ List1split[i]
        Exor1_L.append(Exor2)
        Exor1_L[i] = chr(Exor1_L[i])

Exor1_L = "".join(Exor1_L)
print (Exor1_L)

for i in range(0, len(List2split)):
    Exor3 = Exor1 ^ List2split[i]
    Exor3_L.append(Exor3)
    Exor3_L[i] = chr(Exor3_L[i])

Exor3_L = "".join(Exor3_L)
print (Exor3_L)
