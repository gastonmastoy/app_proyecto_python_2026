# museo_app.py

from museo_db import conectar

def agregar_obra():
    """
    Registra una nueva obra en el museo.
    """
    nombre = input("Nombre de la obra: ")
    artista = input("Artista: ")
    descripcion = input("Descripción: ")
    cantidad = int(input("Cantidad: "))
    valor = float(input("Valor estimado: "))
    categoria = input("Categoría: ")
    sala = input("Sala: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO obras (nombre, artista, descripcion, cantidad, valor, categoria, sala)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (nombre, artista, descripcion, cantidad, valor, categoria, sala))

    conexion.commit()
    conexion.close()

    print("✅ Obra registrada")


def mostrar_obras():
    """
    Muestra todas las obras del museo.
    """
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM obras")
    obras = cursor.fetchall()

    for obra in obras:
        print(obra)

    conexion.close()


def buscar_obra():
    """
    Busca una obra por su ID.
    """
    id_obra = int(input("ID de la obra: "))

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM obras WHERE id = ?", (id_obra,))
    obra = cursor.fetchone()

    if obra:
        print(obra)
    else:
        print("❌ No encontrada")

    conexion.close()


def actualizar_obra():
    """
    Modifica los datos de una obra existente.
    """
    id_obra = int(input("ID a actualizar: "))

    nombre = input("Nuevo nombre: ")
    artista = input("Nuevo artista: ")
    descripcion = input("Nueva descripción: ")
    cantidad = int(input("Nueva cantidad: "))
    valor = float(input("Nuevo valor: "))
    categoria = input("Nueva categoría: ")
    sala = input("Nueva sala: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    UPDATE obras
    SET nombre=?, artista=?, descripcion=?, cantidad=?, valor=?, categoria=?, sala=?
    WHERE id=?
    """, (nombre, artista, descripcion, cantidad, valor, categoria, sala, id_obra))

    conexion.commit()
    conexion.close()

    print("✅ Obra actualizada")


def eliminar_obra():
    """
    Elimina una obra del sistema.
    """
    id_obra = int(input("ID a eliminar: "))

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM obras WHERE id = ?", (id_obra,))

    conexion.commit()
    conexion.close()

    print("🗑️ Obra eliminada")


def reporte_obras():
    """
    Muestra obras con baja cantidad.
    """
    limite = int(input("Cantidad mínima: "))

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM obras WHERE cantidad <= ?", (limite,))
    obras = cursor.fetchall()

    for obra in obras:
        print(obra)

    conexion.close()