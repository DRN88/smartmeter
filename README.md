# README.md

For education purposes only. Many parts of this project are unsecured. 

https://www.netbeheernederland.nl/_upload/Files/Slimme_meter_15_a727fce1f1.pdf
https://www.eon.hu/content/dam/eon/eon-hungary/documents/Lakossagi/aram/muszaki-ugyek/fogyasztasmerok/Holley-DDSD285-DTSD545-v01.pdf
https://www.promotic.eu/en/pmdoc/Subsystems/Comm/PmDrivers/IEC62056_OBIS.htm

# Influxdb python token

- Get a token: http://192.168.222.133:8086/orgs/89f86e4a1ae70ff0/new-user-setup/python
- Update the token in smartmeter: `main.py`

# Manually setup systemd service

root@smartmeter:/etc/systemd/system# cat smartmeter.service 

```conf
[Unit]
Description=SmartMeter Python
After=multi-user.target

[Service]
Type=simple
User=gorkhaan
Group=gorkhaan
Restart=always
WorkingDirectory=/home/gorkhaan/ProjectSmartmeter/smartmeter
ExecStart=/home/gorkhaan/.local/bin/poetry run python main.py

[Install]
WantedBy=multi-user.target
```

# Manually set up InfluxDB2

Make sure you actually install `influxdb2`

# Old project

https://github.com/DRN88/esp8266UartDsmrMqtt
