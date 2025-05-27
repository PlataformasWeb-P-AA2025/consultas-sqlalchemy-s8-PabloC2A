from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from clases import Curso, Tarea, Entrega, engine

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# 5.1 Obtener todos los cursos
cursos = session.query(Curso).all()

# 5.2 Por cada curso, obtener el promedio de calificaciones de sus entregas
for curso in cursos:
    # Obtener todas las entregas del curso actual
    entregas = session.query(Entrega).join(Entrega.tarea).filter(Tarea.curso == curso).all()

    # Calcular promedio de calificaciones
    if entregas:
        promedio = sum([ent.calificacion for ent in entregas]) / len(entregas)
        print(f"Curso: {curso.titulo} -> Promedio de calificaciones: {promedio:.2f}")
    else:
        print(f"Curso: {curso.titulo} -> No tiene entregas")
