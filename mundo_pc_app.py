from ClasesObjetos.Mundo_pc.computadora import Computadora
from ClasesObjetos.Mundo_pc.monitor import Monitor
from ClasesObjetos.Mundo_pc.orden import Orden
from ClasesObjetos.Mundo_pc.raton import Raton
from ClasesObjetos.Mundo_pc.teclado import Teclado

print("*** Mundo pc ***")

if __name__ == "__main__":
    teclado1 = Teclado("HP","USB")
    raton1 = Raton("HP","USB")
    monitor1 = Monitor("HP",27)
    computadora1 = Computadora("HP", monitor1, teclado1, raton1)

    teclado2 = Teclado("Gamer","Bluetooth")
    raton2 = Raton("Gamer","Bluetooth")
    monitor2 = Monitor("Gamer",30)
    computadora2 = Computadora("Gamer", monitor2, teclado2, raton2)

computadoras1 = [computadora1,computadora2]
orden1 = Orden(computadoras1)
print(orden1)
