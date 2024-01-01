
Wi-Fi Manager Web Server

- Initially, Raspberry Pi Pico W will be set up as an Access Point when it starts.
- Next, to connect to your Raspberry Pi Pico W which acts as an AP, we will go to the IP address 192.164.4.1.
- A web page containing available networks will be shown to choose the one to configure.
- The provided network credentials will get saved in Raspberry Pi Pico W.
Then we will set up a new SSID and password for our selected network. The Raspberry Pi Pico W will restart and now will be able to connect with the network we selected. In this phase the Pic W board acts in the Station mode.
If the connection is not successful, Pico W board goes back to AP mode and we will set the SSID and password again.