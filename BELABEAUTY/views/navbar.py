import flet as ft

class NavBar(ft.Container):
    # Variable de clase para almacenar la ruta activa
    active_route = "/"
    
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        # Actualizar la ruta activa con la ruta actual de la página
        NavBar.active_route = page.route
        self.build_navbar()
    
    def navigate_to(self, e, route):
        """Función para navegar a diferentes vistas"""
        # Actualizar la ruta activa en la variable de clase
        NavBar.active_route = route
        self.page.go(route)
        # No es necesario llamar a build_navbar aquí porque se creará una nueva barra
    
    def build_navbar(self):
        # Usar la ruta activa de la variable de clase
        current_route = NavBar.active_route
        
        # Función para crear un elemento de navegación completo
        def create_nav_item(text, route):
            is_active = current_route == route
            
            return ft.Column(
                controls=[
                    # Botón de navegación
                    ft.ElevatedButton(
                        text,
                        on_click=lambda e: self.navigate_to(e, route),
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.AMBER_300 if is_active else ft.Colors.AMBER_100,
                            color=ft.Colors.BLACK,
                            elevation=3 if is_active else 1,
                            shape=ft.RoundedRectangleBorder(radius=8),
                            padding=ft.padding.symmetric(horizontal=25, vertical=12),
                        ),
                    ),
                    # Barra amarilla indicadora (solo visible en vista activa)
                    ft.Container(
                        width=80 if is_active else 0,
                        height=4,
                        bgcolor=ft.Colors.AMBER_600 if is_active else ft.Colors.TRANSPARENT,
                        border_radius=2,
                    )
                ],
                spacing=5,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            )
        
        # Crear botones de navegación
        nav_row = ft.Row(
            controls=[
                create_nav_item("Inicio", "/"),
                create_nav_item("Servicios", "/servicios"),
                create_nav_item("Horarios", "/horarios"),
                create_nav_item("Contacto", "/contacto"),
                create_nav_item("Ubicación", "/ubicacion")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=30,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
        # Configurar el contenedor de la barra de navegación
        self.content = nav_row
        self.bgcolor = ft.Colors.AMBER_50
        self.padding = ft.padding.symmetric(vertical=15, horizontal=20)
        self.border_radius = 10
        self.margin = ft.margin.only(bottom=20)