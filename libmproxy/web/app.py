
import os.path
import tornado.web


class Application(tornado.web.Application):
    def __init__(self, debug):
        handlers = [
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            debug=debug,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

