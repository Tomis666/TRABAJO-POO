from datos.models import database, Rol

def probar_conexion():
    try:
        # Conectar a la base de datos
        database.connect()
        print("¡Conexión exitosa a MySQL!")

        # Intentar leer la tabla 'rol' que creaste en el SQL
        print("\nLeyendo los roles de la base de datos:")
        roles = Rol.select()
        
        for rol in roles:
            print(f"- ID: {rol.id_rol} | Nombre: {rol.nombre} | Permisos: {rol.permisos}")

    except Exception as e:
        print(f"Hubo un error: {e}")
    finally:
        # Cerrar la conexión
        database.close()

if __name__ == '__main__':
    probar_conexion()