#!/bin/bash

# Define el directorio donde están las carpetas resultantes de la última descompresión
result_dir="../../../resources/raw/decompressed"

# Define los archivos CSV de salida
output_comercio="../../../resources/raw/decompressed/comercio.csv"
output_productos="../../../resources/raw/decompressed/productos.csv"
output_sucursales="../../../resources/raw/decompressed/sucursales.csv"

# Elimina los archivos de salida si ya existen
rm -f "$output_comercio" "$output_productos" "$output_sucursales"

# Itera sobre cada carpeta en el directorio de resultados
for dir in "$result_dir"/*; do
    if [ -d "$dir" ]; then
        echo "Processing directory: $dir"
        
        # Procesar comercio.csv
        if [ -f "$dir/comercio.csv" ]; then
            echo "  Adding comercio.csv from $dir"
            # Asegurarse de que el archivo termine con una nueva línea
            sed -i '$a\' "$dir/comercio.csv"  # Añade una nueva línea si no hay
            if [ ! -s "$output_comercio" ]; then
                head -n 1 "$dir/comercio.csv" > "$output_comercio"  # Añadir cabecera
            fi
            tail -n +2 "$dir/comercio.csv" >> "$output_comercio"  # Añadir contenido sin cabecera
        fi
        
        # Procesar productos.csv
        if [ -f "$dir/productos.csv" ]; then
            echo "  Adding productos.csv from $dir"
            # Asegurarse de que el archivo termine con una nueva línea
            sed -i '$a\' "$dir/productos.csv"  # Añade una nueva línea si no hay
            if [ ! -s "$output_productos" ]; then
                head -n 1 "$dir/productos.csv" > "$output_productos"  # Añadir cabecera
            fi
            tail -n +2 "$dir/productos.csv" >> "$output_productos"  # Añadir contenido sin cabecera
        fi
        
        # Procesar sucursales.csv
        if [ -f "$dir/sucursales.csv" ]; then
            echo "  Adding sucursales.csv from $dir"
            # Asegurarse de que el archivo termine con una nueva línea
            sed -i '$a\' "$dir/sucursales.csv"  # Añade una nueva línea si no hay
            if [ ! -s "$output_sucursales" ]; then
                head -n 1 "$dir/sucursales.csv" > "$output_sucursales"  # Añadir cabecera
            fi
            tail -n +2 "$dir/sucursales.csv" >> "$output_sucursales"  # Añadir contenido sin cabecera
        fi
    fi
done

echo "All CSV files have been merged into their respective files:"
echo "- Comercio: $output_comercio"
echo "- Productos: $output_productos"
echo "- Sucursales: $output_sucursales"

