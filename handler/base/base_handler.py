# coding=utf-8
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        print("BaseHandler initialize")

    #     self.db=dbSession

    # def get_current_user(self):
    #     if self.session.get("username"):
    #         return user_model.by_name(self.session.get("username"))
    #     else:
    #         return None

    # def on_finish(self):
    #     self.db.close()
