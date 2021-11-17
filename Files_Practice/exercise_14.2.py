# exercise A
counter=0
f=open('file1.txt', 'r')
for line in f:
    if line[0] not in 't':
        counter+=1
print(counter)
# exercise B
f=open('file1.txt', 'r')
counter=0
for line in f:
    words=line.split()
    for word in words:
        if word=='the':
            counter+=1
print(counter)
# exercise C
sum=0
f=open('file1.txt', 'r')
for line in f:
    words=line.split()
    sum+=len(words)
print(sum)
