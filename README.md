# SEPA Data

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
```

## Usage

# Prerequisites:

- Python 3.7+
- Dependencies will be listed in `requirements.txt` (There is no dependencies yet)

# Instructions:

1. Clone the repository.
2. Install the dependencies.
3. Download the ZIP file from the government website and place it in the `resources/raw/compressed` folder.
4. Run the main script: `python main.py`.

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