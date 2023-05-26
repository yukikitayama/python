from os import strerror

try:
    cnt = 0
    stream = open("text.txt", "rt", encoding="utf-8")
    ch = stream.read(1)

    while ch != "":
        print(ch, end="")
        cnt += 1
        ch = stream.read(1)

    stream.close()

    print("\n\nCharacters in file: ", cnt)

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
