import sqlite3
from datetime import datetime

DB_NAME = "usuarios.db"

# -------------------------------
# Inicializar base de datos
# -------------------------------
def inicializar_bd():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
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
    # Usuario admin
    cursor.execute("""
        INSERT OR IGNORE INTO usuarios (usuario, contraseña, nombre_completo, correo, rol, fecha_creacion)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ("admin", "admin", "Administrador", "admin@example.com", "admin", datetime.now().isoformat()))
    
    # Usuario normal
    cursor.execute("""
        INSERT OR IGNORE INTO usuarios (usuario, contraseña, nombre_completo, correo, rol, fecha_creacion)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ("luz", "12345", "luz agilera ", "luz@gmail.com", "usuario", datetime.now().isoformat()))
    
    conn.commit()
    conn.close()

# -------------------------------
# Verificar login
# -------------------------------
def verificar_login(usuario, contraseña):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND contraseña=?", (usuario, contraseña))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

# -------------------------------
# Crear nuevo usuario
# -------------------------------
def crear_usuario(usuario, contraseña, nombre_completo="", correo="", rol="usuario"):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usuarios (usuario, contraseña, nombre_completo, correo, rol, fecha_creacion)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (usuario, contraseña, nombre_completo, correo, rol, datetime.now().isoformat()))
    conn.commit()
    conn.close()

# -------------------------------
# Obtener rol de un usuario
# -------------------------------
def get_rol_usuario(usuario):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT rol FROM usuarios WHERE usuario=?", (usuario,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "usuario"
