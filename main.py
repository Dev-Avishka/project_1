import os 

print("option 1: run system command")
print("option 2: Create file")


def excmd():
    inp = input("command ")
    os.system(inp)

def createfile():
    file_name = input("file name ")
    print("1:Java")
    print("2: Python")
    print("3: C++")
    option = int(input("choice number: "))
    if option == 1:
        name = file_name+".java"
        f = open(name,"w+")
        ll = "{}"
        f.write(f"public class {file_name}{ll}")
        print("your file has been created")
    if option == 2:
        name = file_name+".py"
        f = open(name,"w+")
        ll = "{}"
        f.write("print('hello world')")
        print("your file has been created")
        
    if option == 3:
        name = file_name+".cpp"
        name2 = file_name+".hpp"
        f = open(name,"w+")
        f2 = open(name2,"w+")
        ll = "{}"
        f.write(f"int main{ll}")
        f2.write("pragma once;")
        print("initializing g++")
        print("success")
        print("your file has been created")

while True:
    option = int(input("option "))
    if option == 1:
        excmd()
    if option == 2:
        createfile()