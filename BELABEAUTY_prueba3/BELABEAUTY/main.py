import flet as ft
from db import inicializar_bd, get_rol_usuario
from login import login_view
from views.home_view import HomeView
from views.presentacion_view import PresentacionView
from views.servicios_view import ServiciosView
from views.horarios_view import HorariosView
from views.contacto_view import ContactoView
from views.ubicacion_view import UbicacionView


def main(page: ft.Page):
    page.title = "Bela Beauty Salon"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_maximized = True
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    page.assets_dir = "assets"

    inicializar_bd()

    # --- Vistas principales ---
    views = {
        "/": HomeView(page),
        "/presentacion": PresentacionView(page),
        "/servicios": ServiciosView(page),
        "/horarios": HorariosView(page),
        "/contacto": ContactoView(page),
        "/ubicacion": UbicacionView(page)
    }

    # --- Función para volver al login ---
    def volver_login(e=None):
        page.on_route_change = lambda x: None  # Desactivar manejador de rutas
        page.views.clear()
        page.go("/login")
        page.views.append(login_view(page, mostrar_vistas))
        page.update()

    # --- Función para mostrar vistas tras login ---
    def mostrar_vistas(usuario):
        rol = get_rol_usuario(usuario)

        # Barra superior con botón Cerrar sesión
        def barra_superior():
            btn_cerrar_sesion = ft.ElevatedButton(
                text="Cerrar sesión",
                bgcolor=ft.Colors.RED_400,
                color=ft.Colors.WHITE,
                on_click=volver_login
            )
            return ft.Row(
                controls=[
                    ft.Text(
                        f"Bienvenido, {usuario}",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK
                    ),
                    ft.Container(expand=True),
                    btn_cerrar_sesion
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )

        # Manejar cambios de ruta
        def route_change(e: ft.RouteChangeEvent):
            route = e.route
            page.views.clear()

            vista_actual = views.get(route, views["/"])

            if isinstance(vista_actual, ft.View):
                controles = [barra_superior()] + vista_actual.controls
            else:
                controles = [barra_superior(), vista_actual]

            nueva_vista = ft.View(
                route=route,
                controls=controles,
                scroll=ft.ScrollMode.AUTO
            )
            
            page.views.append(nueva_vista)
            page.update()

        page.on_route_change = route_change
        page.go("/")  # ruta inicial tras login

    # --- Configurar login ---
    page.views.clear()
    page.on_route_change = lambda e: None  # desactivar temporalmente la ruta
    page.go("/login")
    page.views.append(login_view(page, mostrar_vistas))
    page.update()


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
