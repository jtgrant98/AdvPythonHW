codes = {'A':'#','a':'1','B':'@','b':'2','C':'$','c':'3','D':'!','d':'4','E':'^','e':'5','F':'&','f':'6','G':'*','g':'7',\
'H':'.','h':'8',"I":'`','i':'9','J':'-','j':'10','K':'~','k':'11','L':'_','l':'12','M':'?','m':'13','N':'+','n':'14','O':'(','o':'15',\
'P':'<','p':'16','Q':')','q':'17','R':'=','r':'18','S':':','s':'19','T':';','t':'20','U':']','u':'21','V':'|','v':'22','W':'}','w':'23',\
'X':'k','x':'24','Y':'q','y':'25','Z':'a','z':'26'}

infile = open('info_security.txt','r')
read_infile = infile.read()


infile.close()


Text_encrypted = open('Text_encrypted.txt','w')

for i in read_infile:
    if i in codes:
        Text_encrypted.write(codes[i])
    else:
        print('This file is encrypted.')
Text_encrypted.close()
