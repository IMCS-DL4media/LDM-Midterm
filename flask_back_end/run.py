#!/usr/bin/env python

#import datetime
#from datetime import datetime, timedelta

#import os
#import zipfile

#from bson import ObjectId
#from flask import Flask, render_template, send_from_directory
from flask import Flask
#from flask import request
from flask_pymongo import PyMongo
#from flask import jsonify
#from flask import make_response

#import flask_uploads
#from werkzeug.utils import secure_filename
#import jwt

from functools import wraps
import sys

#//////////////////////////////////////////////////////////////APP INITIALIZATION//////////////////////////////////////////////////////////////////////////////////////////////////
from global_vars import get_app, get_mongo, set_app, set_mongo

#uploadedFiles = flask_uploads.UploadSet('files')
#app.config['UPLOADED_FILES_DEST'] = './files'
#app.config['UPLOADED_FILES_URL'] = 'http://localhost:5000/files/'
#app.config['UPLOADS_DEFAULT_URL'] = 'http://localhost:5000/files/'


#flask_uploads.configure_uploads(app, uploadedFiles)




#//////////////////////////////////////////////////////////////END OF APP INITIALIZATION//////////////////////////////////////////////////////////////////////////////////////////////////

##/////

MONGO_URI_LOCAL       = "mongodb://localhost:27017/logging_db"
MONGO_URI_CONTAINER   = "mongodb://mongo:27017/logging_db"
MONGO_URI_LOCAL_paper = "mongodb://localhost:27017/logging_db_raksts"


def setUpDB():
	print("setup db")
	mongo = get_mongo()
	num_of_docs = mongo.db.users.find({}).count()
	if num_of_docs == 0:
		print("users table is empty - inserting ")
		mongo.db.users.insert_one(
			{
				"login":"user1",
				"password":"psw1",
				"name":"User1 Name"
			}
		)
	col = mongo.db.users.find({})
	for e in col:
		print(e)
	print("/setup db")
	return


def init_app(mongo_uri_prm):
	
	#print(app)
	app = Flask(__name__)
	set_app(app)
	#app.config["MONGO_URI"] = "mongodb://mongo:27017/logging_db"
	if mongo_uri_prm != "" :
		print("Using user supplied mongo URI \'" + mongo_uri_prm + "\'")
		app.config["MONGO_URI"] = mongo_uri_prm
	else:
		print("Using default mongo URI \'mongodb://localhost:27017/logging_db\'")
		app.config["MONGO_URI"] = MONGO_URI_LOCAL_paper

	mongo = PyMongo(app)
	set_mongo( mongo )
	app.config['SECRET_KEY'] = 'some-secret-string12345reqfgb'
	#print(app)
	
	#print ( app.url_map )
	setUpDB()
	from routes import start_run


def start_app():
	print ( get_app().url_map )
	get_app().run(debug=True, host = '0.0.0.0')

if __name__ == '__main__':
	mongo_uri_prm = ""
	if len(sys.argv) > 1:
		mongo_uri_prm = sys.argv[1]
	init_app(mongo_uri_prm)
	start_app()



#if __name__ == '__main__':
#    print ( app.url_map )
#    app.run(debug=True)
