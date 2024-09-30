#!/bin/bash

# Get the current directory
current_dir=$(pwd)

# Define the output directory where the final results will be stored
output_dir="../../../resources/raw/decompressed"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

# Unzip the initial ZIP file (this step will only keep the first ZIP original)
zip_pattern="../../../resources/raw/compressed/sepa_*.zip"
for zip_file in $zip_pattern; do
    if [ -f "$zip_file" ]; then
        echo "Decompressing file: $zip_file"
        unzip "$zip_file" -d "$output_dir"
        
        # Check if the unzip was successful
        if [ $? -eq 0 ]; then
            echo "Decompression successful for $zip_file."
        else
            echo "An error occurred during decompression of $zip_file."
            exit 1
        fi
    fi
done

# Now process all ZIP files that were extracted into the output directory (decompress them)
echo "Looking for ZIP files inside $output_dir to decompress..."
for nested_zip in "$output_dir"/*.zip; do
    if [ -f "$nested_zip" ]; then
        echo "Decompressing nested ZIP file: $nested_zip"
        
        # Create a directory for each nested zip (use the file name minus the extension)
        nested_output_dir="${nested_zip%.zip}"
        mkdir -p "$nested_output_dir"
        
        # Unzip the nested ZIP file into its own directory
        unzip "$nested_zip" -d "$nested_output_dir"

        # Check if the unzip was successful
        if [ $? -eq 0 ]; then
            echo "Decompression successful for $nested_zip. Files extracted to $nested_output_dir"
            # Remove the nested zip file after successful decompression
            rm "$nested_zip"
            echo "Deleted $nested_zip after decompression."
        else
            echo "An error occurred during decompression of $nested_zip."
            exit 1
        fi
    else
        echo "No nested ZIP files found in $output_dir."
    fi
done

# Optionally, delete the original ZIP files if they are no longer needed
# Uncomment the following lines if you want to delete them
# for zip_file in $zip_pattern; do
#     if [ -f "$zip_file" ]; then
#         rm "$zip_file"
#         echo "Deleted original ZIP file: $zip_file."
#     fi
# done