from multiprocessing import cpu_count
from os import environ


def max_workers():
    return cpu_count() + 1


bind = '127.0.0.1:9000'
max_requests = 10000
worker_class = 'gevent'
workers = max_workers()


def post_fork(server, worker):
    from psycogreen.gevent import patch_psycopg
    patch_psycopg()