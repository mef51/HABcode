# Flight Program


## Make a program run on startup

https://www.raspberrypi.org/documentation/linux/usage/systemd.md

Create a service:

```sudo vi /etc/systemd/system/flight.service```

Enable the service:
```sudo systemctl enable flight.service```

Note: ensure the service runs the command in the background

## Flight Script

The flight script will start the camera and create an infinite loop taking methane and ozone readings every 1 second.

This has been tested on a 4-hour run using the Anker power block as the power supply.
