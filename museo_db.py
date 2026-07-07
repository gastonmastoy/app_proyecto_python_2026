# museo_db.py

import sqlite3
from config import DB_NAME

def conectar():
    """
    Establece conexión con la base de datos.
    """
    return sqlite3.connect(DB_NAME)


def crear_tabla():
    """
    Crea la tabla 'obras' si no existe.
    """
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS obras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        artista TEXT,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        valor REAL NOT NULL,
        categoria TEXT,
        sala TEXT
    )
    """)

    conexion.commit()
    conexion.close()