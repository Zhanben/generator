# -*- coding: utf-8 -*-

import sys
import time
import random
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('hei', './STSONG.ttf'))


def gen_data(num):
    data = [[]]
    for i in range(0, 20):
        temp = []
        for j in range(0, 5):
            op1 = int(random.randint(1, num))
            op2 = int(random.randint(1, num))
            op = "+" if op1 % 2 == 0 else "-"
            if op == "+":
                temp.append("%d+%d=" % (op1, op2))
            else:
                if op1 > op2:
                    temp.append("%d-%d=" % (op1, op2))
                else:
                    temp.append("%d+%d=" % (op1, op2))
        data.append(temp)
    return data


def gen_pdf(name, data):
    doc = SimpleDocTemplate("./%s.pdf" % name, rightMargin=0, leftMargin=1 * cm, topMargin=0.3 * cm, bottomMargin=0)
    t = Table(data, colWidths=100, rowHeights=34)
    stylesheet = getSampleStyleSheet()
    s = ParagraphStyle(name='My',
                       parent=stylesheet['Normal'],
                       fontName='hei',
                       fontSize=16,
                       alignment=TA_CENTER,
                       spaceAfter=3)
    text = list()
    text.append(Paragraph('<font name="hei">%s</font>' % name, s))
    text.append(t)
    s.spaceBefore = 16
    s.fontSize = 12
    text.append(Paragraph('<font name="hei">头条号: 程序员学数学 </font>', s))
    doc.build(text)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("使用: ./Generator.exe num \n说明: num为10到100之间的整数，例如num为10，则生成的文件内容为10以内的加减法")
    else:
        d = gen_data(int(sys.argv[1]))
        n = time.strftime('%Y-%m-%d') + "练习题%s以内的加减法" % sys.argv[1]
        gen_pdf(n, d)
