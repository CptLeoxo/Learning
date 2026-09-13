# Zabbix

- Zabbix is an enterprise-class, open-source monitoring solution that makes network and application monitoring simple.

Source: https://www.zabbix.com/

# Zabbix Agent 2 Installation and Configuration Guide

This guide provides step-by-step instructions for installing and configuring **Zabbix Agent 2** on a Linux host, including the setup for native Docker container monitoring.

## 1. System Preparation and Installation

Before installing, verify your OS version and architecture to ensure you download the correct repository package.

### Verify OS and Architecture

```bash
cat /etc/os-release
uname -m
```

### Add Zabbix 7.0 Repository

Navigate to the [official Zabbix repository](https://repo.zabbix.com/zabbix/7.0/) to find the correct package for your distribution, then download and install it:

```bash
wget https://repo.zabbix.com/zabbix/7.0/<os>/pool/main/z/zabbix-release/zabbix-release_7.<info>.deb
sudo dpkg -i zabbix-release_7.<info>.deb
sudo apt update
```

### Install and Verify Zabbix Agent 2

```bash
sudo apt-get install zabbix-agent2
zabbix_agent2 -V
```

---

## 2. Core Configuration

Edit the main configuration file to connect the agent to your Zabbix Server or Proxy.

```bash
sudo nano /etc/zabbix/zabbix_agent2.conf
```

Find and modify the following parameters according to your infrastructure topology:

```ini
# --- General Parameters ---
LogFile=/var/log/zabbix/zabbix_agent2.log
DebugLevel=3
SourceIP=<AGENT_MACHINE_IP>

# --- Passive Checks ---
# List of Zabbix servers or proxies that are allowed to poll this agent
Server=<ZABBIX_SERVER_IP_1>,<ZABBIX_SERVER_IP_2>
ListenPort=10050

# --- Active Checks ---
# Address of the Zabbix server/proxy where the agent will send active metrics
ServerActive=<ZABBIX_PROXY_OR_NODE_IP>:10051

# Dynamically fetch the hostname of the current machine
HostnameItem=system.run[hostname -s]

# --- Sockets ---
PluginSocket=/run/zabbix/agent.plugin.sock
ControlSocket=/run/zabbix/zabbix_agent2.sock
```

---

## 3. Enable Docker Container Monitoring

Zabbix Agent 2 supports native Docker monitoring out of the box via plugins.

### Configure Docker Plugin

Edit the Docker plugin configuration file:

```bash
sudo nano /etc/zabbix/zabbix_agent2.d/plugins.d/docker.conf
```

Ensure the following parameters are set to allow the agent to read the Docker socket:

```ini
### Option: Plugins.Docker.Endpoint
# Docker API endpoint.
Plugins.Docker.Endpoint=unix:///var/run/docker.sock

### Option: Plugins.Docker.Timeout
# The maximum time (in seconds) for waiting when a request has to be done.
Plugins.Docker.Timeout=5
```

_Note: Ensure that the `zabbix` user is added to the `docker` group so the agent has sufficient permissions to read the socket._

```bash
# Restart the agent to apply all configurations
sudo systemctl restart zabbix-agent2
sudo systemctl status zabbix-agent2
```
