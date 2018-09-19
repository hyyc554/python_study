#encoding:utf-8

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

#输出一级菜单
exit_flag = False
while not exit_flag:
    for p in menu:
        print(p)
    province = input('请输入你所在的省份,或者退出Q：')
    if province == 'Q':
        break
    exit_flag_1 = False
    while not exit_flag_1:
        if province in menu:
            for c in menu[province]:
                print(c)
            print('请选择你所在的城市，或者返回返回上级菜单B,或者退出Q')#二级菜单
            city = input('城市：')
            if city in menu[province]:
                exit_flag_2 = False
                while not exit_flag_2:
                    for l in menu[province][city]:
                        print(l)
                    tom = input('请选择你所在的区域，或者退出Q,或者返回返回上级菜单B：')
                    if tom in menu[province][city]:
                        for Z in menu[province][city][tom]:#打印三级菜单
                            print(Z)
                        end = input('请仔细浏览，或者返回上级菜单B，或者退出Q：')
                        if end == 'B':
                            break
                        else:
                            exit_flag_1 = True
                            exit_flag = True
                            break
                    elif tom == 'B':# 返回一级菜单
                        break
                    else:# 退出
                        exit_flag_1 = True
                        exit_flag = True
                        break
            elif city == 'B':#返回一级菜单
                break
            else:#退出
                exit_flag = True
                break