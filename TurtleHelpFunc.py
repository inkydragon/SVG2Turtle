# -*- coding: utf-8 -*-
import turtle as tur
from math import sin, cos, pi

DRAW_SPEED = 30
PEN_SIZE = 6
WIDTH = 600
HEIGHT = 600

"""
辅助函数
"""
def linear_interp(p1, p2, t):
    return p1 * (1 - t) + p2 * t

def bezier1(p1, p2, t):
    return (
        linear_interp(p1[0], p2[0], t),
        linear_interp(p1[1], p2[1], t)
    )

def bezier2(p1, p2, p3, t):
    return bezier1(
        bezier1(p1, p2, t),
        bezier1(p2, p3, t),
        t
    )

def bezier3(p1, p2, p3, p4, t):
    return bezier1(
        bezier2(p1, p2, p3, t),
        bezier2(p2, p3, p4, t),
        t
    )

def bezier_3(p1, p2, p3, p4):
    for t in [x / 15 for x in range(0, 15 + 1)]:
        x, y = bezier3(p1, p2, p3, p4, t)
        tur.goto(x, y)


def p(c):  # 将 SVG 坐标 c 转换为 tur 坐标
    return complex(
        + c.real - WIDTH / 2,
        - c.imag + HEIGHT / 2
    )

def M(c):  # 移动到 SVG 坐标 c
    tur.goto(p(c).real, p(c).imag)

def L(start, end):
    M(start)
    M(end)

def C(start, control1, control2, end):
    M(start)
    bezier_3(
        (p(start).real, p(start).imag),
        (p(control1).real, p(control1).imag),
        (p(control2).real, p(control2).imag),
        (p(end).real, p(end).imag))

def f(sp=0j, rgb='red'):
    tur.fillcolor(rgb)
    M(sp)
    tur.begin_fill()

nf = tur.end_fill

def pd(sp, rgb="#E4007F", bold=PEN_SIZE):
    tur.color(rgb)
    tur.pensize(bold)
    M(sp)
    tur.pendown()

def pu():
    tur.penup()
    tur.pensize(PEN_SIZE)
    tur.color("black")

def E(
        cx, cy,
        a, b,
        matrix=(1, 0, 0, 1, 0, 0)):
    cp = complex(cx, cy)  # 中心
    sp = cp + a  # 绘制起点
    tur.penup()
    M(transform(sp, matrix))
    tur.color("#FB8D8C")
    tur.pensize(0.1)
    tur.fillcolor("#FB8D8C")
    tur.begin_fill()
    tur.pendown()
    for i in range(0, 360 + 1):
        x = a * sin(i * 2 * pi / 360 + pi / 2) + cx
        y = b * cos(i * 2 * pi / 360 + pi / 2) + cy
        p = complex(x, y)
        M(transform(p, matrix))
    nf()
    pu()

def transform(p, matrix=(1, 0, 0, 1, 0, 0)):
    a, b, c = matrix[0], matrix[1], matrix[2],
    d, e, f = matrix[3], matrix[4], matrix[5],
    return complex(
        a * p.real + c * p.imag + e,
        b * p.real + d * p.imag + f
    )

def Mv(c):  # 移动到 SVG 坐标 c
    tur.penup()
    tur.goto(p(c).real, p(c).imag)
    tur.pendown()


"""
绘图代码
"""
screen = tur.Screen()
screen.bgcolor("white")

tur.tracer(3)  # 调整作画时间
tur.pensize(PEN_SIZE)
tur.speed(DRAW_SPEED)
tur.penup()

# Output of `SVG pre process.py`

tur.hideturtle()  # 隐藏乌龟图标
tur.update()
