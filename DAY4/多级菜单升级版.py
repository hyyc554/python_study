# -*- coding: utf-8 -*-

menu = {
    '武汉':{
        '武昌':{
            '光谷':{
                '华为':{},
                '小米':{},
                '华中科技大学':{}
            },
            '洪山':{
                '华中农业大学':{},
                '中南民族大学':{},
                '中南财经政法大学':{},
            },
            '街道口':{
                '武汉大学':{},
            },
        },
        '汉口':{
            '常青花园':{
                '武汉轻工大学':{},
                '张公堤':{},
            },
            '江汉路':{},
            '青年路':{},
        },
        '汉阳':{},
        '黄陂':{},
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

current_level = menu
level = []
while True:
    for key in  current_level:
        print(key)
    choice = input("请输入您希望进入的次级区域，返回上级菜单请输入'b',退出程序请输入'q'：")
    if choice in current_level:#开始进入下一级菜单
        level.append(current_level)
        current_level = current_level[choice]
    elif choice == 'b':#返回上级菜单
        if len(level) == 0:
            break
        else:
            current_level = level.pop()
    else:#输入‘q’或者其他错误选项将直接退出程序
        break