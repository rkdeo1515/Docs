# find.py - find unique items in pkg list

def makeList(f):
    list = []
    while True:
        line = f.readline()
        if not line: break
        list.append(line[:-1])
    f.close()
    return list

def compList(src, des):
    list = []
    tmp = 0
    for i in src :
        tmp = 0
        for j in des :
            if i == j :
                tmp+=1
        if tmp == 0 :
            list.append(i)
    return list

def overList(src, des):
    list = []
    tmp = 0
    for i in src :
        tmp = 0
        for j in des :
            if i == j :
                tmp+=1
        if tmp != 0 :
            list.append(i)
    return list

def writeFile(list, file):
    for i in list:
        file.write(i+"\n")

f1 = open("src", 'r')
f2 = open("des", 'r')
f3 = open("new", 'w')
src = makeList(f1)
des = makeList(f2)
tmp = compList(src, des)
#tmp = overList(src, des)
writeFile(tmp, f3)
print(src)
print("\n")
print(des)
print("\n")
print(tmp)
