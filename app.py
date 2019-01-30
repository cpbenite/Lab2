from wsgiref.simple_server import make_server # the wsgiref webserver (default with Python)
from pyramid.config import Configurator

from pyramid.response import Response
from pyramid.response import FileResponse
from pyramid.renderers import render_to_response

''' Basic Routes '''
def home_route(req):
    return FileResponse('home.html')
'''
def linda_route(req):
    return FileResponse('Linda.html')

def zoe_route(req):
    return FileResponse('Zoe.html')

def emily_route(req):
    return FileResponse('Emily.html')

def martha_route(req):
    return FileResponse('Martha.html')
'''
''' Routes using Jinja templating '''

def linda_template_route2(req):
    data = {'message': 'Linda!'}
    return render_to_response('Linda_template.html', data, request=req)

def emily_template_route2(req):
    data = {'message': 'Emily!'}
    return render_to_response('Emily_template.html', data, request=req)

def martha_template_route2(req):
    data = {'message': 'Martha!'}
    return render_to_response('Martha_template.html', data, request=req)

def zoe_template_route2(req):
    data = {'message': 'Zoe!'}
    return render_to_response('Zoe_template.html', data, request=req)

'''
def zoe_template_route(req):
    data = {'count': 1, 'files': ['Zoe.html']}
    return render_to_response('template.html', data, request=req)

def linda_template_route(req):
    data = {'count': 1, 'files': ['Linda_template.html']}
    return render_to_response('template.html', data, request=req)

def emily_template_route(req):
    data = {'count': 1, 'files': ['Emily.html']}
    return render_to_response('template.html', data, request=req)

def martha_template_route(req):
    data = {'count': 1, 'files': ['Martha.html']}
    return render_to_response('template.html', data, request=req)
'''


''' Main Application '''
def main() :
    with Configurator() as config:
        # Home Route
        config.add_route('home', '/')
        config.add_view(home_route, route_name='home')

        # Jinja Routes
        config.include('pyramid_jinja2')
        config.add_jinja2_renderer('.html')

        config.add_route('linda_template2', '/linda_template2')
        config.add_view(linda_template_route2, route_name='linda_template2')

        config.add_route('zoe_template2', '/zoe_template2')
        config.add_view(zoe_template_route2, route_name='zoe_template2')

        config.add_route('martha_template2', '/martha_template2')
        config.add_view(martha_template_route2, route_name='martha_template2')

        config.add_route('emily_template2', '/emily_template2')
        config.add_view(emily_template_route2, route_name='emily_template2')

        # add static folder to search path
        config.add_static_view(name='/', path='./', cache_max_age=3600)

        # create the webserver config
        app = config.make_wsgi_app()

    '''
        # Linda Route
        config.add_route('linda', '/linda')
        config.add_view(linda_route, route_name='linda')

        # Zoe Route
        config.add_route('zoe', '/zoe')
        config.add_view(zoe_route, route_name='zoe')

        # Emily Route
        config.add_route('emily', '/emily')
        config.add_view(emily_route, route_name='emily')

        # Martha Route
        config.add_route('martha', '/martha')
        config.add_view(martha_route, route_name='martha')

        config.add_route('zoe_template', '/zoe_template')
        config.add_view(zoe_template_route, route_name='zoe_template')

        config.add_route('martha_template', '/martha_template')
        config.add_view(martha_template_route, route_name='martha_template')

        config.add_route('emily_template', '/emily_template')
        config.add_view(emily_template_route, route_name='emily_template')
    '''

    # run the server
    server = make_server('127.0.0.2', 8080, app)
    print("The server is now running on: http://127.0.0.2:8080")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)

if __name__ == '__main__':
    main()