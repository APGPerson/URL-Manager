# -*- coding=utf-8 -*-
import os

import requests,threading,logging
from sys import exit
from shutil import copyfile
from tkinter import filedialog
import time
def CheckUrl(url):
    try:
        URLOBJ=requests.get(url,timeout=(5,10))
    except Exception as e:
        logging.error(str(e))
        return 'Err'
    a=0
    if URLOBJ.status_code  == 200:
        logging.debug(url+' TCPing success')
        return True
    else:
        logging.info(url+' TCPing failed,status code:'+str(URLOBJ.status_code))
        return False
def urllen(text):
    while len(text) < 60:
        text+=' '
    return text
def Print(urls,names):
    file=''
    try:
        file = open('EXISTURLS.TXT','a',encoding='utf-8')
    except Exception as e:
        logging.error(str(e))
        time.sleep(5)
        exit(1)
    for z in range(len(urls)):
        resp = CheckUrl(urls[z])
        if resp == True:
            print('|   {}   |    {}    |   {}   '.format(urllen(urls[z]), 'Accessible',urllen(names[z])))
            try:
                file.write(urls[z]+' '+names[z]+'\r\n')
            except Exception as e:
                logging.error(str(e))
                time.sleep(5)
                exit(1)
        elif resp == 'Err':
            print('|   {}   |      {}       |   {}   '.format(urllen(urls[z]), 'ERROR',urllen(names[z])))
        elif resp == False:
            print('|   {}   |  {}  |   {}   '.format(urllen(urls[z]), 'Not-accessible',urllen(names[z])))
        z+=1
    try:
        file.close()
    except Exception as e:
        logging.error(str(e))
        time.sleep(5)
        exit(1)
    return 0
if __name__ == '__main__':
    logging.basicConfig(filename='log.txt',filemode='w',level=logging.DEBUG)
    m = input('Please choose url file:\n[0] PROGRAM INSTALL PATH\\URLS.TXT\n[1]User input file path')
    fileName = ''
    if m == '0':
        fileName = '.\\URLS.TXT'
    elif m == '1':
        fileName = filedialog.askopenfilename(defaultextension='.txt',filetypes=[('TXT','.txt')],title='Choose URL file')
    else:
        print('PLEASE INPUT 0 OR 1')
        time.sleep(5)
        exit(1)
    if fileName == '':
        print('PLEASE CHOOSE A URL FILE')
        time.sleep(5)
        exit(1)
    elif fileName[-4:] != '.txt':
        print('PLEASE CHOOSE A URL FILE(TXT)')
        time.sleep(5)
        exit(1)
    urllist = []
    namelist = []
    stlist = []
    existurlfile = 'EXISTURLS'+str(int(time.time()))+'.TXT'
    try:
        with open(existurlfile,'w',encoding='utf-8') as f:
            f.close()
        with open(fileName,'r',encoding='utf-8-sig') as f:
            data=f.readlines()
            f.close()
    except Exception as e:
        logging.error(str(e))
        time.sleep(5)
        exit(1)
    for i in data:
        try:
            urllist.append(i.split(' ')[0])
            namelist.append(i.split(' ')[-1].strip('\n').strip('\r'))
        except Exception as e:
            logging.error('INPUT IS NOT LEGAL')
            logging.error(str(e))
            time.sleep(5)
            exit(1)
    print('-----------------------------------------')
    starttime=time.time()
    logging.debug('Start main part at:'+time.ctime(starttime))
    try:
        th1 = threading.Thread(target=Print, args=[urllist[:int(len(urllist)/3-1)],namelist[:int(len(urllist)/3-1)]])
        logging.debug('Create Thread-1 object')
        th2 = threading.Thread(target=Print, args=[urllist[int(len(urllist)/3):int((len(urllist)/3)*2-1)],namelist[int(len(urllist)/3):int((len(urllist)/3)*2-1)]])
        logging.debug('Create Thread-2 object')
        th3 = threading.Thread(target=Print, args=[urllist[int((len(urllist)/3)*2):],namelist[int((len(urllist)/3)*2):]])
        logging.debug('Create Thread-3 object')
        th1.start()
        logging.debug('Run Thread-1 object')
        th2.start()
        logging.debug('Run Thread-2 object')
        th3.start()
        logging.debug('Run Thread-3 object')
        th1.join()
        th2.join()
        th3.join()
    except Exception as e:
        logging.error(str(e))
        time.sleep(5)
        exit(1)
    endtime=time.time()
    logging.debug('Finished main part at:'+time.ctime(endtime))
    logging.debug('Use time:'+str(endtime-starttime)+'s')
    print('-----------------------------------------')
    uin=input('Are you want to change your original file?(y,n)\r\n>>')
    if uin == 'y':
        try:
            copyfile('EXISTURLS.TXT','text.txt')
            logging.debug('Copy file...')
        except Exception as e:
            logging.error(str(e))
            time.sleep(5)
            exit(1)
    else:
        os.remove(existurlfile)
    exit()