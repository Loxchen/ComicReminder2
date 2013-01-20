#update.py - Todo search and update data to iB
# coding=UTF-8

import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class ComicDetail(db.Model):
    name = db.StringProperty(required=True)
    url = db.StringProperty(required=True)


class Show(webapp2.RequestHandler):
    def get(self):
#	self.response.out.write('hahah\n')
	template_values = {
	    'comicDetails': ComicDetail.all(),
	}


	template = jinja_environment.get_template('show.html')
	self.response.out.write(template.render(template_values))

	"""
	for comicDetail in ComicDetail.all():
	    self.response.out.write(comicDetail.name + ': ' + comicDetail.url)
	    self.response.out.write(comicDetail)
	    #comicDetail.delete()
	"""

class Add(webapp2.RequestHandler):
    def post(self):
	name = self.request.get('name')
	url = self.request.get('url')
    	c = ComicDetail(key_name = url,
			name = name,
			url = url)
	c.put()
	self.redirect('/show')

	



