# Visite esta página (https://tutosrive.github.io/sqlazo/)
# Visite esta página (https://tutosrive.github.io/chromologger/)
# Visite esta página (https://tutosrive.github.io/chromolog/)

# pip install sqlazo
# Ejemplo de inicialización
from sqlazo import Database

db = Database('test.db', False)

# Columnas con sus configuraciones
cols = ['id INTEGER PRIMARY KEY', 'name TEXT NOT NULL', 'age INTEGER NOT NULL']
# Ejecutar "consulta" (Crear tabla)
db.create_table('user', cols)
db.insert_data(['Santiago', 19], ['name', 'age'], 'user')

dataAll = db.get_data_all('user')

# Si el tercer parámetro existe, solo se tomarán esa columnas en la "consulta"
# Retornará los registros que cumplen la condición, y solo retornará la columna "name"
# select name from user where id < 3
data_where1 = db.get_data_where('user', 'id < 3', 'name')

# En caso de no existir los *args, se da por entendido que se seleccionarán todas las columnas
# Retorna los registros válidos a la condición y todas las columnas
# select * from user where id < 3*
data_where12 = db.get_data_where('user', 'id < 3')

# Eliminar los usuarios menores de edad
db.delete_data('user', 'age < 18')

# Cerrar conexión con la base de datos
db.close()