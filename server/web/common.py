# This file will be imported to other files as it requires the library imports, database connection and other important aspects
# required for the project

# Tornado and Motor library required for our backend. Can Import libraries required for your backend at this section
from typing import Text
from tornado.httputil import HTTPMessageDelegate
import tornado.ioloop
import tornado.web
import motor.motor_asyncio
import json
import sys
import re
from bson import ObjectId
import mimetypes
import time
import os
import requests
import jwt

# --> uploadUrl = "https://icfai.com/uploads"
uploadUrl = r"file:///D:/icfai/uploads"
# --> imgPath = "../uploads" --> https://icfai.com/uploads/3298392893.png
imgPath = r"D:/icfai/uploads/"
if os.path.isdir(imgPath) == False:
    os.makedirs(imgPath)

# Creating database connection and initializing databases and tables required for your backend
client = motor.motor_asyncio.AsyncIOMotorClient("127.0.0.1", 27017)
prithvi = client['prithvi']
users = prithvi['users']
products = prithvi['products']
search_history = prithvi['search_history']
