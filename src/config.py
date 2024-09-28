import os
from transform.line_parser import ComerciosParser, ProductosParser, SucursalesParser


# Paths
paths = {
    "gross": r"C:\Users\CPKSoft\Desktop\proyectos\sepa_project\resources\gross",
    "combined": r"C:\Users\CPKSoft\Desktop\proyectos\sepa_project\resources\gross\combined",
    "extracted": r"C:\Users\CPKSoft\Desktop\proyectos\sepa_project\resources\gross\compressed",
    "decompressed": r"C:\Users\CPKSoft\Desktop\proyectos\sepa_project\resources\gross\decompressed",
    "transformed": r"C:\Users\CPKSoft\Desktop\proyectos\sepa_project\resources\transformed"
}


# File names
transform_config = {
    "comercio": {
        "filename": "comercio.csv",
        "parser": ComerciosParser
    },
    "productos": {
        "filename": "productos.csv",
        "parser": ProductosParser
    },
    "sucursales": {
        "filename": "sucursales.csv",
        "parser": SucursalesParser
    }
}

# Create directories
def create_directories():
    list(map(lambda path: os.makedirs(path, exist_ok=True), paths.values()))

