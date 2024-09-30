#!/bin/bash

# Define the directory where the folders resulting from the last decompression are located
result_dir="../../../resources/raw/decompressed"

# Define the output CSV files
output_comercio="../../../resources/raw/decompressed/comercio.csv"
output_productos="../../../resources/raw/decompressed/productos.csv"
output_sucursales="../../../resources/raw/decompressed/sucursales.csv"

# Remove output files if they already exist
rm -f "$output_comercio" "$output_productos" "$output_sucursales"

# Iterate over each folder in the results directory
for dir in "$result_dir"/*; do
    if [ -d "$dir" ]; then
        echo "Processing directory: $dir"
        
        # Process comercio.csv
        if [ -f "$dir/comercio.csv" ]; then
            echo "  Adding comercio.csv from $dir"
            # Ensure the file ends with a new line
            sed -i '$a\' "$dir/comercio.csv"  # Add a new line if there isn't one
            if [ ! -s "$output_comercio" ]; then
                head -n 1 "$dir/comercio.csv" > "$output_comercio"  # Add header
            fi
            tail -n +2 "$dir/comercio.csv" >> "$output_comercio"  # Add content without header
        fi
        
        # Process productos.csv
        if [ -f "$dir/productos.csv" ]; then
            echo "  Adding productos.csv from $dir"
            # Ensure the file ends with a new line
            sed -i '$a\' "$dir/productos.csv"  # Add a new line if there isn't one
            if [ ! -s "$output_productos" ]; then
                head -n 1 "$dir/productos.csv" > "$output_productos"  # Add header
            fi
            tail -n +2 "$dir/productos.csv" >> "$output_productos"  # Add content without header
        fi
        
        # Process sucursales.csv
        if [ -f "$dir/sucursales.csv" ]; then
            echo "  Adding sucursales.csv from $dir"
            # Ensure the file ends with a new line
            sed -i '$a\' "$dir/sucursales.csv"  # Add a new line if there isn't one
            if [ ! -s "$output_sucursales" ]; then
                head -n 1 "$dir/sucursales.csv" > "$output_sucursales"  # Add header
            fi
            tail -n +2 "$dir/sucursales.csv" >> "$output_sucursales"  # Add content without header
        fi
    fi
done

echo "All CSV files have been merged into their respective files:"
echo "- Comercio: $output_comercio"
echo "- Productos: $output_productos"
echo "- Sucursales: $output_sucursales"

