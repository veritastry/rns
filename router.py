# -*- coding:utf-8 -*-
'''
The router used in App.
'''
from handler.misc.index_handler import IndexHandler
from handler.user.login_handler import LoginHandler
from handler.user.register_handler import RegisterHandler
from handler.notation.notate_asr_handler import NotateAsrHandler
from handler.notation.notate_speaker_handler import NotateSpeakerHandler
from handler.notation.notate_wakeup_handler import NotateWakeupHandler

router = [
    (r'/', IndexHandler, dict()),
    (r'/index', IndexHandler, dict()),
    (r'/login', LoginHandler, dict()),
    (r'/register', RegisterHandler, dict()),
    (r"/notation/asr", NotateAsrHandler, dict()),
    (r"/notation/wakeup", NotateWakeupHandler, dict()),
    (r"/notation/speaker", NotateSpeakerHandler, dict()),
]
