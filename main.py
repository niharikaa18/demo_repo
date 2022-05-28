with open("message.txt",encoding='cp1252') as f:
    content = f.read(6)
    print(content)


with open("python.txt", "w",encoding='cp1252') as f:
    f.write("Created a new file \n")
    f.write("This is a testing file")


with open("python.txt", "a",encoding='cp1252') as f:
    f.write("\nThis a new line i have appended without erasing previous content")
