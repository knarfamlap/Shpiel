import webapp2;
import jinja2;

jina_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):



app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
