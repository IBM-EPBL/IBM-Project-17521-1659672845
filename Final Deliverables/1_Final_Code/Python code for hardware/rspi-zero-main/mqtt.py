

import paho.mqtt.publish as publish

publish.single("status", "oooo", hostname="mqtt.eclipseprojects.io")