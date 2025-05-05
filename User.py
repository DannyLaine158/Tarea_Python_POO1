# Clase:
class User:
    # Método Constructor: Inicializa todos los atributos
    def __init__(self,
                paramNombre: str, 
                paramEdad: int, 
                paramActivo: bool = True):
        # Atributos:
        self.__nombre = paramNombre
        self.__edad = paramEdad
        self.__activo = paramActivo
    
    # Método de clase (Métodos Getter):
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def getActivo(self):
        return self.__activo
    
    # Métodos Setter: Siempre debe recibir un parámetro
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setEdad(self, edad):
        self.__edad = edad

    def switchActivo(self):
        # Negar su estado
        self.__activo = not self.__activo
    
    # Método estático
    @staticmethod
    def validateAge(age):
        return age >= 18 # True o False
    
    def __str__(self):
        return f"""
        Nombre: {self.__nombre}
        Edad: {self.__edad}
        { 'Estás activo' if self.__activo else 'No estás activo'}
        """