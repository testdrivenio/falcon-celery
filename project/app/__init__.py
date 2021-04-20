# project/app/__init__.py


import json

import falcon


class Ping(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.text = json.dumps('pong!')

app = falcon.App()

app.add_route('/ping', Ping())
