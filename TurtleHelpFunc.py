# -*- coding: utf-8 -*-
import turtle as tur

"""
全局变量定义
    bezier_STEP 贝塞尔函数的取样次数
    DRAW_SPEED  绘制速度
    WIDTH       界面宽度
    HEIGHT      界面高度
"""
bezier_STEP = 15
T_RANGE = map(lambda x: x/bezier_STEP, range(0, bezier_STEP+1))
T_LIST = [x/bezier_STEP for x in range(0, bezier_STEP+1)]
DRAW_SPEED = 5
WIDTH = 600
HEIGHT = 600


"""
辅助函数
"""


# 线性插值
def linear_interp(p1, p2, t):
    return p1*(1-t) + p2*t


# 一阶 bezier 函数 - Tuple
def bezier1(p1, p2, t):
    return (
        linear_interp(p1[0], p2[0], t),
        linear_interp(p1[1], p2[1], t)
    )


# 二阶 bezier 函数
def bezier2(p1, p2, p3, t):
    return bezier1(
        bezier1(p1, p2, t),
        bezier1(p2, p3, t),
        t
    )


# 三阶 bezier 函数
def bezier3(p1, p2, p3, p4, t):
    return bezier1(
        bezier2(p1, p2, p3, t),
        bezier2(p2, p3, p4, t),
        t
    )


def bezier_3(p1, p2, p3, p4):
    tur.pendown()
    for t in T_LIST:
        x,y = bezier3(p1, p2, p3, p4, t)
        tur.goto(x, y)
    tur.penup()


def p(c):  # 将 SVG 坐标 c 转换为 tur 坐标
    return complex(
        + c.real - WIDTH/2,
        - c.imag + HEIGHT/2
    )


def M(c):  # 移动到 SVG 坐标 c
    tur.goto(p(c).real, p(c).imag)


"""
绘图函数
"""


def Line(start, end):
    # tur.penup()
    M(start)
    tur.pendown()
    M(end)
    tur.penup()


def CubicBezier(start, control1, control2, end):
    M(start)
    bezier_3(
        (p(start).real, p(start).imag),
        (p(control1).real, p(control1).imag),
        (p(control2).real, p(control2).imag),
        (p(end).real, p(end).imag))


def Arc(a, *b): # 禁用
    pass





"""
绘图代码
"""
screen = tur.Screen()
screen.bgcolor("white")

tur.tracer(100)   # 调整作画时间
tur.pensize(1)
tur.speed(DRAW_SPEED)
tur.penup()

# Output of `SVG pre process.py`

tur.hideturtle()  # 隐藏乌龟图标
tur.update()

