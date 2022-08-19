import sys

def is_runserver():
    return len(sys.argv) >= 2 and sys.argv[1] == 'runserver'