import random
from flask import Flask

app = Flask(__name__)

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
    checked_server = f"Ping on server {server} {ip} is {current_ping} ms"
    return current_ping



@app.route("/")
def dashboard():
    html_content = "<h1>Server Status</h1><br>"
    
    for server, ip in servers.items():
        latency = check_server(server, ip)
        
        if latency > 300:
            html_content += f"<br>Ping on server {server} {ip} is {latency} ms. Warning! Ping is too high!"
        else:
            html_content += f"<br>Ping on server {server} {ip} is {latency} ms. Status: Everything is fine."
    
    return html_content


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
    
# flask run --host=0.0.0.0 --port=8080 -> if without arg port - default 5000
# or python3 app.py -> then my if __name__ == "__main__" will work