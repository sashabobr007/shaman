import stanza
# Скачивание требуемой модели
stanza.download('ru')
# инициализация нейронной модели
nlp = stanza.Pipeline('ru')
#Текст, содержащий адреса
text = "текст текст текст , ул. 9 Января, д. 68к текст текст текст"
#Извлечение адреса из текста
doc = nlp(text)
#Цикл для вывода адреса в удобной форме
for el in doc.sentences:
    for ent in el.entities:
        if (ent.type in ('LOC')):
            print (ent.text,' ',ent.type)
