# -*- coding:utf-8 -*-
'''
For User login
'''

from handler.base.base_handler import BaseHandler


class IndexHandler(BaseHandler):
    '''
    Handler for Admin.
    '''
    def initialize(self, **kwargs):
        super(IndexHandler, self).initialize()

    def get(self, *args, **kwargs):
        # self.write("hello ")
        self.render("asr_notate.html")

    #self.redirect("/login")
