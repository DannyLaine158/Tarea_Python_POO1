# from User import User
# Método Main
from Teacher import Teacher
from Student import Student
from Course import Course
from Carnet import Carnet
from Seasson import Seasson

# Instancia u Objeto: Creación de un objeto
edad = 54
teacher = None
if Teacher.validateAge(edad):
    teacher = Teacher("Daniel", edad)
    #print("Tienes una edad adecuada")
else:
    pass
    #print("Debes ser mayor de edad")

#user2 = User("Javier", 26)
#user3 = User("Jose", 30, False)
teacher.setNombre("Juan")
teacher.switchActivo()
teacher.switchActivo()

# print(teacher.teach())

# Estudiantes:
student1 = Student("Larry", 16)

carnet = Carnet("201800722", "2018")
student1.setCarnet(carnet)

# Cursos:
course1 = Course('001', 'Matemática 1')
course2 = Course('002', 'Programación 1')
# print(course1)

"""
print(Seasson.CYCLE_ONE)
print(Seasson.CYCLE_ONE.name)
print(Seasson.CYCLE_ONE.value)
print(list(Seasson))
"""

# Agregación directa
student1.addCourse(course1)
student1.addCourse(course2)

# Agregar ciclo al estudiante
student1.setCycle(Seasson.CYCLE_TWO)

print(student1)