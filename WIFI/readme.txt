Raspberry Pi Pico WIFI Manager Pseudocode

start in sta mode
scan available networks  
read credentials from file
if network credentials match an available network
    try to connect 
    if connected
        return connection

stop sta mode
start ap mode
start web service
    show list of available networks
    wait for input of credentials
    try to connect
        write credentials    
