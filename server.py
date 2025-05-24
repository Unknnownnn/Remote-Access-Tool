"""
server.py (Educational Version)

This file is for educational purposes only. All potentially dangerous code has been removed or replaced with safe code.
"""

import socket

def start_server(listen_ip, listen_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((listen_ip, listen_port))
    s.listen(1)
    print(f"[Educational] Server listening on {listen_ip}:{listen_port}")
    conn, addr = s.accept()
    print(f"[Educational] Connection from {addr}")
    while True:
        command = input("Enter message to send to client ('exit' to quit): ")
        conn.sendall(command.encode('utf-8'))
        if command.strip().lower() == 'exit':
            print("[Educational] Exiting and closing connection.")
            break
    conn.close()
    s.close()

if __name__ == "__main__":
    # Example usage (safe values)
    start_server("0.0.0.0", 4444) 