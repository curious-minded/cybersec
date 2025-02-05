import socket
import random
import time
import logging

logging.basicConfig(
    filename="client1_logs.txt",
    level=logging.INFO,
    format="%(asctime)s  %(message)s"
)

def generate_ip():
    return f"192.168.0.{random.randint(0, 255)}"

def generate_packet():
    packet_ip = generate_ip()
    packet_size = random.randint(50, 1500)
    packet_type = random.choice(["normal", "blocked", "suspicious"])
    
    packet = f"{packet_ip},{packet_size},{packet_type}"
    
    if len(packet.split(",")) != 3:
        print(f"Error: Malformed packet: {packet}")
        return None
    return packet

def client(id):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(10)  
            print(f"Client {id} connecting to the server...")
            client.connect(("localhost", 9999))
            print(f"Client {id} connected to the server. Sending packets...\n")

            while True:
                packet = generate_packet()
                if packet:
                    print(f"Client {id} Sending: {packet}")
                    client.sendall(packet.encode("utf-8"))
                    try:
                        response = client.recv(1024).decode("utf-8")
                        print(f"Client {id} Response: {response}\n")
                        logging.info(f"Sent: {packet} - Response: {response}")
                    except socket.timeout:
                        print(f"Client {id} Timeout: No response from server.")
                        logging.error(f"Timeout occurred while waiting for response.")
                    except socket.error as e:
                        print(f"Client {id} Socket error: {e}")
                        logging.error(f"Socket error: {e}")
                    
                    time.sleep(random.uniform(0.5, 2))  

    except ConnectionResetError:
        print("Server disconnected unexpectedly.")
        logging.error(f"Server disconnected unexpectedly.")
    except socket.error as e:
        print(f"Socket error: {e}")
        logging.error(f"Socket error: {e}")
    finally:
        print(f"Client {id} stopped.")

if __name__ == "__main__":
    client(1)
