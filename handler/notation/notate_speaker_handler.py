# -*- coding:utf-8 -*-
'''
For   speaker natate
'''

import tornado.web
from handler.base.base_handler import BaseHandler


class NotateSpeakerHandler(BaseHandler):
    '''
    Handler for Admin.
    '''
    def initialize(self, **kwargs):
        super(NotateSpeakerHandler, self).initialize()

    def get(self, *args, **kwargs):
        # self.write("hello ")
        self.render("speaker_notate.html")
