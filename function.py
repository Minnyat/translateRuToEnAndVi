from googletrans import Translator
import re
class pair3():
    ru = ''
    en = ''
    vi = '' 
def readFile(name):
    f = open(name,"r")
    dataRead = f.read()
    dataReturn = dataRead.split(" ")   
    return dataReturn
    
def Writefile(name,dataWrite):
    f = open(name, "w")
    for x in dataWrite:
        tempst = " |-| "
        st = x.ru +tempst+x.en+tempst+x.vi+'\n'
        f.write(st,)
    f.close()
def ruToEn(x):
    translator = Translator()
    st = translator.translate(x, dest='en' , src ='ru').text
    return st
def enToVi(x):
    translator = Translator()
    st = translator.translate(x, dest='vi', src ='en').text
    return st
def change(x):
    dataout = []
    for Ru in x:
        temp = pair3()
        temp.ru = Ru
        temp.en = ruToEn(temp.ru)
        temp.vi = enToVi(temp.en)
        dataout.append(temp)
    return dataout

def test(x):
    translator = Translator()
    st = translator.translate(x,dest='en',src='auto')
    print(st)
if __name__ == '__main__':
    test('Всем')