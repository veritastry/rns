# coding=utf-8
import os

DB_CFG = {
    'host': '127.0.0.1',
    'port': '3306',
    'db': 'asrnotation',
    'user': 'root',
    'pass': '123456',
}

SITE_CFG = {
    'site_url': 'http://0.0.0.0:8888',
    'cookie_secret': '123456',
}
SITE_ROOT = os.path.abspath(os.path.dirname(__file__))

setting = dict(
    debug=True,  # 设置debug启动方式
    template_path=os.path.join(SITE_ROOT, 'templates'),  # 设置模板路径
    static_path=os.path.join(SITE_ROOT, 'static'),  # 设置静态文件路径
    login_url="/login",  # 重定向到登录页面
    # packet的配置
    pycket={
        "engine": "mysql",  # 配置存储类型
        "storage": {
            "host": "localhost",
            "port": 3306,
            "db_sessions": 5,
            "db_notifications": 11,
            "max_connections": 2**31
        },
        "cookies": {
            "expires_days": 30,
            "max_age": 360
        }
    },
    cookie_secret="aaa",
    xscf_cookies=True)
