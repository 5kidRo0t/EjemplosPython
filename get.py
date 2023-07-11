import hashlib, os, getpass
os.system("clear")
print("BIENVENID@\n")
user=[]
pas=[]
while True:
    terminal = input("Indica que deseas hacer escribiendo el número correspondiente a la opción elegida:\n\n1-Crear cuenta\n2-Salir\n\nOpción: ")
    if terminal == "1":
        os.system("clear")
        usuario = input("Introduce el nombre de usuario a crear: ")
        while True:
            contra = getpass.getpass("Introduce la contraseña: ")
            contraconfirm = getpass.getpass("Vuelve a introducir la contraseña: ") 
            if contra == contraconfirm:
                os.system("clear")
                print("Has creado la cuenta correctamente.")
                cipher = hashlib.sha512(usuario.encode()).hexdigest()
                cipher2 = hashlib.sha512(contra.encode()).hexdigest()
                user.append(cipher)
                pas.append(cipher2)
                os.system("sleep 5")
                os.system("clear")
                while True:
                    print("Para iniciar sesión introduzca el usuario y la contraseña por favor.\n")
                    usuario = input("Introduce el nombre de usuario: ")
                    contra = getpass.getpass("Ahora introduzca la contraseña: ")
                    cipher = hashlib.sha512(usuario.encode()).hexdigest()
                    cipher2 = hashlib.sha512(contra.encode()).hexdigest()                
                    if cipher in user and cipher2 in pas:
                        print("Bienvenido al sistema,", usuario.capitalize())
                        os.system("sleep 5")
                        exit()
                    else:
                        os.system("clear")
                        print("Lo sentimos pero el usuario y la contraseña no coinciden.\nVuelva a intentarlo.")
                        os.system("sleep 5")
                        os.system("clear")
            else:
                os.system("clear")
                print("Lo sentimos pero las contraseñas no coinciden vuelva a intentarlo.")
                os.system("sleep 5")
                os.system("clear")
    if terminal == "2":
        os.system("clear")
        print("Adiós\n")
        os.system("sleep 5")
        os.system("clear")
        break
    else:
        os.system("clear")
        print("La opción elegida no es correcta.")
        os.system("sleep 5")