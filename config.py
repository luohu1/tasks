from pathlib import Path

_data = Path(__file__).cwd().joinpath('data')
_backend_folder = _data.joinpath('results')
_backend_folder.mkdir(parents=True, exist_ok=True)

# Broker settings.
broker_url = 'redis://127.0.0.1:6379/6'

# List of modules to import when the Celery worker starts.
imports = ('tasks', )

# Using the filesystem to store task state and results.
result_backend = _backend_folder.as_uri()
