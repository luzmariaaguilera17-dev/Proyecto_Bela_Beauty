import flet as ft

def CatalogoView():
    imagenes = [
        "assets/foto1.jpg",
        "assets/foto2.jpg",
        "assets/foto3.jpg",
    ]

    index = ft.Ref[int]()
    index.current = 0

    img = ft.Image(src=imagenes[index.current], width=400, height=300, fit=ft.ImageFit.COVER)

    def anterior(e):
        index.current = (index.current - 1) % len(imagenes)
        img.src = imagenes[index.current]
        img.update()

    def siguiente(e):
        index.current = (index.current + 1) % len(imagenes)
        img.src = imagenes[index.current]
        img.update()

    return ft.Column(
        [
            ft.Text("Catálogo de Trabajos", size=28, weight="bold", color="#ff8c42"),
            img,
            ft.Row(
                [
                    ft.ElevatedButton("Anterior", on_click=anterior, bgcolor="#ff8c42", color="white"),
                    ft.ElevatedButton("Siguiente", on_click=siguiente, bgcolor="#ff8c42", color="white"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
    )
