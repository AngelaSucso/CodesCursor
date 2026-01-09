import sys
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    description="Organiza archivos en carpetas según su tipo."
)

parser.add_argument(
    "-d", "--directorio",
    type=str,
    default=str(Path(__file__).parent / "Downloads"),
    help="Ruta a la carpeta objetivo"
)

args = parser.parse_args()
carpeta_objetivo = Path(args.directorio)

if not carpeta_objetivo.exists():
    print(f"Error: la carpeta '{carpeta_objetivo}' no existe.")
    sys.exit(1)
print(f"Organizando archivos en: {carpeta_objetivo}\n")


categorias = {
    "Imagenes": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Musica": [".mp3", ".wav"],
}
categorias_predeterminadas = ["Otros"]  # donde irá lo que no encaje en las anteriores

extension_a_categoria = {}
for categoria, exts in categorias.items():
    for ext in exts:
        extension_a_categoria[ext.lower()] = categoria

archivos = [f for f in carpeta_objetivo.iterdir() if f.is_file()]
for archivo in archivos:
    ext = archivo.suffix.lower()
    categoria = extension_a_categoria.get(ext, "Otros")
    destino_dir = carpeta_objetivo / categoria
    destino_dir.mkdir(exist_ok=True)
    archivo.rename(destino_dir / archivo.name)

    print(f"Movido {archivo.name} a {categoria}/")

print("\nOrganización finalizada.")