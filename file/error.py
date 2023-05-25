from os import strerror


try:
    s = open("C:/something.txt", "rt")
    s.close()
except Exception as exc:
    print("The file could not be opened: ", strerror(exc.errno))
