# encoding: UTF-8

import os
print u'load {0}/*'.format(os.path.dirname(__file__))

# 默认设置
from chinese import text

# 是否要使用英文
from vnpy.trader.vtGlobal import globalSetting
if globalSetting['language'] == 'english':
    from english import text