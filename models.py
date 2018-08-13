from google.appengine.ext import ndb


class User(ndb.Model):
    username = ndb.StringProperty(required=True)
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)


class Comment(ndb.Model):
    comment_owner = ndb.KeyProperty(User)
    comment_body = ndb.StringProperty(required=True)


class Article(ndb.Model):
    title = ndb.StringProperty(required=True)
    body = ndb.StringProperty(required=True)
    # category = ndb.StringProperty(required=True)
    # post_owner = ndb.KeyProperty(User)
    # comments = ndb.KeyProperty(Comment, repeated=True)




class Category(ndb.Model):
    topic = ndb.StringProperty(required=True)
    post = ndb.KeyProperty(Article, repeated=True)
