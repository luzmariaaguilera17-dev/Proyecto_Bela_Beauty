import flet as ft
from views.home_view import HomeView
from views.servicios_view import ServiciosView
from views.contacto_view import ContactoView
from views.navbar import NavBar


def main(page: ft.Page):
    page.title = "Bela Beauty Salon"
    page.window_width = 900
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.bgcolor = "#f8f8f8"

    # Contenedor de contenido dinámico
    contenido = ft.Container(expand=True, padding=30)

    # --------- Función de navegación ----------
    def mostrar_pantalla(pantalla):
        if pantalla == "inicio":
            contenido.content = HomeView(mostrar_pantalla)
        elif pantalla == "servicios":
            contenido.content = ServiciosView()
        elif pantalla == "contacto":
            contenido.content = ContactoView()
        page.update()

    # Crear barra de navegación
    navbar = NavBar(mostrar_pantalla)

    # Estructura principal
    page.add(
        ft.Column(
            controls=[navbar, contenido],
            expand=True,
        )
    )

    # Mostrar la vista inicial
    mostrar_pantalla("inicio")


ft.app(target=main)
rget=main
