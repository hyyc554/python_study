import sys ,os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #__file__的是打印当前被执行的模块.py文件相对路径，注意是相对路径
print(BASE_DIR)

sys.path.append(BASE_DIR)

from proj import settings

def sayhi():
    print('hello world!')

print(settings.DATABASES)



