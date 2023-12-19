# README.md

Arduino project. This is only for education purposes. If you want to make it a bit more secure, add at least http basic authentication for the enpoints.
This code is super simple, but in return, I had to parse the DSMR data on server side.

You can use `ElegantOTA` to update the firmware, well OTA. For that you need a firmware.  

Use Arduino to rebuild and export your firmware: `Sketch -> Export Compiled Binary`.  
Use the compiled `whatever.ino.bin` and upload it to your esp8266 elegantota endpoint: `http://1.2.3.4/update` (OTA Mode: Firmware)
