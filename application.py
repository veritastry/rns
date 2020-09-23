# -*- coding:utf-8 -*-
'''
The Application.
'''

from router import router
from settings import setting, SITE_ROOT  # , DB_CFG, SITE_CFG

import tornado.web
print("site root=", SITE_ROOT)
APP = tornado.web.Application(handlers=router, **setting)
