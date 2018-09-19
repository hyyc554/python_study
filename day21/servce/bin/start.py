# -*- coding: utf-8 -*-
import os
import sys
from  import main


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)


# if __name__ == '__main__':
#     main.run()