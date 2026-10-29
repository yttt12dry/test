m=input("entre la chaine de caractere : ")
inverse=""
for c in m:
    inverse=c+inverse
if inverse==m:
    print("la chaine est un palindrome")
else:
    print("la chaine n'est pas un palindrome")