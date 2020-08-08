Pass1 = "A fish hopped out of the water."
Pass2 = "jk@lmno p."
Pass3 = ""



List1split = [65, 76]
List2split = [46, 108]
Exor1_L = []

for i in range(0, len(List1split)):
    Exor1 = List1split[i] ^ List2split[i]
    print (Exor1)
    print (Exor1_L)
    Exor2 = Exor1 ^ List1split[i]
    print (Exor2)
    Exor1_L.append(Exor2)
    print (Exor1_L)
    Exor1_L[i] = chr(Exor1_L[i])
    print (Exor1_L)
print (Pass3)
    
