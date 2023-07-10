#Programa de prueba ocultación y encriptación de contraseña en un login by 5kidRo0t // Luxxy
#El usuario es Luxxy y la contraseña es iloveyou1234

import hashlib, getpass, os, time
os.system("clear")

nombre="luxxy"
se= "\033[92m" + ("x" * 70) + "\033[0m"
user = "Luxxy"
intentos = 3
while intentos > 0:
    print(se, "\033[93m\nBIENVENIDO A LUXXY OS\nA continuación se le indicará que ingrese el usuario y la contraseña.\033[0m")
    print(se, "\n")
    userin = input("Introduce el nombre de usuario: ")
    pas = "77e066a97089b91d5e2eeb305f72041d5a30d2b8103765ef1e136c846baf637ec06aebd40814ebc414ca106e62cee725fe50790f49f6fb7bce8293200782ffea"
    passin = getpass.getpass("Ahora introduce la contraseña: ")
    encript = hashlib.sha512(passin.encode()).hexdigest()
    if userin == user and encript == pas:
        intentos = -1
        print("\033[96m¡Enhorabuena! has introducido los datos correctamente.\nBienvenido al sistema Luxxy OS, si necesita mas informacion teclee [help]\033[0m")
    if userin != user and encript != pas:
        intentos -= 1
        print("\033[91mEres gilipollas y te quedan", intentos, "intentos.\n\033[0m")
        os.system("sleep 3")
        os.system("clear")
    if intentos == 0:
        def mostrar_texto_progresivo(texto, delay=0.07):
            for i in range(len(texto)):
                print(texto[:i+1], end=" ", flush=True)
                time.sleep(delay)
            print()
        texto = "航海できない小さなボートがありサタンが彼ら全員を殺すためにやって来ました昔々航海できない小さなボートがありサタンが彼ら全 昔々航海できない小さなボートがありサタンが彼ら全員を殺すためにやって来ました昔々航海できない小さなボートがありサタンが彼ら全員 昔々航海できない小さなボートがありサタンが彼ら全員を殺すためにやって来ました昔々航海できない小さなボートがありサタンが彼きない小さなボートがありサタンが彼ら全員を殺すためにやって来ました"
        mostrar_texto_progresivo(texto)
        os.system("sleep 3")
        os.system("clear")
    carpeta="/"
    ficheros="home"
    daa="No se ha encontrado el directorio."
    def listar():
        if terminal == "ls":
            print(ficheros)
    def whoami():
        print(carpeta)
    def entrar():
        carpeta="/"
        ficheros="home"
        if terminal == "cd "+ficheros and carpeta == "/":
            carpeta="/home"
            ficheros="luxxy"
        else:
            print(daa)
        if terminal == "cd luxxy" and carpeta == "/home":
            carpeta="/home/luxxy"
            ficheros="Desktop"
        else:
            print(daa)
        if terminal == "cd Desktop" or "cd "+"desktop" and carpeta == "/home/luxxy":
            carpeta="/home/luxxy/Desktop"
            ficheros="Malware.exe"
        else:
            print(daa)
    def atras():
        if terminal == "cd .." or "cd..":
            if carpeta == "/":
                print(carpeta)
            if carpeta == "/home":
                carpeta="/"
            if carpeta == "/home/luxxy":
                carpeta="/home"
            if carpeta == "/home/luxxy/Desktop":
                carpeta="/home/luxxy"
comandos={"pwd":whoami, "ls":listar, "cd ..":atras, ("cd "+ficheros):entrar}
while True:
    terminal = input("root@luxxy~$ ")
    if terminal in comandos:
            comandos[terminal]()
    if terminal == "help":
            print("exit-----para salir")
    if terminal == "exit":
        break