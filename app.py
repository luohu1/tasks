from celery import Celery

import config

app = Celery('tasks')
app.config_from_object(config)

if __name__ == "__main__":
    app.start()
