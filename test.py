from googletrans import Translator

def test(x):
    translator = Translator()
    st = translator.translate(x,src='ru',dest='en')
    print(st)

test('Всем')
