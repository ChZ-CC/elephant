# -*- coding: utf-8 -*-
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'zdg8d9h78tuoi2u3o4ih'
