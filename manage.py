# -*- coding:utf-8 -*-
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.escape
from tornado.options import define, options
from application import APP

define("port", default=8000, help="run port ", type=int)
define("t", default=False, help="creat tables", type=bool)

if __name__ == "__main__":
    options.parse_command_line()
    if options.t:
        # create_talbes.run()
        print("create tables")

    APP.listen(options.port)
    # print 'start server'
    tornado.ioloop.IOLoop.instance().start()
