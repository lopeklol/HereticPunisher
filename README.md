# Project: Heretic Punisher

# InquisitionExecutor

**Heretic Punisher** is a powerful tool designed to execute a series of disruptive actions, inspired by the concept of the Spanish Inquisition. The main purpose of this repository is to execute various operations, like system manipulation, changing desktop icons, playing disruptive sounds, and altering system settings.

**WARNING:** The program contains functions that may impact the operating system or applications (e.g., changing settings, stopping processes, modifying system files). **I am not responsible for any damage caused by using this program**. Use it at your own risk.

## Features

- Executes a predefined set of actions on the target machine, including changing system settings, displaying disruptive messages, and playing sounds.
- Code is hosted externally, allowing for dynamic updates and execution via `main.py` or `main.exe`.
- Includes a stop mechanism (`stop.py` or `stop.exe`) to halt the execution of operations.

## Files in this repository:

1. **main.py** / **main.exe**: This file will download and execute the `code.py` script from an online source.
2. **code.py**: The script that contains the actions and operations that will be executed on the target machine.
3. **stop.py** / **stop.exe**: Used to stop the execution of operations initiated by `main.py`/`main.exe`.
4. **README.md**: Documentation for setting up and understanding the project.
5. **requirements.txt**: Contains the necessary dependencies to run the project.

## How to Use

1. **Clone the repository** or download the files.
2. **Install the necessary dependencies**:
   - Run `pip install -r requirements.txt` to install all required libraries.
3. **Run the main file**:
   - Execute `main.py` or the compiled `main.exe` to start executing the predefined actions from the code.
   - The code will download the `code.py` file from the repository and run it.
4. **Stop the execution**:
   - To stop the running operations, use the `stop.py` or `stop.exe` file.

## Requirements

- Python 3.x
- `requests`
- `plyer`
- `pygame`
- `pyvolume`
- `psutil`
- `pythoncom`
- `win32com.client`

## Disclaimer

- This repository is intended for educational and personal use only. **Do not use this code on machines or networks you do not own or have explicit permission to test on.**
- Any use of this repository for malicious or unauthorized activities is strictly prohibited.
- Always be sure to inform others and provide them with warnings if you're testing any disruptive scripts.
