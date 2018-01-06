"""
fseditserver.py
Author: Abhishek Mishra
6th Jan 2018
"""
from fsevent import *
import json
import importlib

namespaces_and_modules = {
    'bootstrap': None,
}


class RegisterCommand:
    def handle(self, e):
        print('Register command executed')
        p = json.loads(e.payload)
        print(p)
        namespaces_and_modules[p['namespace']] = importlib.import_module('.commands', p['package_name'])

    
default_command_config = {
    'register': RegisterCommand()
}


def log_event(e):
    print(e)


def event(t, ns, c, p):
    e = Event(t, ns, c, p)
    if e.namespace == 'bootstrap':
        default_command_config[e.command].handle(e)
    elif e.namespace in namespaces_and_modules.keys():
        print('Namespace', e.namespace, 'found.')
        m = namespaces_and_modules[e.namespace]
        m.default_command_config[e.command].handle(e)
    else:
        print('Namespace', e.namespace, 'not found')


if __name__ == "__main__":
    event(None, 'bootstrap', 'register', '{"namespace": "root", "package_name": "fsroot"}')
    event(None, 'root', 'start', '')
