from googletrans import Translator


translator = Translator()

result = translator.translate('안녕하세요.', dest='ja')

print(result.text)
