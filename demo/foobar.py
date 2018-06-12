# !/bin/python
# -*- coding:utf-8 -*-

# application is the default name which uwsgi will search for.
# run : 
# 	uwsgi --http :9090 --wsgi-file foobar.py
# 	
# 	Do not use --http when you have a frontend webserver or you are doing some form of benchmark, use --http-socket. Continue reading the quickstart to understand why.
# 	
# run :
# 	uwsgi --http :9090 --wsgi-file foobar.py --master --processes 4 --threads 2
# This will spawn 4 processes (each with 2 threads), a master process (will respawn your processes when they die) and the HTTP router (seen before).
# 
# run : 
# 	... --stats 127.0.0.1:9191
# 	The stats subsystem allows you to export uWSGI’s internal statistics as JSON:
# 	We could use telnet or uwsgitop to touch it.
# 		telnet 127.0.0.1 9191		<== show the stats as JSON
# 		uwsgitop 127.0.0.1:9191		<== more frendly looking
# 		
# run with Django:
# 	... --chdir /home/foobar/myproject/ <== we move to a specific directory
# 	
# we can also put all these things into a config file, like uwsgi.ini, then run "uwsgi uwsgi.ini"
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]