import network

# enable station interface and connect to WiFi access point
sta = network.WLAN(network.STA_IF)
sta.active(True)
networks = sta.scan()

# laut docu eigentlich 0..4, man bekommt aber 5 für WPA/WPA2-PSK?
SECURITY = dict([(1,'open'), (2,'WEP'), (3,'WPA-PSK'), (4,'WPA2-PSK'), (5,'WPA/WPA2-PSK')])
#HIDDEN = dict([(0,'visible'),(1,'hidden')])

for ssid, bssid, channel, rssi, security, visibility in sorted(networks):
    ssid = ssid.decode('UTF-8')
    encrypted = security > 1
    print("ssid: %s, chan: %d, encrypted: %s, encryption: %s" % (ssid,channel,encrypted, SECURITY.get(security,'?')))

