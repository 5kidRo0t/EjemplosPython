import os

def limp():
    os.system("clear")
def muestra():
    print("/")
def ayuda():
    print("pwd / clear / exit")

dic={"clear":limp,"pwd":muestra, "help":ayuda}
while True:
    terminal = input("Terminal: ")
    if terminal == "exit":
        break
    if terminal in dic:
        dic[terminal]()
    else:
        print("Command", terminal, "not found")
