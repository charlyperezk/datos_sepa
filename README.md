# Datos SEPA

## Description

This project focuses on processing and preparing price data from Argentine businesses for further analysis. 
The data comes from an Argentine government website that publishes a ZIP file daily with information on 
the prices of various businesses. The main goal is to transform this raw data into a format suitable 
for analysis, in this case, CSV files.

### Data Source: https://datos.gob.ar/dataset/produccion-precios-claros---base-sepa

## Features

- Functional Approach: The project adopts a functional approach, using pure functions and breaking down the 
  problem into independent, reusable steps.
- ETL Processing: An Extract, Transform, Load (ETL) process is implemented to manage the data.
- Bash Scripts: Bash scripts are used to decompress the ZIP file and unify the CSV files.
- Flexible Configuration: The project configuration, such as file paths and transformation functions, 
  is managed in a centralized and flexible way.

## Project Structure

```
└── ./
    └── src
        ├── config
        │   ├── __init__.py
        │   └── project_config.py
        ├── etl
        │   ├── bash_scripts
        │   │   ├── decompress_process.sh
        │   │   └── unify.sh
        │   ├── __init__.py
        │   ├── config.py
        │   ├── etl.py
        │   ├── extract.py
        │   ├── line.py
        │   └── transform.py
        ├── utils
        │   └── decorators.py
        └── main.py
    └── logs
        └── app.log
    └── resources
        └── raw
            └── compressed
                └── .zip
            └── decompressed
                └── .csv
        └── processed
            └── .csv
    └── venv/
```

## Usage

# Prerequisites:

- Python 3.7+
- Dependencies will be listed in `requirements.txt` (There is no dependencies yet)

# Instructions:

1. Clone the repository.
2. Install the dependencies.
3. Create the project structure executing `python src/main.py --create-dirs`
4. Download the ZIP file from the government website and place it in the `resources/raw/compressed` folder.
5. Run the bash scripts: `bash decompress_process.sh` and `bash unify.sh`.
6. Run the main script: `python src/main.py --process-all` or `python src/main.py --configs comercio` or `python src/main.py --configs sucursales` or `python src/main.py --configs productos`.
7. Clean the raw data: `python src/main.py --clean-raw-data compressed` or `python src/main.py --clean-raw-data decompressed` or `python src/main.py --clean-raw-data compressed decompressed`.

## Implementation Details

- Extraction: The `SepaExtract` class handles reading CSV files [1].
- Transformation: The `Transform` class applies transformation and filtering functions to the file lines [2, 3].
- Load: The `SepaETL` class saves the processed data into CSV files [4].

## Next Steps

- Implement unit tests to ensure code quality.
- Add detailed documentation to classes and functions.
- Explore options to automate data download.
- Make an API available for data analysis.
- Save the data delta between dates for trend analysis.
- Dockerize the project.

## Contributions

Contributions are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

# Frequently Asked Questions

## About the SEPA Data Processing Project

1. **How are the paths to directories and files managed within the project?**
   The `ProjectDirs` class in `project_config.py` defines and creates paths to important directories such as `resources`, `raw_data`, `processed_data`, `logs`, etc. These paths are used throughout the project to access necessary files and directories.

2. **What is the purpose of the bash scripts `decompress_process.sh` and `unify.sh`?**
   - `decompress_process.sh`: Decompresses the ZIP files containing the input data. First, it decompresses the initial ZIP file and then any nested ZIP files, creating an organized directory structure.
   - `unify.sh`: Combines individual CSV files (`comercio.csv`, `productos.csv`, `sucursales.csv`) found in the decompressed directories into a single CSV file per type.

3. **How is the ETL process configured for different types of data (stores, branches, products)?**
   The `ComerciosConfig`, `SucursalesConfig`, and `ProductosConfig` classes in `etl/config.py` define specific configurations for each type of data. This includes the source file path, destination file path, transformation functions, and filter functions.

4. **How is data extraction performed in the project?**
   The `SepaExtract` class in `etl/extract.py` is responsible for reading data from CSV files. It uses UTF-8 encoding and returns a list of `Line` objects, which represent each line of the file.

5. **What types of transformations can be applied to the data?**
   The `Transform` class in `etl/transform.py` provides methods to apply transformations to the data, such as converting to uppercase (`upper()`) using lambda functions.

6. **How is data filtered during the ETL process?**
   The filter functions, defined as lambda functions in the configuration classes, are used to determine which lines of data should be processed. For example, you can filter by the number of fields or whether a line is empty.

7. **How are important actions and events logged during project execution?**
   The project uses Python's `logging` module to log debugging information to the `app.log` file inside the `logs` directory. This helps with identifying and resolving issues during the ETL process execution.