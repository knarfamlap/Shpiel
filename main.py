import webapp2;
import jinja2;
import os
from models import User
from models import Article
from models import Comment
from models import Category

from google.appengine.api import users

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        print("hello")
        mainpage_template = jinja_env.get_template('templates/mainpage.html')
        all_articles = Article.query().fetch()
        self.response.out.write(mainpage_template.render({'articles' : all_articles}))

    def post(self):
        ttle = self.request.get('user-title')
        bdy = self.request.get('user-body')
        tp = self.request.get('topic-selector') 
        article = Article(title= ttle, body=bdy, category="news")
        article.put()

class News(webapp2.RequestHandler):
    def get(self):
        self.response.write('news')
        news_post = Article.query().filter(Article.category == 'News').fetch()
        news_template = jinja_env.get_template('templates/news.html')
        self.response.out.write(news_template.render())
        self.response.write(news_post)


class Sports(webapp2.RequestHandler):
    def get(self):
        sports_post = Article.query().filter(Article.category == 'Sports').fetch()
        sports_template = jinja_env.get_template('templates/sports.html')
        self.response.out.write(sports_template.render())
        self.response.write(sports_post)


class Tech(webapp2.RequestHandler):
    def get(self):
        tech_post = Article.query().filter(Article.category == 'Tech').fetch()
        tech_template = jinja_env.get_template('templates/tech.html')
        self.response.out.write(tech_template.render())
        self.response.write(tech_post)


class FeelGood(webapp2.RequestHandler):
    def get(self):
        feelgood_post = Article.query().filter(Article.category == 'FeelGood').fetch()
        feelgood_template = jinja_env.get_template('templates/feelgood.html')
        self.response.out.write(feelgood_template.render())
        self.response.write(feelgood_post)

class Business(webapp2.RequestHandler):
    def get(self):
        business_post = Article.query().filter(Article.category == 'Business').fetch()
        business_template = jinja_env.get_template('templates/business.html')
        self.response.out.write(business_template.render())
        self.response.write(business_post)



class Caleb(webapp2.RequestHandler):
    def get(self):
        caleb_post = Article.query().filter(Article.category == 'Caleb').fetch()
        caleb_template = jinja_env.get_template('templates/celeb.html')
        self.response.out.write(caleb_template.render())
        self.response.write(caleb_post)


class Books(webapp2.RequestHandler):
    def get(self):
        books_post = Article.query().filter(Article.category == 'Books').fetch()
        books_template = jinja_env.get_template('templates/books.html')
        self.response.out.write(books_template.render())
        self.response.write(books_post)


class Education(webapp2.RequestHandler):
    def get(self):
        education_post = Article.query().filter(Article.category == 'Education').fetch()
        education_template = jinja_env.get_template('templates/education.html')
        self.response.out.write(education_template.render())
        self.response.write(education_post)

class Temp(webapp2.RequestHandler):
    def get(self):
        temp_template = jinja_env.get_template('templates/temp.html')
        all_articles = Article.query().fetch()
        self.response.out.write(temp_template.render({'articles' : all_articles}))





app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/news', News),
    ('/sports', Sports),
    ('/tech', Tech),
    ('/feelgood', FeelGood),
    ('/business', Business),
    ('/celeb', Caleb),
    ('/books', Books),
    ('/education', Education),
    ('/temp', Temp)
], debug=True)
