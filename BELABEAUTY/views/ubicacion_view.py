import flet as ft
from views.navbar import NavBar

class UbicacionView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__("/ubicacion", controls=[])
        self.page = page
        self.build_view()

    def build_view(self):
        # Función para abrir Google Maps
        def abrir_google_maps(e):
            self.page.launch_url("https://www.google.com/maps?q=Itacurubi+de+la+Cordillera+Paraguay")
        
        # Mapa placeholder con imagen o icono
        mapa_placeholder = ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.MAP, size=80, color=ft.Colors.AMBER_600),
                    ft.Text(
                        "Mapa de ubicación",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.AMBER_800
                    ),
                    ft.Text(
                        "Itacurubi de la Cordillera, Paraguay",
                        size=16,
                        color=ft.Colors.GREY_600,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=20),
                    ft.ElevatedButton(
                        "Abrir en Google Maps",
                        on_click=abrir_google_maps,
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.AMBER_200,
                            color=ft.Colors.BLACK,
                            padding=ft.padding.symmetric(horizontal=30, vertical=15)
                        ),
                        icon=ft.Icons.MAP,
                        icon_color=ft.Colors.BLACK
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            width=400,
            height=300,
            bgcolor=ft.Colors.WHITE,
            border_radius=20,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.BLACK12,
            ),
            alignment=ft.alignment.center,
            padding=30
        )
        
        # Información de la ubicación
        info_ubicacion = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "NUESTRA UBICACIÓN",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.AMBER_800,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=20),
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Icon(ft.Icons.LOCATION_ON, size=40, color=ft.Colors.GREEN_600),
                                    ft.Text("Dirección", size=18, weight=ft.FontWeight.W_600),
                                    ft.Text("Itacurubi de la Cordillera\nParaguay", size=16, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER)
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=10,
                                width=200
                            ),
                            ft.Container(ft.VerticalDivider(), height=100),
                            ft.Column(
                                [
                                    ft.Icon(ft.Icons.DIRECTIONS, size=40, color=ft.Colors.BLUE_600),
                                    ft.Text("Cómo llegar", size=18, weight=ft.FontWeight.W_600),
                                    ft.Text("En el centro de la ciudad", size=16, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER)
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=10,
                                width=200
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=30
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=30,
            bgcolor=ft.Colors.WHITE,
            border_radius=20,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.Colors.BLACK12,
            ),
            margin=ft.margin.only(bottom=30)
        )
        
        # Horario de atención
        horario_atencion = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "HORARIO DE ATENCIÓN",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.AMBER_800,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=20),
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Text("Lunes a Viernes", size=18, weight=ft.FontWeight.W_600),
                                    ft.Text("8:00 AM - 6:00 PM", size=16, color=ft.Colors.GREY_600)
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            ft.Container(ft.VerticalDivider(), height=50),
                            ft.Column(
                                [
                                    ft.Text("Sábados", size=18, weight=ft.FontWeight.W_600),
                                    ft.Text("9:00 AM - 4:00 PM", size=16, color=ft.Colors.GREY_600)
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=30
                    ),
                    ft.Container(height=20),
                    ft.Text(
                        "Domingos cerrado",
                        size=16,
                        color=ft.Colors.GREY_600,
                        text_align=ft.TextAlign.CENTER
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            width=500,
            padding=30,
            bgcolor=ft.Colors.AMBER_50,
            border_radius=20,
            margin=ft.margin.only(bottom=30)
        )
        
        # Instrucciones adicionales
        instrucciones = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "INFORMACIÓN ADICIONAL",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.AMBER_800,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=10),
                    ft.Text(
                        "• Estacionamiento gratuito disponible\n• Acceso para personas con movilidad reducida\n• Aceptamos tarjetas de crédito y débito",
                        size=16,
                        color=ft.Colors.GREY_600,
                        text_align=ft.TextAlign.CENTER
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=5,
                color=ft.Colors.BLACK12,
            )
        )
        
        # Construir la vista completa
        self.controls = [
            ft.Column(
                [
                    NavBar(self.page),
                    
                    # Contenido principal
                    ft.Container(
                        content=ft.Column(
                            [
                                # Mapa
                                ft.Container(
                                    content=mapa_placeholder,
                                    alignment=ft.alignment.center,
                                    margin=ft.margin.only(top=20, bottom=30)
                                ),
                                
                                # Información de ubicación
                                info_ubicacion,
                                
                                # Horario de atención
                                horario_atencion,
                                
                                # Instrucciones adicionales
                                instrucciones,
                                
                                # Botón para contactar
                                ft.Container(
                                    ft.ElevatedButton(
                                        "CONTACTAR",
                                        on_click=lambda e: self.page.go("/contacto"),
                                        style=ft.ButtonStyle(
                                            bgcolor=ft.Colors.AMBER_200,
                                            color=ft.Colors.BLACK,
                                            padding=ft.padding.symmetric(horizontal=40, vertical=20)
                                        ),
                                        icon=ft.Icons.CHAT,
                                        icon_color=ft.Colors.BLACK
                                    ),
                                    margin=ft.margin.only(top=30, bottom=40)
                                )
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