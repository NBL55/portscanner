import socket
from datetime import datetime

target = "127.0.0.1"  # Replace with desired IP or domain
start_port = 20
end_port = 100

print(f"\nStarting scan on {target} from port {start_port} to {end_port}\n")
start_time = datetime.now()

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    sock.close()

end_time = datetime.now()
print(f"\nScan completed in: {end_time - start_time}")
