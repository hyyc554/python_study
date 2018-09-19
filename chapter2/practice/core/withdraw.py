# -*- coding: utf-8 -*-


def with_draw(kavrgs):
    draw_num = input('请输入提现金额：').strip()
    if draw_num.isdigit():
        draw_num = int(draw_num)
        if draw_num <= kavrgs['credit_line']:
            kavrgs['balance'] -= (draw_num * 1.05)
        else:
            kavrgs['balance'] -= draw_num
    return kavrgs
