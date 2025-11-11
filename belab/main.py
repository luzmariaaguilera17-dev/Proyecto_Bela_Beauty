import flet as ft
from views.home_view import HomeView
from views.servicios_view import ServiciosView
from views.contacto_view import ContactoView
from views.catalogo_view import CatalogoView
from views.navbar import NavBar


def main(page: ft.Page):
    page.title = "Bela Beauty Salon"
    page.window_width = 900
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.bgcolor = "#fff9f5"  # Naranja muy suave

    contenido = ft.Container(expand=True, padding=30)

    def mostrar_pantalla(pantalla):
        if pantalla == "inicio":
            contenido.content = HomeView(mostrar_pantalla)
        elif pantalla == "servicios":
            contenido.content = ServiciosView()
        elif pantalla == "contacto":
            contenido.content = ContactoView()
        elif pantalla == "catalogo":
            contenido.content = CatalogoView()
        page.update()

    navbar = NavBar(mostrar_pantalla)
    page.add(ft.Column([navbar, contenido], expand=True))

    mostrar_pantalla("inicio")


ft.app(target=main)
