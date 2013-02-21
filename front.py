import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
from tornado.options import define, options
define("port", default=8001, help="run on the given port", type=int)
class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        response = client.fetch("http://www.baidu.com/" ,callback=self.on_response)

    def on_response(self,response):
        self.write(response.body)
        self.finish()

if __name__=='__main__':
    tornado.options.parse_command_line()
    app=tornado.web.Application(handlers=[(r'/',IndexHandler)])
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
