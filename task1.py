#Задача 1
#Дано имя файла: folder1/folder2/file.ext
#Необходимо вывести на экран его расширение с помощью стандартного модуля re.

import re

fileName = "folder1/folder2/file.ext"

a = re.split(r"[.]", fileName)

print(a[1])