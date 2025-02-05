# FAKE DATA GEN 

[English](README.md) | [Русский](READ_RU.md) | [한국어](READ_KO.md) | [中文](READ_CN.md)

**FAKE DATA GEN** - Fake data generator using Faker library.  
**Version:** 1.0 🚀  
**Author:** k1y0miiii (◕‿◕)

---

## Overview 📌

FAKE DATA GEN is a command-line tool that generates fake data using the [Faker](https://github.com/joke2k/faker) library. It supports multiple languages for both the user interface and the generated data, and it features a stylish banner rendered with [pyfiglet](https://github.com/pwaller/pyfiglet) along with colored output via [colorama](https://github.com/tartley/colorama).

---

## Features ✨

- **🌍 Multilingual Interface:**  
  Supports Russian, English, Chinese, Korean, and more.
- **📊 Diverse Data Fields:**  
  Generate various types of fake data such as full names, phone numbers, addresses, etc.
- **📂 Flexible Export Options:**  
  Export generated data in CSV, TXT, and various SQL formats (MySQL, SQLite, PostgreSQL).
- **🎨 Dynamic Menu Display:**  
  A styled, colorful menu that adapts to the chosen language.
- **📡 IP-based Language Detection:**  
  Automatically detects your location via IP to select the default language, with a manual fallback.
- **❌ Easy Exit:**  
  At any prompt, enter `-q` to exit the program and close the console (where supported).

---

## Installation 🛠️

### Prerequisites

- **🐍 Python 3.6+**
- **📦 pip** (Python package installer)

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/k1y0miiii/Fake-data-gen.git
cd fake-data-gen
```

### Install Dependencies

Install the required dependencies using pip and the provided requirements.txt file:

```bash
pip install -r requirements.txt
```

A sample `requirements.txt` might include:

```
Faker>=13.0.0
pyfiglet>=0.8.post1
colorama>=0.4.4
wcwidth>=0.2.5
requests>=2.25.1
```

---

## Usage 🚀

Run the program via the command line:

```bash
python data_gen.py
```

### How It Works ⚙️

1. **🌍 Language Detection:**  
   The program attempts to detect your location using your IP address to select the appropriate language for the menu. If detection fails, you'll be prompted to choose a language manually.
2. **📜 Interactive Menu:**  
   A styled menu will display various options for data fields. Select the fields you want to generate.
3. **🛠️ Data Generation:**  
   After selecting the fields and specifying the number of records, the program generates fake data accordingly.
4. **💾 Data Export:**  
   You can choose to export the generated data in your preferred format (CSV, TXT, or SQL). The exported file will be saved on your Desktop inside a folder named `gen_data`.
5. **🚪 Exiting the Program:**  
   At any prompt, you can enter `-q` to exit the program. On supported systems (especially when launched as a standalone executable), the console window will close automatically upon exit.

---

## Building an Executable 🏗️

You can package FAKE DATA GEN into a standalone executable using PyInstaller.

### Step 1. Install PyInstaller

```bash
pip install pyinstaller
```

### Step 2. Create a PyInstaller Hook for pyfiglet

Create a file named `hook-pyfiglet.py` in your project directory (the same folder as `data_gen.py`) with the following content:

```python
from PyInstaller.utils.hooks import collect_data_files
datas = collect_data_files('pyfiglet')
```

### Step 3. Build the Executable

Run PyInstaller with the additional hooks directory specified:

```bash
pyinstaller --onefile --additional-hooks-dir=. data_gen.py
```

This command will generate a single executable file in the `dist` folder.

---

## Release 📦

The compiled executable and source code will be available under the Releases section of this repository.

---

## License 📜

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributing 🤝

Contributions are welcome! If you have ideas for improvements or find bugs, please open an issue or submit a pull request.

---

## Author ✍️

**k1y0miiii** (◕‿◕)

🎉 Happy data generating! 🚀

