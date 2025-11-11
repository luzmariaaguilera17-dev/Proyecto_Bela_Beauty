import flet as ft
from db import verificar_login, crear_usuario

def login_view(page, on_login_success):
    # Campos de login
    usuario_input = ft.TextField(label="Usuario", autofocus=True, width=300)
    contraseña_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)

    # Campos de registro
    usuario_reg_input = ft.TextField(label="Usuario", width=300)
    contraseña_reg_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    nombre_input = ft.TextField(label="Nombre completo", width=300)
    correo_input = ft.TextField(label="Correo electrónico", width=300)

    mensaje = ft.Text("", color="red", size=14)

    # Caja de registro (oculta inicialmente)
    registro_box = ft.Column([], visible=False, alignment=ft.MainAxisAlignment.CENTER,
                             horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)

    # Función para registrar usuario
    def registrar_click(e):
        usuario = usuario_reg_input.value.strip()
        contraseña = contraseña_reg_input.value.strip()
        nombre = nombre_input.value.strip()
        correo = correo_input.value.strip()

        if not usuario or not contraseña or not nombre or not correo:
            mensaje.value = "Completa todos los campos para registrarte"
        else:
            try:
                crear_usuario(usuario, contraseña, nombre, correo)
                mensaje.value = "Usuario registrado exitosamente. Ingresa tus datos."
                # Limpiar campos de registro
                usuario_input.value = ""
                contraseña_input.value = ""
                usuario_reg_input.value = ""
                contraseña_reg_input.value = ""
                nombre_input.value = ""
                correo_input.value = ""
                # Restaurar visibilidad de login
                usuario_input.visible = True
                contraseña_input.visible = True
                login_button.visible = True
                registro_box.visible = False
            except Exception as err:
                mensaje.value = f"Error al registrar: {err}"
        page.update()

    # Contenido de registro
    registro_box.controls = [
        ft.Text("Registro de usuario", size=20, weight=ft.FontWeight.BOLD),
        ft.Divider(thickness=1, color="#CCCCCC"),
        usuario_reg_input,
        contraseña_reg_input,
        nombre_input,
        correo_input,
        ft.ElevatedButton(
            "Registrarse",
            on_click=registrar_click,
            width=300,
            style=ft.ButtonStyle(
                bgcolor="#4B0082",
                color="white",
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=ft.Padding(10, 10, 20, 20)
            )
        )
    ]

    # Función login
    def login_click(e):
        usuario = usuario_input.value.strip()
        contraseña = contraseña_input.value.strip()

        if not usuario or not contraseña:
            mensaje.value = "Ingresa usuario y contraseña"
        elif verificar_login(usuario, contraseña):
            on_login_success(usuario)  # Pasamos usuario al main
        else:
            mensaje.value = "Usuario no encontrado. Regístrate a continuación."
            # Mostrar registro y ocultar login
            registro_box.visible = True
            usuario_input.visible = False
            contraseña_input.visible = False
            login_button.visible = False
        page.update()

    # Botón login
    login_button = ft.ElevatedButton(
        "Ingresar",
        on_click=login_click,
        width=300,
        style=ft.ButtonStyle(
            bgcolor="#4B0082",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.Padding(10, 10, 20, 20)
        )
    )

    # Contenedor principal
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Bela Beauty Salon", size=32, weight=ft.FontWeight.BOLD, color="#4B0082"),
                ft.Text("Inicia sesión para continuar", size=18, color="#555555"),
                ft.Divider(thickness=1, color="#CCCCCC", height=20),
                usuario_input,
                contraseña_input,
                login_button,
                registro_box,
                mensaje
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        width=400,
        padding=ft.padding.all(30),
        bgcolor="#F8F8F8",
        border_radius=ft.border_radius.all(15),
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=8,
            color="#888888",
            offset=ft.Offset(3, 3)
        )
    )
