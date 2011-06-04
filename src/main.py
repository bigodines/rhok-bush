from tipfy import RequestHandler, Response

class HelloWorldHandler(RequestHandler):
    def get(self):
        return Response('Hello, World!')
