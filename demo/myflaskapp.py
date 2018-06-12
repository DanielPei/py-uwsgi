# -*- coding:utf-8 -*-
"""
	uwsgi --http :9090 --wsgi-file myflaskapp.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191

	# --callable app <== specify the server Flask exports its WSGI function as
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<span style='color:red'>I am app 1</span>"