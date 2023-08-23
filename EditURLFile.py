''' NOT FINISHED
from sys import exit
def urllen(text):
    while len(text) < 60:
        text+=' '
    return text
def choosearg(inp):
    if inp == 'name':
        return True
    elif inp == 'url':
        return False
    else:
        return 'ERR'
with open('URLS.TXT', 'r', encoding='utf-8-sig') as f:
    data = f.readlines()
    f.close()
print('-----------------------------------------')
urllist=[]
namelist=[]
for i in data:

    urllist.append(i.split(' ')[0])
    namelist.append(i.split(' ')[-1].strip('\n').strip('\r'))

    print('|   {}   |   {}   '.format(urllen(i.split(' ')[0]), urllen(i.split(' ')[-1].strip('\n').strip('\r'))))
print('-----------------------------------------')
while True:
    userinput=input('>>')
    if userinput=='exit':
        exit()
    elif userinput=='help':
        print()
    elif userinput[:4]=='add ':
        arg=choosearg(userinput[4:7])

    elif userinput[:4]=='set ':
        arg=choosearg(userinput[4:7])
        if arg == 'ERR':
            print('[ERR]Arg is illegal')
            continue
        elif arg == True:
            vil = False
            name = userinput[8:]
            temp = 0
            for x in namelist:
                if x == name:
                    vil = True
                    break
                temp += 1
            if vil == False:
                print('[ERR]THERE ARE NO URL NAME:' + name)
                continue
            
    elif userinput[:4]=='del ':
        arg=choosearg(userinput[4:7])
    elif userinput[:5] == 'save ':
    else:
        print('[ERROR]THIS COMMAND IS NOT EXIST')'''