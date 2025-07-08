<div align="center">
<img src="https://github.com/eugenio-jefferson/DVR-Viewer/blob/develop/assets/icon.png?raw=true">
<br>
<a href="https://github.com/eugenio-jefferson/DVR-Viewer/releases">
<img src="https://img.shields.io/github/v/release/eugenio-jefferson/DVR-Viewer?label=Latest%20Release&style=for-the-badge" alt="Latest Release">
</a>
<img src="https://img.shields.io/github/repo-size/eugenio-jefferson/DVR-Viewer?style=for-the-badge" alt="Repo Size">
<img src="https://img.shields.io/github/languages/count/eugenio-jefferson/DVR-Viewer?style=for-the-badge" alt="Language Count">
<img src="https://img.shields.io/github/issues/eugenio-jefferson/DVR-Viewer?style=for-the-badge" alt="Issues">
<img src="https://img.shields.io/github/license/eugenio-jefferson/DVR-Viewer?style=for-the-badge" alt="License">
</div>

<br>


# DVR Viewer

An open-source utility to facilitate the viewing of security cameras through the Intelbras DVR website.

DVR Viewer is a project designed to simplify and automate access to Intelbras security camera systems. Instead of manually navigating the website and repeatedly entering credentials, this application provides a simple interface that launches and displays the cameras quickly and directly.

The main goal is to offer a more fluid and efficient user experience for daily monitoring.


## 📚 Table of Contents

- [Prerequisites](#-prerequisites)
- [Installing DVR Viewer](#-installing-dvr-viewer)
- [Using DVR Viewer](#-using-dvr-viewer)
- [For Developers](#-for-developers)
    - [Project Structure](#️-project-structure)
    - [Compiling from Source](#-compiling-from-source)
        - [Prerequisites for compilation](#️-prerequisites-for-compilation)
        - [Compilation Steps](#compilation-steps)
- [License](#-license)


## 💻 Prerequisites
Before you begin, ensure you have met the following requirements:

- You have a compatible <Windows / Linux> machine.

- No special dependencies are required for end-users.


## 🚀 Installing DVR Viewer
To install DVR Viewer, follow these steps:

1. Go to the project's [**Releases**](hhttps://github.com/eugenio-jefferson/DVR-Viewer/releases) page.

2. Download the executable file corresponding to your operating system (Windows or Linux).

3. Run the downloaded file. On the first run, the application will set itself up and create a shortcut in your system's application menu.


## 🎥 Using DVR Viewer
To use DVR Viewer, **simply run the application from the shortcut created on your computer** during the first execution. The program will handle the automation, and you just need to wait for the camera feed to be displayed.


## 🧑‍💻 For Developers
This section contains information for those who wish to contribute, modify, or compile the project from the source code.

### 🗃️ Project Structure

The project's file and folder structure is organized as follows:

```
DVR-Viewer
├── assets
│   ├── icon.png
│   └── icon.ico
│
├── src
│   ├── core
│   │   ├── automation.py
│   │   └── dvr_viewer.py
│   │
│   ├── gui
│   │   └── gui_manager.py
│   │
│   ├── services
│   │   ├── credentials_manager.py
│   │   ├── configuration_manager.py
│   │   └── shortcut_creator.py
│   │
│   └── __init__.py
│
├── LICENSE
├── main.py
├── requirements_linux.txt
├── requirements_windows.txt
└── README.md
```

---


### 💽 Compiling from Source
To compile DVR Viewer, follow the steps below corresponding to your operating system.


#### 🛠️ Prerequisites for compilation

| Platform | System Packages / Tools |
| --- | --- |
| **Debian/Ubuntu** | `sudo apt update && sudo apt install python3-dev build-essential` |
| **Windows** | **Visual Studio Community** with the **"Desktop development with C++"** workload. |

Also install:

- **Python ≥ 3.10**

---

#### Compilation Steps

1. **Clone the repository:**
  
  ```
  git clone https://github.com/eugenio-jefferson/DVR-Viewer.git
  cd DVR-Viewer
  ```
  
2. **Create and activate a virtual environment (Recommended):**
  
  ```
  python -m venv venv
  
  # On Windows:
  .\venv\Scripts\activate
  
  # On Linux:
  source venv/bin/activate
  ```
  
3. **Install the dependencies:**
  
  - **On Linux:**
    
    ```
    pip install -r requirements-linux.txt
    ```
  
  - **On Windows:**
    
    ```
    pip install -r requirements-windows.txt
    ```
    
4. **Run the Nuitka compilation command:**
  
  - **On Linux:**
    
    ```
    nuitka --onefile --include-data-dir=assets=assets main.py -o DVR-Viewer
    ```
    
  - **On Windows:**
    
    ```
    nuitka --onefile --include-data-dir=assets=assets --enable-plugin=tk-inter --windows-console-mode=disable --windows-product-name="DVR Viewer" --windows-icon-from-ico=assets/icone.ico main.py -o DVR-Viewer
    ```
    
After compilation, the final executable will be the `./DVR-Viewer`.

---

## 📝 License

Made by [**Eugênio Jefferson**](https://github.com/eugenio-jefferson).

This project is licensed under the **MIT License**. See the [`LICENSE`](https://github.com/eugenio-jefferson/DVR-Viewer/blob/develop/LICENSE) file for more details.