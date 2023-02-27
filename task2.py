#Задача 2
#1. Найдите пакет http, с помощью функции help изучите модули, из которых он состоит.
#2. Импортируйте модуль client из пакета http.
#3. Воспользуйтесь функционалом импортированного модуля:
#    1. Создайте HTTP соединение по адресу www.google.com
#    2. Отправьте GET запрос по адресу выше
#    3. Проверьте ответ на отправленный запрос

import http.client

conn = http.client.HTTPConnection('www.google.com')
conn.request("GET", "/")

r1 = conn.getresponse()
print(r1.status, r1.reason)