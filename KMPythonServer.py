import pyautogui
import math
import sys
import time
import threading
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)
pyautogui.FAILSAFE = False

# Parte originale dello script
def move_mouse(x, y, duration=0.25):
    pyautogui.moveTo(x, y, duration=duration)

def click_single(button='left'):
    pyautogui.click(button=button)

def click_double(button='left'):
    pyautogui.doubleClick(button=button)

def drag(start_x, start_y, end_x, end_y, button='left', duration=0.5):
    move_mouse(start_x, start_y)
    pyautogui.mouseDown(button=button)
    move_mouse(end_x, end_y, duration)
    pyautogui.mouseUp(button=button)

def long_click(x, y, button='left', hold_duration=1.0):
    move_mouse(x, y)
    pyautogui.mouseDown(button=button)
    time.sleep(hold_duration)
    pyautogui.mouseUp(button=button)

def draw_circle():
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    radius = 100
    
    num_points = 50
    for i in range(num_points + 1):
        angle = 2 * math.pi * i / num_points
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        move_mouse(x, y, duration=0.05)
    
    move_mouse(center_x, center_y)
    click_single()

# Parte server HTTP
@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Remote Mouse</title>
        <style>
            body { margin: 0; overflow: hidden; background: black; }
            #overlay { width: 100vw; height: 100vh; cursor: none; }
        </style>
    </head>
    <body>
        <div id="overlay"></div>
        <script>
            const overlay = document.getElementById('overlay');
            
            function sendMove(x, y) {
                const xPercent = (x / window.innerWidth) * 100;
                const yPercent = (y / window.innerHeight) * 100;
                fetch('/move', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ x: xPercent, y: yPercent })
                });
            }

            overlay.addEventListener('mousemove', (e) => {
                sendMove(e.clientX, e.clientY);
            });

            overlay.addEventListener('mousedown', (e) => {
                const button = e.button === 2 ? 'right' : 'left';
                fetch('/mouse_down', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ button: button })
                });
            });

            overlay.addEventListener('mouseup', (e) => {
                const button = e.button === 2 ? 'right' : 'left';
                fetch('/mouse_up', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ button: button })
                });
            });

            overlay.addEventListener('dblclick', (e) => {
                const button = e.button === 2 ? 'right' : 'left';
                fetch('/double_click', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ button: button })
                });
            });
        </script>
    </body>
    </html>
    """

@app.route('/move', methods=['POST'])
def handle_move():
    data = request.json
    screen_width, screen_height = pyautogui.size()
    x = (data['x'] / 100) * screen_width
    y = (data['y'] / 100) * screen_height
    move_mouse(x, y, duration=0)
    return jsonify(status='success')

@app.route('/mouse_down', methods=['POST'])
def handle_mouse_down():
    data = request.json
    pyautogui.mouseDown(button=data.get('button', 'left'))
    return jsonify(status='success')

@app.route('/mouse_up', methods=['POST'])
def handle_mouse_up():
    data = request.json
    pyautogui.mouseUp(button=data.get('button', 'left'))
    return jsonify(status='success')

@app.route('/double_click', methods=['POST'])
def handle_double_click():
    data = request.json
    click_double(button=data.get('button', 'left'))
    return jsonify(status='success')

def run_server():
    app.run(host='0.0.0.0', port=8071)

if __name__ == "__main__":
    # Avvia il server in un thread separato
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

    # Mantieni il programma principale in esecuzione
    try:
        if len(sys.argv) == 1:
            draw_circle()
        else:
            print("Modalità funzioni disponibili:")
            print("move_mouse(x, y, duration)")
            print("click_single(button)")
            print("click_double(button)")
            print("drag(start_x, start_y, end_x, end_y, button, duration)")
            print("long_click(x, y, button, hold_duration)")
        
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nInterruzione del server.")
        sys.exit(0)
