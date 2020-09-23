# -*- coding:utf-8 -*-
'''
For   asr notate
'''

import tornado.web
from handler.base.base_handler import BaseHandler


class NotateAsrHandler(BaseHandler):
    '''
    Handler for Admin.
    '''
    def initialize(self, **kwargs):
        super(NotateAsrHandler, self).initialize()

    def get(self, *args, **kwargs):
        # self.write("hello ")
        self.render("asr_notate.html")

    # def initialize(self, **kwargs):
    #     super(NotateAsrHandler, self).initialize()

    # # @tornado.web.authenticated
    # def get(self, *args, **kwargs):
    #     url_str = args[0]
    #     if url_str == '':
    #         self.index()
    #     else:
    #         self.render('misc/html/404.html', kwd={}, userinfo=self.userinfo)

    # @tornado.web.authenticated
    # def post(self):
    #     self.render('user/asr', userinfo=self.userinfo, kwd={})
