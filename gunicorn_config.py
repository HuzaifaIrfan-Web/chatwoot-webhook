bind = "0.0.0.0:8000"
workers = 4
worker_class = "uvicorn.workers.UvicornWorker"
accesslog = '/app/log/access.log'
errorlog = '/app/log/error.log'
loglevel = 'info'