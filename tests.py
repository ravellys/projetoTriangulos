from triangulos import Triangulo, TrianguloRetangulo


def test_is_not_triangulo():
    lados = (1, 2, 3)
    triangulo = Triangulo(*lados)
    assert triangulo.is_triangulo() == False


def test_is_triangulo():
    lados = (10, 9, 5)
    triangulo = Triangulo(*lados)
    assert triangulo.is_triangulo() == True


def test_is_triangulo_retangulo():
    cateto1 = 1
    cateto2 = 2
    hipotenusa = round((cateto2 ** 2 + cateto1 ** 2) ** 0.5, 2)
    lados = (cateto1, cateto2, hipotenusa)
    triangulo_retangulo = TrianguloRetangulo(*lados)
    assert triangulo_retangulo.is_triangulo() == True
    assert triangulo_retangulo.is_triangulo_retangulo() == True


def test_triangulo_retangulo_get_hipotenusa():
    cateto1 = 1
    cateto2 = 2
    hipotenusa = round((cateto2 ** 2 + cateto1 ** 2) ** 0.5, 2)

    lados = (cateto1, cateto2, None)
    triangulo_retangulo = TrianguloRetangulo(*lados)
    assert triangulo_retangulo.get_hipotenusa() == hipotenusa
    assert triangulo_retangulo.is_triangulo_retangulo() == True


def test_triangulo_retangulo_get_catetos():
    cateto1 = 1
    cateto2 = 2
    catetos = list({cateto1, cateto2})
    menor_cateto = min(catetos)
    maior_cateto = max(catetos)

    lados = (cateto1, cateto2, None)
    triangulo_retangulo = TrianguloRetangulo(*lados)
    assert triangulo_retangulo.get_catetos() == catetos
    assert triangulo_retangulo.get_menor_cateto() == menor_cateto
    assert triangulo_retangulo.get_maior_cateto() == maior_cateto
    assert triangulo_retangulo.is_triangulo_retangulo() == True