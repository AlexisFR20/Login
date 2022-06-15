import psycopg2

conexion1 = psycopg2.connect(database="reloj", user="postgres", password="root")
cursor1=conexion1.cursor()
sql="insert into users(id, username, password) values (%s,%s,%s)"
datos=(0, "username", "password")
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close() 