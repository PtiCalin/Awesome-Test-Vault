# 🌐 Calin Coin – Minimal P2P Node
# Purpose: Accept peer connections, share mempool, and broadcast blocks

import socket
import threading
import json

# ------------------ ⚙️ Config ------------------
HOST = '127.0.0.1'  # localhost for demo
PORT = 8453         # default port
PEERS = []          # known peer addresses (can be prefilled)
MEMPOOL = []        # shared mempool across peers

# ------------------ 📨 Message Protocol ------------------
def send_message(conn, data):
    message = json.dumps(data).encode('utf-8')
    conn.sendall(message)

def handle_message(message):
    try:
        data = json.loads(message)
        if data['type'] == 'transaction':
            MEMPOOL.append(data['payload'])
            print("🆕 Transaction received:", data['payload'])
        elif data['type'] == 'block':
            print("📦 New block broadcasted:", data['payload'])
        else:
            print("⚠️ Unknown message type:", data)
    except Exception as e:
        print("❌ Failed to handle message:", e)

# ------------------ 📡 Peer Listener ------------------
def handle_client(conn, addr):
    print(f"🔗 Connected to peer: {addr}")
    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            handle_message(data.decode('utf-8'))
    except:
        pass
    finally:
        conn.close()
        print(f"🔌 Disconnected from {addr}")

# ------------------ 🚀 Start Node ------------------
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"🌱 Calin Node running on {HOST}:{PORT}... Waiting for friends...\n")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

# ------------------ 🔗 Connect to Peer ------------------
def connect_to_peer(peer_ip, peer_port):
    try:
        peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        peer.connect((peer_ip, peer_port))
        PEERS.append(peer)
        print(f"🎉 Connected to peer at {peer_ip}:{peer_port}")
        return peer
    except Exception as e:
        print("🚫 Connection failed:", e)

# ------------------ 💌 Send Transaction ------------------
def broadcast_transaction(txn):
    for peer in PEERS:
        send_message(peer, {'type': 'transaction', 'payload': txn})

# ------------------ 🧪 Demo CLI ------------------
if __name__ == "__main__":
    threading.Thread(target=start_server, daemon=True).start()
    
    while True:
        cmd = input("\n✨ Calin Node Menu:\n[c] Connect to peer\n[t] Send transaction\n[q] Quit\n> ")
        if cmd == 'c':
            ip = input("Peer IP: ")
            port = int(input("Peer Port: "))
            connect_to_peer(ip, port)
        elif cmd == 't':
            txn = input("Paste signed transaction JSON: ")
            try:
                txn_data = json.loads(txn)
                broadcast_transaction(txn_data)
                print("📨 Transaction sent to peers!")
            except:
                print("⚠️ Invalid JSON format.")
        elif cmd == 'q':
            break
