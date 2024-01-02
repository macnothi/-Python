import network

# enable station interface and connect to WiFi access point
sta = network.WLAN(network.STA_IF)
sta.active(True)

networks = sta.scan()

SECURITY = {0: 'open', 1: "WEP", 2: "WPA-PSK", 3: "WPA2-PSK", 4: "WPA/WPA2-PSK"}
HIDDEN = {0: 'visible', 1: 'hidden'}

