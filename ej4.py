def cuadradonumero(num_x):
    resultado=num_x*num_x
    return resultado

def mensajeBienvenida(textoInfo):
    print("Bienvenido:")
    print(textoInfo)

cuadrado = cuadradonumero(25)
print("El cuadrado de 25 es:")
print(str(cuadrado))

mensajeBienvenida('Daniel')