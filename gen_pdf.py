import random
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('hei', './STSONG.ttf'))


def gen_add_minus(data, num, total):
    for i in range(0, total):
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


def gen_multi_plus(data, num, total):
    for i in range(0, total):
        temp = []
        for j in range(0, 5):
            op1 = int(random.randint(1, num))
            op2 = int(random.randint(1, num))
            op = "x" if op1 % 2 == 0 else "÷"
            if op == "x":
                temp.append("%dx%d=" % (op1, op2))
            else:
                if op1 % op2 == 0:
                    temp.append("%d÷%d=" % (op1, op2))
                else:
                    temp.append("%dx%d=" % (op1, op2))
        data.append(temp)
    return data


def Gen_pdf(name, add_flag, add_range_value, multi_flag, multi_range_value):
    doc = SimpleDocTemplate("./%s.pdf" % name, rightMargin=0, leftMargin=1 * cm, topMargin=0.3 * cm, bottomMargin=0)
    data = [[]]
    if add_flag and multi_flag:
        data = gen_add_minus(data, add_range_value, 10)
        data = gen_multi_plus(data, multi_range_value, 10)
    elif add_flag:
        data = gen_add_minus(data, add_range_value, 20)
    else:
        data = gen_multi_plus(data, multi_range_value, 20)
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
