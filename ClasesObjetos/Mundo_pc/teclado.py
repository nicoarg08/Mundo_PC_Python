from ClasesObjetos.Mundo_pc.dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclado = 1
    def __init__(self, marca,tipo_entrada):
        self.id_teclado = Teclado.contador_teclado
        Teclado.contador_teclado += 1
        super().__init__(marca,tipo_entrada)

    def __str__(self):
        return (f"Id: {self.id_teclado}, Marca: {self.marca}"
                f", Tipo de entrada: {self.tipo_entrada}")

if __name__ == "__main__":
    teclado1 = Teclado("Noga","Bluetooth")
    print(teclado1)
    teclado2 = Teclado("VSG","USB")
    print(teclado2)