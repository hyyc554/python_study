# -*- coding: utf-8 -*-
# 1.logging模块有几个日志级别？


# 2.请配置logging模块，使其在屏幕和文件里同时打印以下格式的日志

# 2017-10-18 15:56:26,613 - access - ERROR - account [1234] too many login attempts

import logging

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
fh = logging.FileHandler('my.log', encoding='utf-8')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger = logging.getLogger('access')

logger.addHandler(fh)
logger.addHandler(ch)


logger.error('account [1234] too many login attempts')
