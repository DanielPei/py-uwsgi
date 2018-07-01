import sys
reload(sys)
sys.setdefaultencoding('utf8')



if __name__ == '__main__':
    str = "django.server"
    str = str.decode('utf-8')
    print str
