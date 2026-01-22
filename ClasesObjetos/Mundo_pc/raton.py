from ClasesObjetos.Mundo_pc.dispositivo_entrada import  DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 1
    def __init__(self, marca, tipo_entrada):
        self.id_raton = Raton.contador_ratones
        Raton.contador_ratones += 1
        super().__init__(marca,tipo_entrada)

    def __str__(self):
        return (f"id {self.id_raton},Marca {self.marca},"
                f" tipo entrada {self.tipo_entrada}")

# Codigo principal
if __name__ == "__main__":
    raton1 = Raton("HP","USB")
    print(raton1)
    raton2 = Raton("Acer","Bluetooth")
    print(raton2)