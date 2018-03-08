# project/app/__init__.py


import json

import falcon


class Ping(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps('pong!')

app = falcon.API()

app.add_route('/ping', Ping())
