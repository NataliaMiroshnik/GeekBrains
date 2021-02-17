from googletrans import Translator
with open('new_file4.txt', 'w') as write:
    with open('file4.txt') as file:
        text = file.read()
    rename = Translator()
    new_text = rename.translate(text)
    print(new_text)
