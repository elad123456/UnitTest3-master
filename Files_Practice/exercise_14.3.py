# exercise A
f=open('file1.txt', 'r')
for line in f:
    words=line.strip()
    print(words)
# exercise B
f=open('file1.txt', 'r')
counter=0
for line in f:
    counter+=1
print(counter)
