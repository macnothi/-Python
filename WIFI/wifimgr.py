import network

# enable station interface and connect to WiFi access point
sta = network.WLAN(network.STA_IF)
sta.active(True)

networks = sta.scan()

SECURITY = dict([(0,'open'), (1,'WEP'), (2,'WPA-PSK'), (3,'WPA2-PSK'), (4,'WPA/WPA2-PSK')])
HIDDEN = dict([(0,'visible'),(1,'hidden')])

for ssid, bssid, channel, rssi, security, hidden in networks:
    ssid = ssid.decode('UTF-8')
    print("ssid: %s, chan: %d, security: %d, visibility: %d" %(ssid,channel,security,hidden))
