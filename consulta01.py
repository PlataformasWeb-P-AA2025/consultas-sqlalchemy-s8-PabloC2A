from sqlalchemy.orm import sessionmaker
from clases import Entrega, Tarea, Estudiante, Curso, Instructor, Departamento, engine

Session = sessionmaker(bind=engine)
session = Session()

# Consulta 1
# Obtener las entregas de todos los estudiantes que pertenecen al departamento de Arte. En función de la entrega, presentar,
# nombre del tarea, nombre del estudiante, calificación, nombre de instructor y nombre del departamento

entregas_arte = session.query(Entrega) \
    .join(Entrega.tarea) \
    .join(Entrega.estudiante) \
    .join(Tarea.curso) \
    .join(Curso.instructor) \
    .join(Curso.departamento) \
    .filter(Departamento.nombre == "Arte") \
    .all()

# Imprimir los resultados obteneidos
for entrega in entregas_arte:
    print(f"Tarea: {entrega.tarea.titulo}, "
          f"Estudiante: {entrega.estudiante.nombre}, "
          f"Calificación: {entrega.calificacion}, "
          f"Instructor: {entrega.tarea.curso.instructor.nombre}, "
          f"Departamento: {entrega.tarea.curso.departamento.nombre}")
