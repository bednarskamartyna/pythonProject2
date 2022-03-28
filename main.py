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
    print(word_list)

count_words("sonety.txt")


