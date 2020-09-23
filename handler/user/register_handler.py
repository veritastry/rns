# -*- coding:utf-8 -*-
'''
For User register
'''

import tornado.web
from handler.base.base_handler import BaseHandler


class RegisterHandler(BaseHandler):
    '''
    Handler for Admin.
    '''
    def initialize(self, **kwargs):
        super(RegisterHandler, self).initialize()

    def get(self, *args, **kwargs):
        url_str = args[0]
        if url_str == '':
            self.index()
        else:
            self.render('misc/html/404.html', kwd={}, userinfo=self.userinfo)

    @tornado.web.authenticated
    def index(self):
        self.render('admin/admin_index.html', userinfo=self.userinfo, kwd={})
