# project/app/__init__.py


import json

import falcon
from celery.result import AsyncResult

from app.tasks import fib


class Ping(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.text = json.dumps('pong!')


class CreateTask(object):

    def on_post(self, req, resp):
        raw_json = req.stream.read()
        result = json.loads(raw_json)
        task = fib.delay(int(result['number']))
        resp.status = falcon.HTTP_200
        result = {
            'status': 'success',
            'data': {
                'task_id': task.id
            }
        }
        resp.text = json.dumps(result)


class CheckStatus(object):

    def on_get(self, req, resp, task_id):
        task_result = AsyncResult(task_id)
        result = {'status': task_result.status, 'result': task_result.result}
        resp.status = falcon.HTTP_200
        resp.text = json.dumps(result)


app = falcon.App()

app.add_route('/ping', Ping())
app.add_route('/create', CreateTask())
app.add_route('/status/{task_id}', CheckStatus())
