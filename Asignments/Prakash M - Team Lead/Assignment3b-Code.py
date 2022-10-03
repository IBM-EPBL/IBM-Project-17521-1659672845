# IBM-Project Guidence available--Insta @Diino_the_dev
import turtle
import time
wn= turtle.getscreen()
wn.title("Stoplight By Diino-Prakash")
wn.bgcolor("black")


pen= turtle.Turtle()
pen.color("Yellow")
pen.width(4)
pen.hideturtle()
pen.penup()
pen.goto(-30, 60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)




red_light =turtle.Turtle()
red_light.shape("circle")
red_light.color("grey")
red_light.penup()
red_light.goto(0, 40)


yellow_light =turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("grey")
yellow_light.penup()
yellow_light.goto(0, 0)

green_light =turtle.Turtle()
green_light.shape("circle")

green_light.color("grey")
green_light.penup()
green_light.goto(0, -40)


while True:
    yellow_light.color("grey")
    red_light.color("red")
    print("Red light Blinked - Now vehicle Stop behind zebra cross..")
    print("Blink!!")
    time.sleep(2)
    print("Blink!!")

    red_light.color("grey")
    green_light.color("green")
    print("Green light on- Now vehicle can go..")
    print("Blink!!")
    time.sleep(3)
    print("Blink!!")

    green_light.color("grey")
    yellow_light.color("yellow")
    print("Yellow light Blinked- Now vehicle Ready to go..")
    print("Blink!!")
    time.sleep(1)
    print("Blink!!")


wn.mainloop()
