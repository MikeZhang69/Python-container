import websocket
import json
import time
import subprocess

# WebSocket URL for noVNC clipboard (adjust port if needed)
WS_URL = "ws://127.0.0.1:6080/websockify"

def get_clipboard():
    try:
        result = subprocess.run(['xclip', '-o'], capture_output=True, text=True)
        return result.stdout.strip()
    except:
        return ""

def set_clipboard(text):
    try:
        subprocess.run(['echo', text, '|', 'xclip', '-i'], shell=True)
    except:
        pass

def on_message(ws, message):
    data = json.loads(message)
    if data.get("type") == "clipboard":
        set_clipboard(data.get("data", ""))

def on_open(ws):
    print("Clipboard relay connected")
    while True:
        clipboard = get_clipboard()
        if clipboard:
            ws.send(json.dumps({"type": "clipboard", "data": clipboard}))
        time.sleep(0.5)

if __name__ == "__main__":
    ws = websocket.WebSocketApp(WS_URL,
                              on_message=on_message,
                              on_open=on_open)
    ws.run_forever()