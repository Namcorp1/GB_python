# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

data = "привет абв как леабвс дела абвоск"
words = data.split()
result = [i for i in words if not "абв" in i]
print(result)