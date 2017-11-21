import cherrypy
from app import app

cherrypy.tree.graft(app, '/')

cherrypy.config.update({
    'environment': 'embedded',
    'engine.autoreload.on': False,
    'server.socket_host': '0.0.0.0',
    'server.socket_port': 5000
})


if __name__ == '__main__':
    cherrypy.engine.signals.subscribe()
    try:
        print('Start CherryPy WSGI server on http://{host}:{port}. Press Ctrl+C to stop'.format(
            host='0.0.0.0',
            port=5000
        ))
        cherrypy.engine.start()
    except KeyboardInterrupt:
        cherrypy.engine.exit()
