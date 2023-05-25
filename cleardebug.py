with open('log.txt','r') as f:
    lines=f.readlines()
    f.close()
with open('lognodebug.txt','w',encoding='utf-8') as fa:
    for i in lines:
        if i[:5] != 'DEBUG':
            fa.write(i)
print('Success')