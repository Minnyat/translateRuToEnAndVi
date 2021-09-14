from googletrans import Translator

class pair3():
    ru = ''
    en = ''
    vi = '' 
def check(x):
    cur = ''
    A = []
    for i in x:
        if (i!=' '):
             cur += i 
        else :
            if(len(cur)!=0):
                A.append(cur)
                cur = ''
    if(len(cur)!=0):
        A.append(cur)
    return A

def readFile(name):
    f = open(name,"r",encoding="utf8")
    dataRead = f.read()
    return check(dataRead)
   
def Writefile(name,dataWrite):
    f = open(name, "w", encoding="utf8")
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
        print("translating....",Ru)
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