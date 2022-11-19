import time

while True:
    exec(open("./main.py").read())
    #exec("/home/pi/Documents/main.py")
    time.sleep(60)
    print("Done")