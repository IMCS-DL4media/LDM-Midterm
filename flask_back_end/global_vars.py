#!/usr/bin/env python

module_local_app = None
module_local_mongo = None


def set_app(new_val):
	global module_local_app
	module_local_app = new_val

def get_app():
	return module_local_app

def set_mongo(new_val):
	global module_local_mongo
	module_local_mongo = new_val

def get_mongo():
	return module_local_mongo
