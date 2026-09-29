from peewee import *

database = MySQLDatabase('iec_n2_c1', **{'charset': 'utf8mb4', 'host': 'localhost', 'user': 'iec_n2_c1', 'password': 'iecn2c1'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Articulo(BaseModel):
    contenido = TextField()
    fecha_publicacion = DateField(null=True)
    id_articulo = AutoField()
    id_autor = IntegerField(index=True)
    id_categoria = IntegerField(index=True)
    id_estado = IntegerField(index=True)
    titulo = CharField(max_length=200)

    class Meta:
        table_name = 'articulo'

class ArticuloEtiqueta(BaseModel):
    id_articulo = IntegerField()
    id_etiqueta = IntegerField(index=True)

    class Meta:
        table_name = 'articulo_etiqueta'
        indexes = (
            (('id_articulo', 'id_etiqueta'), True),
        )
        primary_key = CompositeKey('id_articulo', 'id_etiqueta')

class Autor(BaseModel):
    biografia = TextField(null=True)
    id_usuario = IntegerField(primary_key=True)

    class Meta:
        table_name = 'autor'

class Categoria(BaseModel):
    id_categoria = AutoField()
    nombre = CharField(max_length=50)

    class Meta:
        table_name = 'categoria'

class Comentario(BaseModel):
    contenido = TextField()
    fecha = DateField()
    id_articulo = IntegerField(index=True)
    id_comentario = AutoField()
    id_lector = IntegerField(index=True)

    class Meta:
        table_name = 'comentario'

class EstadoArticulo(BaseModel):
    estado = CharField(max_length=30)
    id_estado = AutoField()

    class Meta:
        table_name = 'estado_articulo'

class Etiqueta(BaseModel):
    id_etiqueta = AutoField()
    nombre = CharField(max_length=50)

    class Meta:
        table_name = 'etiqueta'

class Lector(BaseModel):
    correo = CharField(max_length=100)
    id_lector = AutoField()
    id_suscripcion = IntegerField(index=True, null=True)
    nombre = CharField(max_length=100)

    class Meta:
        table_name = 'lector'

class Likes(BaseModel):
    fecha = DateField()
    id_articulo = IntegerField(index=True)
    id_lector = IntegerField(index=True)
    id_like = AutoField()

    class Meta:
        table_name = 'likes'

class Plan(BaseModel):
    duracion = IntegerField()
    id_plan = AutoField()
    nombre = CharField(max_length=50)
    precio = DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        table_name = 'plan'

class Rol(BaseModel):
    id_rol = AutoField()
    nombre = CharField(max_length=50)
    permisos = CharField(null=True)

    class Meta:
        table_name = 'rol'

class Suscripcion(BaseModel):
    estado = CharField(max_length=20)
    fecha_fin = DateField()
    fecha_inicio = DateField()
    id_plan = IntegerField(index=True)
    id_suscripcion = AutoField()

    class Meta:
        table_name = 'suscripcion'

class Usuario(BaseModel):
    contrasenia = CharField()
    correo = CharField(max_length=100)
    id_rol = IntegerField(index=True)
    id_usuario = AutoField()
    nombre = CharField(max_length=100)

    class Meta:
        table_name = 'usuario'

