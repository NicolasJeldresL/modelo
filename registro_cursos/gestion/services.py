from .models import Curso, Profesor, Estudiante, Direccion

def crear_curso(nombre, descripcion):
    curso = Curso(nombre=nombre, descripcion=descripcion)
    curso.save()
    return curso

def crear_profesor(nombre, direccion_id):
    direccion = Direccion.objects.get(pk=direccion_id)
    profesor = Profesor(nombre=nombre, direccion=direccion)
    profesor.save()
    return profesor

def crear_estudiante(nombre, direccion_id):
    direccion = Direccion.objects.get(pk=direccion_id)
    estudiante = Estudiante(nombre=nombre, direccion=direccion)
    estudiante.save()
    return estudiante

def crear_direccion(calle, ciudad, codigo_postal):
    direccion = Direccion(calle=calle, ciudad=ciudad, codigo_postal=codigo_postal)
    direccion.save()
    return direccion

def obtiene_estudiante(estudiante_id):
    return Estudiante.objects.get(pk=estudiante_id)

def obtiene_profesor(profesor_id):
    return Profesor.objects.get(pk=profesor_id)

def obtiene_curso(curso_id):
    return Curso.objects.get(pk=curso_id)

def agrega_profesor_a_curso(profesor_id, curso_id):
    profesor = Profesor.objects.get(pk=profesor_id)
    curso = Curso.objects.get(pk=curso_id)
    profesor.cursos.add(curso)
    profesor.save()

def agrega_cursos_a_estudiante(estudiante_id, curso_ids):
    estudiante = Estudiante.objects.get(pk=estudiante_id)
    cursos = Curso.objects.filter(id__in=curso_ids)
    estudiante.cursos.add(*cursos)
    estudiante.save()

def imprime_estudiante_cursos(estudiante_id):
    estudiante = Estudiante.objects.get(pk=estudiante_id)
    cursos = estudiante.cursos.all()
    print(f"Estudiante: {estudiante.nombre}")
    for curso in cursos:
        print(f"   Curso: {curso.nombre}")