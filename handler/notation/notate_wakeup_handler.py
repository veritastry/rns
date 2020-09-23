# -*- coding:utf-8 -*-
'''
For   wakeup natate
'''

import tornado.web
from handler.base.base_handler import BaseHandler


class NotateWakeupHandler(BaseHandler):
    '''
    Handler for Admin.
    '''
    def initialize(self, **kwargs):
        super(NotateWakeupHandler, self).initialize()

    def get(self, *args, **kwargs):
        # self.write("hello ")
        self.render("wakeup_notate.html")
