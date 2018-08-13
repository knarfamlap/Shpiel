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
        self.response.write('Hello World')
        mainpage_template = jinja_env.get_template('templates/mainpage.html')
        self.response.out.write(mainpage_template.render())
        # Login with google

        user = users.get_current_user()

        if user:
            email_address = user.nickname()
            cssi_user = User.get_by_id(user.user_id())
            signout_link_html = '<a href="%s">sign out</a>' % (
            users.create_logout_url('/'))
      # If the user has previously been to our site, we greet them!
            if cssi_user:
                self.response.write('''
                    Welcome %s %s (%s)! <br> %s <br>''' % (
                    cssi_user.first_name,
                    cssi_user.last_name,
                    email_address,
                    signout_link_html))
          # If the user hasn't been to our site, we ask them to sign up
            else:
                self.response.write('''
                    Welcome to our site, %s!  Please sign up! <br>
                    <form method="post" action="/">
                    <input type="text" name="first_name">
                    <input type="text" name="last_name">
                    <input type="submit">
                    </form><br> %s <br>
                    ''' % (email_address, signout_link_html))
        else:
          self.response.write('''
            Please log in to use our site! <br>
            <a href="%s">Sign in</a>''' % (
              users.create_login_url('/')))

    def post(self):
      user = users.get_current_user()
      if not user:
      # You shouldn't be able to get here without being logged in
        self.error(500)
        return
      cssi_user = CssiUser(
          first_name=self.request.get('first_name'),
          last_name=self.request.get('last_name'),
          id=user.user_id())
      cssi_user.put()
      self.response.write('Thanks for signing up, %s!' %
        cssi_user.first_name)


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
