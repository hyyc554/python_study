# -*- coding: utf-8 -*-

import logging


ch = logging.StreamHandler()
fh = logging.FileHandler('my.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(massage)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger = logging.getLogger("ascees")
logger.addHandler(fh)
logger.addHandler(ch)
logger.error('account [1234] too many login attempts')