class MonticuloMediana:
    def __init__(self):
        self.__monticulo_max = MonticuloBinario(es_max=True)
        self.__monticulo_min = MonticuloBinario(es_max=False)
        self.__lista_mediana = []
        self.__mediana = 0

    def agregar_dato(self, nuevo_dato):
        self.__lista_mediana.append(nuevo_dato)

        if len(self.__lista_mediana) == 1:
            self.__mediana = nuevo_dato
            self.__monticulo_max.insertar(nuevo_dato)
            return self.__mediana

        if nuevo_dato > self.__mediana:
            self.__monticulo_min.insertar(nuevo_dato)
        else:
            self.__monticulo_max.insertar(nuevo_dato)

        # Balancear montículos
        if len(self.__monticulo_min) - len(self.__monticulo_max) > 1:
            self.__monticulo_max.insertar(self.__monticulo_min.eliminar())
        elif len(self.__monticulo_max) - len(self.__monticulo_min) > 1:
            self.__monticulo_min.insertar(self.__monticulo_max.eliminar())

        self.__actualizar_mediana()
        return self.__mediana

    def __actualizar_mediana(self):
        if len(self.__monticulo_min) > len(self.__monticulo_max):
            self.__mediana = self.__monticulo_min.obtener_min()
        elif len(self.__monticulo_max) > len(self.__monticulo_min):
            self.__mediana = self.__monticulo_max.obtener_max()
        else:
            self.__mediana = (self.__monticulo_max.obtener_max() + self.__monticulo_min.obtener_min()) / 2

    def calcular_mediana(self):
        return self.__mediana

    def mostrar(self):
        print("Mediana:", self.calcular_mediana())
        print("Datos:", self.__lista_mediana)
        print("Montículo Máx:", self.__monticulo_max)
        print("Montículo Mín:", self.__monticulo_min)


class MonticuloBinario:
    def __init__(self, es_max):
        self.es_max = es_max
        self.__lista = [0]  # índice 0 no se usa
        self.__tamano = 0

    def __len__(self):
        return self.__tamano

    def insertar(self, valor):
        self.__lista.append(valor)
        self.__tamano += 1
        self.__infiltrar_arriba(self.__tamano)

    def eliminar(self):
        if self.__tamano == 0:
            raise IndexError("El montículo está vacío")
        raiz = self.__lista[1]
        self.__lista[1] = self.__lista[self.__tamano]
        self.__tamano -= 1
        self.__lista.pop()
        self.__infiltrar_abajo(1)
        return raiz

    def obtener_max(self):
        if not self.es_max:
            raise ValueError("No es un montículo de máximos")
        if self.__tamano == 0:
            raise IndexError("Montículo vacío")
        return self.__lista[1]

    def obtener_min(self):
        if self.es_max:
            raise ValueError("No es un montículo de mínimos")
        if self.__tamano == 0:
            raise IndexError("Montículo vacío")
        return self.__lista[1]

    def __infiltrar_arriba(self, i):
        while i // 2 > 0:
            padre = i // 2
            if self.__comparar(self.__lista[i], self.__lista[padre]):
                self.__lista[i], self.__lista[padre] = self.__lista[padre], self.__lista[i]
            i = padre

    def __infiltrar_abajo(self, i):
        while i * 2 <= self.__tamano:
            hijo = self.__hijo_prioritario(i)
            if self.__comparar(self.__lista[hijo], self.__lista[i]):
                self.__lista[i], self.__lista[hijo] = self.__lista[hijo], self.__lista[i]
            else:
                break
            i = hijo

    def __hijo_prioritario(self, i):
        if i * 2 + 1 > self.__tamano:
            return i * 2
        if self.__comparar(self.__lista[i * 2], self.__lista[i * 2 + 1]):
            return i * 2
        else:
            return i * 2 + 1

    def __comparar(self, a, b):
        return a > b if self.es_max else a < b

    def __str__(self):
        return str(self.__lista[1:])
