class estudiante:
    def __init__(self):
        self.nombre=""
        self.apellido=""
        self.edad=10
    def verificarEdad(self):
        print("La Edad del usuario es:")
        print(str(self.edad))

est1=estudiante()
est1.nombre="Daniel"
est1.apellido="Ingaruca"
est1.edad=26

est2=estudiante()
est2.nombre="Mario"
est2.apellido="Siles"
est2.edad=36

print("Datos del primer estudiante:")
print(est1.nombre)
print(est1.apellido)
print(str(est1.edad))

print("Datos del segundo estudiante")
print(est2.nombre)
print(est2.apellido)
print(str(est2.edad))

print(type(est1))
print(type(est2))

lista_estudiantes=[est1,est2]
print("Se imprimen los nombres de los estudiantes creados:")
for alumno in lista_estudiantes:
    print(alumno.nombre)

est1.verificarEdad()
est2.verificarEdad()