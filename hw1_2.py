my_file = open("hw.txt", "r+", encoding="utf-8")
user_input = "s"
while user_input != "":
    user_input = input("Введите текст")
    my_file.write(user_input + "\n")
my_file.seek(0)
i = 0
while True:
    read = my_file.readline()
    if read == "\n":
        break
    else:
        count = len(read) - 1
        print(f"Введенная строка {read}количество символов в строке {count}")
        read = read.split()
        print(f"Количество слов в строке {len(read)}")
        i += 1
print(f"Количество строк {i}")
my_file.close()
