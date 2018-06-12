Always avoid running your uWSGI instances as root. You can drop privileges using the uid and gid options:

[uwsgi]
https = :9090,foobar.crt,foobar.key
uid = foo
gid = bar
chdir = path_to_web2py
module = wsgihandler
master = true
processes = 8