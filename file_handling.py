with open("file.txt", "w") as f:
    f.write("Hello world")
    f.write("hi")
    f.write("Haiqa")
with open("file.txt", "r") as f:
    print(file.read())