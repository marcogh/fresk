# coding: utf-8

import os

bind = 'unix:/var/www/api/api.sock'
backlog = 2048
workers = 1
worker_class = 'gevent'
worker_connections = 1000
threads = 12
timeout = 30 
graceful_timeout = 10
keepalive=2
spew = False
daemon = False
pidfile = None
user = None
group = None
tmp_upload_dir = None
proc_name = None
