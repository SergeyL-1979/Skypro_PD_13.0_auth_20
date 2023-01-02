#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path

# ==== ИМПОРТИРУЕМ load_dotenv ====
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# ==== АКТИВАЦИЯ БИБЛИОТЕКИ python-dotenv ====
load_dotenv(override=True)
# load_dotenv(os.path.join(basedir, ".flaskenv"))


class Config:
    DEBUG = True
    SERVER_NAME = '127.0.0.1:10100'
    JSON_AS_ASCII = False
    # === МОЖНО ИСПОЛЬЗОВАТЬ ВАРИАНТА =======
    # SECRET_KEY = os.getenv('SECRET_KEY')
    # === ИЛИ ВОТ ТАКОЙ ВАРИАНТ =============
    SECRET_KEY = os.environ.get('SECRET_KEY')  # Так и не пойму как генерить данный код для сессии?
    SQLALCHEMY_DATABASE_URI = "sqlite:///movies.db"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'order.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
