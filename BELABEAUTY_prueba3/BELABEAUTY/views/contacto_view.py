import flet as ft
from views.navbar import NavBar

class ContactoView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__("/contacto", controls=[])
        self.page = page
        self.build_view()

    def build_view(self):
        # Campos del formulario
        nombre_field = ft.TextField(
            label="Nombre",
            width=400,
            filled=True,
            bgcolor=ft.Colors.WHITE,
            border_radius=10
        )
        
        email_field = ft.TextField(
            label="Email",
            width=400,
            filled=True,
            bgcolor=ft.Colors.WHITE,
            border_radius=10
        )
        
        mensaje_field = ft.TextField(
            label="Mensaje",
            multiline=True,
            min_lines=5,
            max_lines=10,
            width=400,
            filled=True,
            bgcolor=ft.Colors.WHITE,
            border_radius=10
        )
        
        # Función para enviar mensaje
        def enviar_mensaje(e):
            if not nombre_field.value or not email_field.value or not mensaje_field.value:
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Por favor completa todos los campos."),
                    bgcolor=ft.Colors.RED_400
                )
            else:
                # Aquí normalmente enviarías el mensaje a un servidor
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Gracias, tu mensaje ha sido enviado."),
                    bgcolor=ft.Colors.GREEN_400
                )
                # Limpiar formulario
                nombre_field.value = ""
                email_field.value = ""
                mensaje_field.value = ""
            
            self.page.snack_bar.open = True
            self.page.update()
        
        # Función para abrir Instagram
        def abrir_instagram(e):
            self.page.launch_url("https://instagram.com/belabeauty_")
        
        # Información de contacto
        info_contacto = [
            {
                "icono": ft.Icons.PHONE,
                "titulo": "CELULAR",
                "valor": "+123-456-7890",
                "color": ft.Colors.AMBER_600,
                "accion": None
            },
            {
                "icono": ft.Icons.PHOTO_CAMERA,
                "titulo": "INSTAGRAM",
                "valor": "@belabeauty_",
                "color": ft.Colors.PINK_600,
                "accion": abrir_instagram
            },
            {
                "icono": ft.Icons.EMAIL,
                "titulo": "EMAIL",
                "valor": "hello@reallygreatsite.com",
                "color": ft.Colors.BLUE_600,
                "accion": None
            },
            {
                "icono": ft.Icons.LOCATION_ON,
                "titulo": "UBICACIÓN",
                "valor": "Itacurubi de la Cordillera",
                "color": ft.Colors.GREEN_600,
                "accion": None
            }
        ]
        
        # Función para crear tarjetas de información
        def crear_tarjeta_info(info):
            # Contenido del icono
            icon_content = ft.Icon(
                info["icono"],
                size=40,
                color=info["color"]
            )
            
            # Si es Instagram, hacerlo clickeable
            if info["accion"]:
                icon_content = ft.GestureDetector(
                    content=icon_content,
                    on_tap=info["accion"]
                )
            
            return ft.Container(
                content=ft.Column(
                    [
                        icon_content,
                        ft.Text(
                            info["titulo"],
                            size=16,
                            weight=ft.FontWeight.W_600,
                            color=ft.Colors.GREY_700
                        ),
                        ft.Text(
                            info["valor"],
                            size=14,
                            color=ft.Colors.GREY_600,
                            text_align=ft.TextAlign.CENTER
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                ),
                width=200,
                padding=20,
                bgcolor=ft.Colors.WHITE,
                border_radius=15,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=10,
                    color=ft.Colors.BLACK12,
                ),
                margin=10,
                on_click=info["accion"] if info["accion"] else None
            )
        
        # Contenedor de información de contacto
        info_container = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "CONTÁCTENOS",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.AMBER_800,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=20),
                    ft.Row(
                        [crear_tarjeta_info(info) for info in info_contacto],
                        wrap=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                        run_spacing=20
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=20,
            margin=ft.margin.only(bottom=30)
        )
        
        # Formulario de contacto
        formulario_container = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "ENVÍANOS UN MENSAJE",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.AMBER_700,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=20),
                    nombre_field,
                    ft.Container(height=15),
                    email_field,
                    ft.Container(height=15),
                    mensaje_field,
                    ft.Container(height=20),
                    ft.ElevatedButton(
                        "ENVIAR MENSAJE",
                        on_click=enviar_mensaje,
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.AMBER_200,
                            color=ft.Colors.BLACK,
                            padding=ft.padding.symmetric(horizontal=30, vertical=15),
                            elevation=5
                        ),
                        icon=ft.Icons.SEND,
                        icon_color=ft.Colors.BLACK
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            width=450,
            padding=30,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.BLACK12,
            ),
            margin=ft.margin.only(bottom=30)
        )
        
        # Construir la vista completa (sin mapa ni horario)
        self.controls = [
            ft.Column(
                [
                    NavBar(self.page),
                    
                    # Contenido principal
                    ft.Container(
                        content=ft.Column(
                            [
                                # Información de contacto
                                info_container,
                                
                                # Formulario
                                formulario_container,
                            ],
                            scroll=ft.ScrollMode.AUTO,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0
                        ),
                        padding=20,
                        expand=True
                    )
                ],
                spacing=0,
                expand=True
            )
        ]