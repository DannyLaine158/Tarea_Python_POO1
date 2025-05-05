from User import User
from Seasson import Seasson

class Student(User):
    def __init__(self, paramNombre, paramEdad, paramActivo = True):
        super().__init__(paramNombre, paramEdad, paramActivo)
        self.courses = [] # Tiene una lista de cursos vacía
        self.carnet = None
        self.cycle = None

    # Agregación:
    def addCourse(self, course):
        self.courses.append(course)

    # Asociación
    def setCarnet(self, carnet):
        self.carnet = carnet

    def setCycle(self, cycle: Seasson):
        self.cycle = cycle

    # Matematica 1, Matematica 2, Fisica 1 = ', ' unir con elementos de lista
    def __str__(self):
        return f"""Estudiante {self.carnet}: {super().__str__()}
        Lista de cursos: \n\t {',\n\t '.join(str(cls) for cls in self.courses)}
        Ciclo inicial: {self.cycle.name}"""