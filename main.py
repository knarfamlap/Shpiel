import webapp2;
import jinja2;
import os

jina_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello World')


class News(webapp2.RequestHandler):
    def get(self):

        

class Sports(webapp2.RequestHandler):
    def get(self):



class Tech(webapp2.RequestHandler):
    def get(self):



class FeelGood(webapp2.RequestHandler):
    def get(self):



class Business(webapp2.RequestHandler):
    def get(self):



class Caleb(webapp2.RequestHandler):
    def get(self):



class Books(webapp2.RequestHandler):
    def get(self):



class Education(webapp2.RequestHandler):
    def get(self):




app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/news', News),
    ('/sports', Sports),
    ('/tech', Tech),
    ('/feelgood', FeelGood),
    ('/business' Business),
    ('/celeb', Caleb),
    ('/books', Books),
    ('/education', Education)
], debug=True)
