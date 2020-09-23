# -*- coding:utf-8 -*-
'''
For User login
'''

from handler.base.base_handler import BaseHandler


class LoginHandler(BaseHandler):
    '''
    Handler for Admin.
    '''
    def initialize(self, **kwargs):
        super(LoginHandler, self).initialize()

    def get(self, *args, **kwargs):
        print("login get")
        self.render('login.html')

    def post(self, *args, **kwargs):
        print("login post")
        self.render("/notation/asr")
