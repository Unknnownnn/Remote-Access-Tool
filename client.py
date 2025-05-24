"""
client.py (Educational Version)

This file is for educational purposes only. All potentially dangerous code has been removed or replaced with safe code.
"""

import socket
import educational_logger

def connect_to_server(server_ip, server_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_ip, server_port))
        print(f"[Educational] Connected to server at {server_ip}:{server_port}")
        while True:
            data = s.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f"[Educational] Received from server: {message}")
            if message.strip().lower() == 'exit':
                print("[Educational] Exiting on server request.")
                break
        s.close()
    except Exception as e:
        print(f"[Educational] Connection failed: {e}")

if __name__ == "__main__":
    connect_to_server("127.0.0.1", 4444) 