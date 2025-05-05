class Course:
    def __init__(self, codCurso, nombreCurso):
        self.codCurso = codCurso
        self.nombreCurso = nombreCurso

    def __str__(self):
        return f"Curso: {self.codCurso} - {self.nombreCurso}"