import socket
import logging
import time
import random
from threading import Thread, Lock

servers = ["Server1", "Server2", "Server3"]
current_server = 0
blacklist = {f"192.168.0.{random.randint(0, 255)}" for _ in range(15)}
client_timestamps = {}
timestamps_lock = Lock()

logging.basicConfig(filename="packet_logs.txt", level=logging.INFO,
                    format="%(asctime)s - %(message)s")

def inspect_packet(data, addr):
    try:
        packet_ip, packet_size, packet_type = data.split(",")
        packet_size = int(packet_size)
        packet_type = packet_type.strip()

        if packet_ip in blacklist:
            status = f"Packet from {packet_ip} is blocked by firewall"
            logging.info(f"Packet: {data} -> Status: {status}")
            return status

        global current_server
        assigned_server = servers[current_server]
        current_server = (current_server + 1) % len(servers)

        if packet_size > 1000:
            status = f"Packet from {packet_ip} - Assigned to {assigned_server} - Flagged due to suspicious activity"
        else:
            status = f"Packet from {packet_ip} - Assigned to {assigned_server} - Processed successfully"

        logging.info(f"Packet: {data} -> Status: {status}")
        return status
    except Exception as e:
        logging.error(f"Error inspecting packet: {data} -> {e}")
        return f"Error processing packet: {e}"

def is_rate_limited(packet_ip):
    now = time.time()
    with timestamps_lock:  
        if packet_ip in client_timestamps:
            if now - client_timestamps[packet_ip] < 2:  
                return True
        client_timestamps[packet_ip] = now
    return False

def handle_client(conn, addr):
    print(f"Server connected to {addr}")
    while True:
        try:
            data = conn.recv(1024).decode("utf-8")
            if not data:
                break

            packet_ip = data.split(",")[0]
            if is_rate_limited(packet_ip):
                status = f"Rate-limited connection from {packet_ip}"
                print(status)
                conn.sendall(status.encode("utf-8"))
                continue  

            status = inspect_packet(data, addr)
            print(f"Processing Packet: {data} -> Status: {status}")
            conn.sendall(status.encode("utf-8"))
        except ConnectionResetError:
            print(f"Connection reset by {addr}")
            break
        except socket.error as e:
            print(f"Socket error with {addr}: {e}")
            break
        except Exception as e:
            print(f"Unexpected error with {addr}: {e}")
            break

    conn.close()
    print(f"Connection closed with {addr}")

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(("localhost", 9999))
        server.listen(5)
        print("Secure server started on port 9999. Listening for packets...")

        while True:
            conn, addr = server.accept()
            thread = Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()

if __name__ == "__main__":
    server()