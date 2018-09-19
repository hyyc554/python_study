from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello</h1>']


httpd = make_server('', 8080, application)
print('Serving HTTP on 8000...')
# 开始监听HTTP请求
httpd.serve_forever()
