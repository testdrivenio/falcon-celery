# Falcon + Celery

Example of how to handle background processes with Falcon, Celery, and Docker

### Quick Start

Spin up the containers:

```sh
$ docker-compose up -d
```

Open your browser to http://localhost:8000/ping to view the app or to http://localhost:5555 to view the Flower dashboard.

Trigger a new task:

```sh
$ curl -X POST http://localhost:8000/create \
    -d '{"number":"3"}' \
    -H "Content-Type: application/json"
```

Check the status:

```sh
$ curl http://localhost:8000/status/<ADD_TASK_ID>
```

### Want to learn how to build this?

Check out the [post](https://testdriven.io/asynchronous-tasks-with-falcon-and-celery).
