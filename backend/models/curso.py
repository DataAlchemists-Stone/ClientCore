from config.database import connection_pool

def get_cursos():
    conn = connection_pool.getconn()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM cursos;")
            cursos = cursor.fetchall()
    finally:
        connection_pool.putconn(conn)
    return cursos
