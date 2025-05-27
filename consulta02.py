from sqlalchemy.orm import sessionmaker
from clases import Entrega, Tarea, Curso, Departamento, engine

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los departamentos que tengan entregas con nota <= 0.3.
# Por cada objeto Departamento:
# - Nombre del departamento
# - Número de cursos que tiene ese departamento
# distinct() = sirve para eliminar duplicados si hay múltiples entregas

departamentos_bajas_calificaciones = session.query(Departamento) \
    .join(Curso) \
    .join(Tarea) \
    .join(Entrega) \
    .filter(Entrega.calificacion <= 0.3) \
    .distinct() \
    .all()

# Imprimir los resultados obteneidos
for departamento in departamentos_bajas_calificaciones:
    print(f"Departamento: {departamento.nombre}, Cursos: {len(departamento.cursos)}")
