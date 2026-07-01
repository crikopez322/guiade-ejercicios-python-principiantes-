reservadas = {"if", "for", "while", "def", "class", "return", "import"}
identificadores = ["variable", "for", "funcion", "if", "dato"]
encontradas = [id for id in identificadores if id in reservadas]
if encontradas:
    print(f"Se encontraron palabras reservadas: {encontradas}")
else:
    print("No se encontraron palabras reservadas.")