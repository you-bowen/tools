import sys

if len(sys.argv)!=2:
    print('usage: clean xxx.cpp')
    exit()
with open(sys.argv[1],'r+') as f:
    content = f.read()
res = ''
for id,i in enumerate(content):
    if ord(i) in list(range(32,128))+[10] :
        res+=content[id]
    else:
        res+=' '
with open(sys.argv[1],'w') as f:
    f.write(res)
print("okey!")