Pass1 = ord("a")
Pass2 = ord('l')
print (chr(Pass1))
print (chr(Pass2))
First_ExceptOr = Pass1 ^ Pass2
Second_Except = First_ExceptOr ^ Pass1
print (chr(Second_Except))

