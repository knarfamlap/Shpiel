import webapp2;
import jinja2;
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello World')
        mainpage_template = jinja_env.get_template('templates/mainpage.html')
        self.response.out.write(mainpage_template.render())

class News(webapp2.RequestHandler):
    def get(self):
        self.response.write('news')
        news_template = jinja_env.get_template('templates/news.html')
        self.response.out.write(news_template.render())


class Sports(webapp2.RequestHandler):
    def get(self):
        self.response.write('sports')
        sports_template = jinja_env.get_template('templates/sports.html')
        self.response.out.write(sports_template.render())


class Tech(webapp2.RequestHandler):
    def get(self):
        self.response.write('tech')
        tech_template = jinja_env.get_template('templates/tech.html')
        self.response.out.write(tech_template.render())


class FeelGood(webapp2.RequestHandler):
    def get(self):
        self.response.write('feelgood')
        feelgood_template = jinja_env.get_template('templates/feelgood.html')
        self.response.out.write(feelgood_template.render())

class Business(webapp2.RequestHandler):
    def get(self):
        self.response.write('business')
        business_template = jinja_env.get_template('templates/business.html')
        self.response.out.write(business_template.render())



class Caleb(webapp2.RequestHandler):
    def get(self):
        self.response.write('caleb')
        caleb_template = jinja_env.get_template('templates/caleb.html')
        self.response.out.write(caleb_template.render())


class Books(webapp2.RequestHandler):
    def get(self):
        self.response.write('books')
        books_template = jinja_env.get_template('templates/books.html')
        self.response.out.write(books_template.render())


class Education(webapp2.RequestHandler):
    def get(self):
        self.response.write('education')
        education_template = jinja_env.get_template('templates/education.html')
        self.response.out.write(education_template.render())



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/news', News),
    ('/sports', Sports),
    ('/tech', Tech),
    ('/feelgood', FeelGood),
    ('/business', Business),
    ('/celeb', Caleb),
    ('/books', Books),
    ('/education', Education)
], debug=True)
