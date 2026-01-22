class Monitor:
    contador_monitores = 0
    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.id_monitor = Monitor.contador_monitores
        self.marca = marca
        self.tamanio = tamanio

    def __str__(self):
        return f"id: {self.id_monitor}, Marca: {self.marca} tamaño: {self.tamanio}"

if __name__ == "__main__":
    monitor1 = Monitor("HP",15)
    print(monitor1)
    monitor2 = Monitor("Dell",22)
    print(monitor2)