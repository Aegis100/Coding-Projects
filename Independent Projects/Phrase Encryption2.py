'''Phrase Encryption2(One that actually works)
Programmed by Dylan Walker 8/3/2020'''

Pass1 = "A Lion swam."
Pass2 = "@@#ffffffffjeed"



List1 = list(Pass1)
List2 = list(Pass2)

print (Pass1)
#print (List2)  
    
Exor1_L = []
  
Exor2_L = []
  
Exor3_L = []

#for i in range(0, len(List1)):
for x in range(0, len(List2)):
    #try:
    List2[x] = ord(List2[x])
    #print (List2)
    '''except:
        List2[x] = chr(List2[x])'''
for y in range(0, len(List1)):
    #try:
    List1[y] = ord(List1[y])
    #print (List1)
    '''except:
        List1[y] = chr(List1[y])'''
    #if y == len(List1):
        #return List1()
print (List1)
print (List2)
for i in range(0, len(List1)):
    Exor1 = List1[i] ^ List2[i]
    Exor2 = Exor1 ^ List2[i]
    Exor1_L.append(Exor2)
    Exor1_L[i] = chr(Exor1_L[i])

print (Exor1)
Exor1_L = "".join(Exor1_L)
print (Exor1_L)

'''for i in range(0, len(List2)):
    Exor3 = Exor1 ^ List2[i]
    Exor3_L.append(Exor3)
    Exor3_L[i] = chr(Exor3_L[i])'''

#Exor3_L = "".join(Exor3_L)
#print (Exor3_L)
