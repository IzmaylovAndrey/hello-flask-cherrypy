import cheroot.wsgi
from app import app


server = cheroot.wsgi.Server(('0.0.0.0', 5000), app)

if __name__ == '__main__':
    try:
        print('Start CherryPy WSGI server on http://{host}:{port}. Press Ctrl+C to stop'.format(
            host='0.0.0.0',
            port=5000
        ))
        server.safe_start()
    except KeyboardInterrupt:
        server.stop()
