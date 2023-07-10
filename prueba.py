import os
os.system("clear")

print("", " PROGRAMA DE PRUEBA ", "", sep="xxxxx")
nombre = input("Introduce tu nombre: ")
m = "gatos"
m1 = "odín"
m2 = "simba."
mensaje = "Tu nombre es {a} y tienes 2 {b}, uno se llama {c} y la otra se llama {d}"
print(mensaje.format(a = nombre.capitalize(), b = m, c = m1.capitalize(), d = m2.capitalize()))
