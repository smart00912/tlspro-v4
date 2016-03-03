#_*_coding:utf-8_*_
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

def simple_app(environ,start_response):
	status='200 OK'
	for k,v in environ.items():                                      #打印浏览器提交的系统信息
		print str(k)+"--->"+str(v)
	response_headers=[('Content-type','text/plain')]
	start_response(status,response_headers)
	return ['Hello world!\n']


if __name__ == '__main__':
	httpd=make_server('',8001,simple_app)
	httpd.serve_forever()