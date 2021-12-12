from copy import copy
from typing import List


class Triangulo:
    def __init__(self, lado1: float, lado2: float, lado3: float):
        self.lado3: float = lado3
        self.lado2: float = lado2
        self.lado1: float = lado1

    def is_triangulo(self):
        lados: List[float] = [self.lado1, self.lado2, self.lado3]

        for pos, lado in enumerate(lados):
            lados_copy = copy(lados)
            lados_copy.pop(pos)
            if not (abs(lados_copy[0] - lados_copy[1]) < lado < sum(lados_copy)):
                return False
        return True

    def print_lados(self):
        for pos, lado in enumerate([self.lado1, self.lado2, self.lado3]):
            print(f'lado{pos}: {lado}')


class TrianguloRetangulo(Triangulo):

    def __init__(self, cateto1: float = None, cateto2: float = None, hipotenusa: float = None):
        cateto1, cateto2, hipotenusa = self.validacao_inicial_dos_lados_informados(cateto1, cateto2, hipotenusa)
        super().__init__(cateto1, cateto2, hipotenusa)

    def validacao_inicial_dos_lados_informados(self, cateto1, cateto2, hipotenusa):
        if self.has_mais_de_dois_nulos([cateto1, cateto2, hipotenusa]):
            raise ValueError('É necessário ter pelo menos 2 valores não nulos')
        elif not hipotenusa:
            hipotenusa = self.calcular_hipotenusa(cateto1, cateto2)
        elif not cateto1:
            cateto1 = self.calcular_cateto(cateto2, hipotenusa)
        elif not cateto2:
            cateto1 = self.calcular_cateto(cateto1, hipotenusa)
        else:
            if not (hipotenusa == self.calcular_hipotenusa(cateto1, cateto2)):
                raise ValueError('Valor de hipotenuas inválido')
        return cateto1, cateto2, hipotenusa

    def has_mais_de_dois_nulos(self, lados: list) -> bool:
        contador_nulos = 0
        for lado in lados:
            if lado == None:
                contador_nulos += 1

            if contador_nulos >= 2:
                return True

        return False

    def calcular_hipotenusa(self, cateto1: float, cateto2: float) -> float:
        return round((cateto1 ** 2 + cateto2 ** 2) ** 0.5, 2)

    def calcular_cateto(self, cateto: float, hipotenusa: float) -> float:
        if cateto >= hipotenusa:
            raise ValueError('Cateto maior ou igual a Hipotenusa')

        return round((hipotenusa ** 2 - cateto ** 2) ** 0.5, 2)

    def is_triangulo_retangulo(self) -> bool:
        if not self.is_triangulo():
            return False

        lados: set = {self.lado1, self.lado2, self.lado3}
        cateto1 = lados.pop()
        cateto2 = lados.pop()
        hipotenusa = lados.pop()

        return hipotenusa == self.calcular_hipotenusa(cateto1, cateto2)

    def get_hipotenusa(self) -> float:
        lados: set = {self.lado1, self.lado2, self.lado3}
        return max(lados)

    def get_menor_cateto(self) -> float:
        lados: set = {self.lado1, self.lado2, self.lado3}
        return min(lados)

    def get_maior_cateto(self) -> float:
        lados = {self.lado1, self.lado2, self.lado3}
        lados.pop()
        return min(lados)

    def get_catetos(self) -> List[float]:
        return list({self.get_menor_cateto(), self.get_maior_cateto()})

    def print_lados(self):
        print(f'cateto_menor: {self.get_menor_cateto()}')
        print(f'cateto_maior: {self.get_maior_cateto()}')
        print(f'hipotenusa: {self.get_hipotenusa()}')
