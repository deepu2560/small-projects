with open("demo.txt") as file:
    content = file.read()
    print(content)

with open("demo.txt", mode="a") as file:
    file.write("\nNew Text file")

with open("new_demo.txt", mode="a") as file:
    file.write("Hello world")
