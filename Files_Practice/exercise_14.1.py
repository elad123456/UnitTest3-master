text1='a boy is playing there'
text2='there is a play ground'
text3='an airplane is in the sky'
text4='alphabets and numbers are allowed in the password'
l=text1+'\n'+text2+'\n'+text3+'\n'+'the sky is pink'+'\n'+text4
# f=open('file1.txt', 'w')
# f.writelines(l)
f=open('file1.txt', 'r')
print(f.read())

