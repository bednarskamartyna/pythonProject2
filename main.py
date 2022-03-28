import modulefinder


def longest_word(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read().split()
        #print(text)
        lword = text[0]
        for i in text:
            if len(lword)<len(i):
                lword = i
        return lword
print(longest_word("text.txt"))

# exception handling
# try:
#     msg = lst[5]
# except IndexError as error:
#     msg = "Jesteś poza zakresem listy ("+str(error)+")"
# print(msg)

# Napisz program w Pythonie, który zapisze listę do pliku.
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']



def colors(filename):
    save_list = open(filename, 'w')  # otwieramy plik w trybie do zapisu
    save_list.write(str(color))

colors("Lista.txt")

# Napisz program w Pythonie, aby ocenić, czy plik jest zamknięty, czy nie.

filename = ("Lista.txt")

try:
    with open("filename", "r") as file:
        print("File has opened for reading.")
except IOError:
    print("File has opened already.")

file = open("Lista.txt", "r")

if not file.closed:
    file.close()
    print("File was closed.")




def count_words(filename):
    f = open(filename, "r", encoding="utf-8")
    word_list = f.read().split()
    print(len(word_list))

count_words("sonety.txt")

#Zliczanie co siódmej liniki tekstu
def count_7_words(filename):
    f = open(filename, "r", encoding="utf-8")
    lines = f.readlines()
    count = 0
    for i in lines:
        if count%7 == 0:
            print("W linijce ", count, "jest ", len((i.split())), " słów")
        count += 1

count_7_words("sonety.txt")


def c_seven(filename):
    f = open(filename, 'r', encoding="utf-8")
    alllines = f.readlines()
    for i in range(0, len(alllines), 7):
        print("w linijce ", i, "jest ", len(alllines[i].split()), "słów")


c_seven('sonety.txt')

import os
os.system("ls")

import math
# os.system("dir")    # Windows
math.pi

from time import sleep
print("Dobranoc")
sleep(2)
print("Dzień dobry")

import os
print (dir(os))


import math
print (dir(math))
math.sin(1)