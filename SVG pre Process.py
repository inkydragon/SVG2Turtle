# -*- coding: utf-8 -*-
from svgpathtools import svg2paths2
import re

TURTLE_LEADER = "tur"
"""
SVG 解析处理函数
"""


## 上色函数
def begin_fill(rgb):
    tur.color("black", "#F2F2F2")
    M(151.94 + 332.51j)
    tur.begin_fill()


def end_fill():  # 结束填充
    print("%s.end_fill()" % TURTLE_LEADER)


## 输出函数
def p(i):  # 打印单条路径
    if 'id' in attributes[i]:
        print("\n## %s" % attributes[i]['id'])
    for cur in paths[i]:
        # res = re.sub(r"\n\s+", "\n", repr(cur))
        res = re.sub(r"(control.=)|(start=)|(end=)|(radius=)|(rotation=)|(large_arc=)|(sweep=)", "", repr(cur))
        res = re.sub(r"\(\(", "(", res)
        res = re.sub(r"\), \(", ", ", res)
        res = re.sub(r"\)\)[,]*", ")", res)
        print(res)
    # print(paths[i])
    # print(attributes[i])


def p_ij(i=0, j=10):  # 打印路径 [i, j)
    subpath_count = 1
    for idx in range(i, j):
        if 'id' in attributes[idx]:
            subpath_count = 1
        else:
            subpath_count += 1
            print("\n# %d" % subpath_count)
        p(idx)
    # print(paths[i:j])
    print("\n# Origin SVG Paths")
    print(attributes[i])
    print(attributes[j-1])


def p_all():  # 打印所有路径
    p_ij(i=0, j=len(paths))


"""
代码
"""

#paths, attributes, svg_attributes = svg2paths2("Eriri-small2-human-onlyColor.svg")
paths, attributes, svg_attributes = svg2paths2("LoveYourSelf-lion.svg")

#pathsr, attributesr, svg_attributesr = svg2paths2("Eriri-small2-human-onlyColor.svg",convert_to_turtle_r=True)


p_all()
