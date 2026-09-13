import random

servers = {
    "DB server":"192.168.1.5",
    "Web server":"192.168.1.10",
    "Wazuh server":"192.168.1.15"
}
    
def generate_ping():
    ping_latency = random.randint(10, 500)
    return ping_latency    
    
def check_server(server, ip):

    current_ping = generate_ping()
    print(f"Starting checks: {server} {ip}")
    print(f"Ping on server {server} is {current_ping} ms")
    return current_ping

def ping():
    for server, ip in servers.items():
        latency = check_server(server, ip)
        
        if latency > 300:
            print("Warning! Ping is too high!")
        else:
            print("Status: Everything is fine.")
        
if __name__ == "__main__":
    ping()
    
