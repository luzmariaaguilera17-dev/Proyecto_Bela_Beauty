import sqlite3
from datetime import datetime

DB_NAME = "bela_beauty.db"

# -------------------------------
# Inicializar base de datos
# -------------------------------
def inicializar_bd():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Tabla de usuarios
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL UNIQUE,
            contraseña TEXT NOT NULL,
            nombre_completo TEXT,
            correo TEXT,
            rol TEXT DEFAULT 'usuario',
            fecha_creacion TEXT NOT NULL
        )
    """)
    
    # Tabla de citas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS citas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            telefono TEXT NOT NULL,
            dia TEXT NOT NULL,
            hora TEXT NOT NULL,
            estado TEXT DEFAULT 'pendiente',
            fecha_creacion TEXT NOT NULL,
            fecha_actualizacion TEXT
        )
    """)
    
    # Usuario admin
    cursor.execute("""
        INSERT OR IGNORE INTO usuarios (usuario, contraseña, nombre_completo, correo, rol, fecha_creacion)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ("admin", "admin", "Administrador", "admin@example.com", "admin", datetime.now().isoformat()))
    
    # Usuario normal
    cursor.execute("""
        INSERT OR IGNORE INTO usuarios (usuario, contraseña, nombre_completo, correo, rol, fecha_creacion)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ("luz", "12345", "luz aguilera", "luz@gmail.com", "usuario", datetime.now().isoformat()))
    
    conn.commit()
    conn.close()

# -------------------------------
# Funciones para citas
# -------------------------------
def crear_cita(nombre, email, telefono, dia, hora):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO citas (nombre, email, telefono, dia, hora, fecha_creacion)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nombre, email, telefono, dia, hora, datetime.now().isoformat()))
    conn.commit()
    cita_id = cursor.lastrowid
    conn.close()
    return cita_id

def obtener_citas():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, nombre, email, telefono, dia, hora, estado, fecha_creacion 
        FROM citas 
        ORDER BY dia, hora
    """)
    citas = cursor.fetchall()
    conn.close()
    return citas

def obtener_cita_por_id(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM citas WHERE id = ?", (id,))
    cita = cursor.fetchone()
    conn.close()
    return cita

def actualizar_cita(id, nombre, email, telefono, dia, hora):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE citas 
        SET nombre = ?, email = ?, telefono = ?, dia = ?, hora = ?, 
            fecha_actualizacion = ?
        WHERE id = ?
    """, (nombre, email, telefono, dia, hora, datetime.now().isoformat(), id))
    conn.commit()
    conn.close()

def eliminar_cita(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM citas WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def cambiar_estado_cita(id, estado):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE citas 
        SET estado = ?, fecha_actualizacion = ?
        WHERE id = ?
    """, (estado, datetime.now().isoformat(), id))
    conn.commit()
    conn.close()

# -------------------------------
# Funciones para usuarios (ya existentes)
# -------------------------------
def verificar_login(usuario, contraseña):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND contraseña=?", (usuario, contraseña))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

def crear_usuario(usuario, contraseña, nombre_completo="", correo="", rol="usuario"):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usuarios (usuario, contraseña, nombre_completo, correo, rol, fecha_creacion)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (usuario, contraseña, nombre_completo, correo, rol, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_rol_usuario(usuario):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT rol FROM usuarios WHERE usuario=?", (usuario,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "usuario"