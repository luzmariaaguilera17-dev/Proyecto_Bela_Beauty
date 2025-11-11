import flet as ft
from views.navbar import NavBar

class ContactoView(ft.View):
    def _init_(self, page: ft.Page):
        super()._init_("/contacto", controls=[])
        self.page = page
        self.build_view()

    def build_view(self):
        # Campos del formulario
        nombre = ft.TextField(label="Nombre", width=400)
        correo = ft.TextField(label="Correo electrónico", width=400)
        mensaje = ft.TextField(label="Mensaje", multiline=True, min_lines=3, width=400)

        # Función para enviar mensaje
        def enviar(e):
            if not nombre.value or not correo.value or not mensaje.value:
                self.page.snack_bar = ft.SnackBar(ft.Text("Por favor completa todos los campos."), open=True)
            else:
                self.page.snack_bar = ft.SnackBar(ft.Text("Gracias, tu mensaje ha sido enviado."), open=True)
                nombre.value = correo.value = mensaje.value = ""
            self.page.update()

        # Construcción de la vista
        self.controls = [
            ft.Container(
                content=ft.Column(
                    [
                        NavBar(self.page),
                        ft.Text("Contacto", size=28, weight=ft.FontWeight.BOLD),
                        nombre,
                        correo,
                        mensaje,
                        ft.ElevatedButton("Enviar", on_click=enviar, bgcolor=ft.Colors.AMBER_200)
                    ],
                    spacing=10
                ),
                padding=20  # ✅ Padding aplicado correctamente
            )
        ]