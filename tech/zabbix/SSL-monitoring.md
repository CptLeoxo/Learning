# Monitoring SSL/TLS Certificates with Zabbix Agent 2

This quick guide demonstrates how to monitor SSL/TLS certificate expiration dates using the native `web.certificate.get` key in Zabbix Agent 2.

## 1. Command Line Testing

To test the metric extraction directly from the terminal, run the following command. Replace `<DOMAIN_OR_IP>` with your target website or IP address:

```bash
zabbix_agent2 -t 'web.certificate.get[<DOMAIN_OR_IP>,443]'
```

## 2. Zabbix Web UI Configuration

When creating a new **Item** in the Zabbix frontend, use the following configuration to collect the certificate data:

- **Type:** Zabbix agent (or Zabbix agent active)
- **Key:** `web.certificate.get[<DOMAIN_OR_IP>,443]`
- **Type of information:** Text

### Preprocessing Step

The native key returns a full JSON object with certificate details. To extract only the expiration timestamp, add the following preprocessing step:

- **Step:** JSONPath
- **Parameters:** `$.x509.not_after.value`
