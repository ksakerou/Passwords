import requests
from transliterate import translit
import itertools
import time
import sys

#zaborchik

def fence(str1,str2):
    res = ""
    for i in range(max(len(str1),len(str2))):
        if i < len(str1):
            res = res + str1[i]
        if i < len(str2):
            res = res + str2[i]
    return res

#exit

def endd(begin):
    wtime = time.time() - begin
    print("Success! Time wasted: " + str(wtime) + "sec.")
    sys.exit()


password = input("PASSWORD:")
vklink = input("VK LINK:")
bthday = input("DATE OF BIRTHDAY(13042004):")

begin  = time.time()

try:
    vkname = requests.get(vklink).text    
    if vkname.find('page_name') != -1:
        vkname = vkname[vkname.find('page_name'):]
    elif vkname.find('op_header') != -1:
        vkname = vkname[vkname.find('op_header'):]
    vkname = vkname[vkname.find('>')+1:vkname.find(' ')]
    vkname = translit(vkname, language_code = 'ru', reversed = True)
except Exception:
    print("Invalid link.Please try again")
    sys.exit()

#set of artems

names = [vkname,'','','','']
names[1] = vkname.lower()
names[2] = vkname.upper()
for i,s in enumerate(vkname, start = 0):
    if i%2:
        names[3] = names[3] + s.lower()
    else:
        names[3] = names[3] + s.upper()
        
for i,s in enumerate(vkname, start = 1):
    if i%2:
        names[4] = names[4] + s.lower()
    else:
        names[4] = names[4] + s.upper()

#0) lonely artems

if password in names:
    endd(begin)

#1) artems + bth
for name in names:
    for i in range(1,len(bthday)+1):
        for bth in itertools.permutations(bthday,i):
            lst  = [fence(name,bth),fence(bth,name),name + ''.join(bth),''.join(bth) + name]
            if password in lst:
                endd(begin)

#2) artems + worstpass

with open('500-worst-passwords.txt',"r", encoding = "utf-8") as worstpass:
    words = worstpass.readlines()
    for name in names:
        for word in words:
            word = word[:-1]
            lst = [fence(name,word),fence(word,name),name + word,word + name,word]
            if password in lst:
                endd(begin)
                

#3) ня пока

with open("mydict.txt","r", encoding = "utf-8") as mydict:
    words = mydict.readlines()
    for word in words:
        if word[:-1] == password:
            endd(begin)
            
print("Sorry. My script can't crack your password. You passed the test:)")
                    
