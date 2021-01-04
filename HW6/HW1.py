from turtle import *
import time

t = Turtle()
t.screen.setup(800, 800)
t.hideturtle()


def blink():
    t.begin_fill()
    t.circle(60, 360)
    t.fillcolor("white")
    t.end_fill()


def colors(color, x, y):
    t.penup()
    t.speed(0)
    t.goto(x, y)
    t.begin_fill()
    t.circle(60, 360)
    t.fillcolor(color)
    t.pendown()
    t.end_fill()


class TrafficLight:
    __color = ["red", "yellow", "green"]

    def running(self):
        i = 0
        while i < 3:
            if i == 0:
                colors(TrafficLight.__color[i], 0, 110)
                time.sleep(7)
                blink()
                colors(TrafficLight.__color[i], 0, 110)
                time.sleep(1)
                blink()
                colors(TrafficLight.__color[i], 0, 110)
                time.sleep(1)
                blink()
                colors(TrafficLight.__color[i], 0, 110)
                time.sleep(1)
                blink()
                i += 1
            elif i == 1:
                colors(TrafficLight.__color[i], 0, -10)
                time.sleep(5)
                blink()
                colors(TrafficLight.__color[i], 0, -10)
                time.sleep(1)
                blink()
                colors(TrafficLight.__color[i], 0, -10)
                time.sleep(1)
                blink()
                colors(TrafficLight.__color[i], 0, -10)
                time.sleep(1)
                blink()
                i += 1
            else:
                colors(TrafficLight.__color[i], 0, -130)
                time.sleep(3)
                blink()
                colors(TrafficLight.__color[i], 0, -130)
                time.sleep(1)
                blink()
                colors(TrafficLight.__color[i], 0, -130)
                time.sleep(1)
                blink()
                colors(TrafficLight.__color[i], 0, -130)
                time.sleep(1)
                blink()
                i += 1

        t.screen.exitonclick()


a = TrafficLight()
a.running()
