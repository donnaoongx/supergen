# SuperGen

SuperGen is a Python-based utility designed to automatically detect and clear unused files and applications on Windows devices, helping you free up valuable disk space.

## Features

- Scans specified directories (e.g., Downloads folder) for unused files and deletes them.
- Identifies and terminates unused applications running in the background.

## Requirements

- Python 3.x
- `psutil` package

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the required package:
   ```bash
   pip install psutil
   ```

## Usage

1. Download or clone this repository.
2. Run the program using the following command in your terminal or command prompt:
   ```bash
   python supergen.py
   ```
3. The program will scan for unused files in the specified directory and unused applications, and will attempt to clear them.

## Customization

- Modify the `directory_to_clean` variable in `supergen.py` to change the directory being scanned for unused files.
- Change the `days_unused` parameter in the functions to set the threshold for considering files and applications as unused.

## Notes

- This tool is intended for use on Windows systems.
- Administrator privileges may be required to terminate certain applications.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.