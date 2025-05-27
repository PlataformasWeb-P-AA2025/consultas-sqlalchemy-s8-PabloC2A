from sqlalchemy.orm import sessionmaker
from clases import Entrega, Tarea, Estudiante, engine

# Crear sesión para ejecutar consultas
Session = sessionmaker(bind=engine)
session = Session()

# Obtener todas las tareas asignadas a los siguientes estudiantes:
# Jennifer Bolton, Elaine Perez, Heather Henderson, Charles Harris
# Mostrar: título de la tarea, nombre del estudiante, número de entregas por tarea
nombres_estudiantes = ["Jennifer Bolton", "Elaine Perez", "Heather Henderson", "Charles Harris"]

tareas = (session.query(Tarea).join(Tarea.entregas)
                              .join(Entrega.estudiante)
                              .filter(Estudiante.nombre.in_(nombres_estudiantes))
                              .all())

# Imprimir los resultados obteneidos
for tarea in tareas:
    for entrega in tarea.entregas:
        if entrega.estudiante.nombre in nombres_estudiantes:
            print(f"Estudiante: {entrega.estudiante.nombre}, Tarea: {tarea.titulo}, Número de entregas: {len(tarea.entregas)}")
            break
