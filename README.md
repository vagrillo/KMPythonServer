# KMPythonServer
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Flask](https://img.shields.io/badge/flask-2.0%2B-lightgrey)

An advanced Python server for remote mouse control via a web interface, combining desktop automation and network functionality.

All made by AI (_DeepSeek R1_) !

## ✨ Key Features

### **Advanced Local Control**
- Drawing geometric shapes (circles)
- Smooth pointer movement
- Single and double clicks
- Drag-and-drop functionality
- Long press clicks
- Support for left/right mouse buttons

### **Remote Control via Web**
- Full-screen black interface
- Precise mouse movement tracking
- Real-time click/double-click detection
- Multi-browser support
- Remote dragging
- Automatic coordinate conversion
- RESTful API for integrations

## 🚀 Installation

**Prerequisites:**
- Python 3.7+
- Pip package manager

**Steps:**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/KMPythonServer.git
   cd KMPythonServer


2. Install dependencies:
   ```bash
   pip install pyautogui flask


3. Run the script:
   ```bash
   python km_python_server.py


## 🖥️ Usage

### Basic Mode

python km_python_server.py
-   Draws a circle on the screen
-   Moves the mouse to the center
-   Performs an automatic click
    

### Server Mode

python km_python_server.py --server
-   Starts the HTTP server on port 8071
-   Accessible via browser at  `http://localhost:8071`
    

### Advanced Options

bash

Copy

# Change server port
python km_python_server.py --port 8080

# Disable graphical features
python km_python_server.py --headless


## 🛠️ Architecture and Components

### Technology Stack
-   **Core Engine**: PyAutoGUI for mouse control
-   **Web Server**: Flask for REST API
-   **Frontend**: HTML5/CSS3/JavaScript for web interface
-   **Concurrency**: Threading for async I/O
    

#
## 🔒 Security Considerations
1.  **Firewall**: Ensure port 8071 is open
2.  **Authentication**: Add security layers for production use
3.  **CORS**: Configure properly for cross-domain access
4.  **Fail-Safe**: Disabled to allow absolute movements

**Important**: Do not use in untrusted environments without proper authentication mechanisms.

    

## 📚 Acknowledgments
-   PyAutoGUI development team
-   Flask community
-   PEP8 standards for code guidelines
    

 
