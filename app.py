from wsgiref.simple_server import make_server # the wsgiref webserver (default with Python)
from pyramid.config import Configurator

from pyramid.response import Response
from pyramid.response import FileResponse
from pyramid.renderers import render_to_response

''' Routes '''
def linda_route(req):
  return FileResponse('Linda.html')

def zoe_route(req):
  return FileResponse('Zoe.html')

def emily_route(req):
  return FileResponse('Emily.html')

def martha_route(req):
  return FileResponse('Martha.html')

'''
def template_route(req):
  data = {'message': 'Greetings!'}
  return render_to_response('index2.html', data, request=req)

def template_route2(req):
  data = {'count': 1, 'files': ['msg1.html', 'msg2.html', 'msg3.html']}
  return render_to_response('index3.html', data, request=req)
'''

''' Main Application '''
def main() :
  with Configurator() as config:
    # Linda Route
    config.add_route('linda', '/')
    config.add_view(linda_route, route_name='Linda')

    # Zoe Route
    config.add_route('zoe', '/')
    config.add_view(zoe_route, route_name='Zoe')

    # Emily Route
    config.add_route('emily', '/')
    config.add_view(emily_route, route_name='Emily')

    # Martha Route
    config.add_route('martha', '/')
    config.add_view(martha_route, route_name='Martha')

'''
    # for template_route / template_route2
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')

    config.add_route('template_example', '/template')
    config.add_view(template_route, route_name='template_example')

    config.add_route('template_example2', '/template2')
    config.add_view(template_route2, route_name='template_example2')
'''
    # add static folder to search path
    config.add_static_view(name='/', path='./public', cache_max_age=3600)

    # create the webserver config
    app = config.make_wsgi_app()

  # run the server
  server = make_server('127.0.0.2', 8080, app)
  print("The server is now running on: http://127.0.0.1:8080")
  
  try:
    server.serve_forever()
  except KeyboardInterrupt:
    print("\nExiting...")
    exit(0)

if __name__ == '__main__':
  main()