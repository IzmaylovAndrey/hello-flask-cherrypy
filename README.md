# hello-flask-cherrypy
Test project for issue <https://github.com/cherrypy/cherrypy/issues/1662>

Flask application that's served by CherryPy as WSGI server

By default server runs on 0.0.0.0:5000

## Run server:

- Flask development server:
```bash
python run.py
```

- CherryPy WSGI server:
```bash
python server.py
```

## Requirements
- Python 3.5
- Flask 0.12
- CherryPy 12.0.0

## Endpoints
- '/' 

returns 200 on GET
- '/hello?name=\<string:name\>, where name param is not required

returns "Hello, \<name\>! Nice to meet you!" with 200 code

_**To this endpoint you should send OPTIONS request**_

## Docker image

<https://hub.docker.com/r/andreyizmaylov/hello-flask-cherrypy/>
