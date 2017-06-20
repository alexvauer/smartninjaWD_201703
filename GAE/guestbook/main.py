#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import GMessages

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        messages = GMessages.query().fetch()
        params = {"messages": messages}
        return self.render_template("hello.html", params=params)

    def post(self):
        message = self.request.get("g_text")
        name = self.request.get("g_name")
        email = self.request.get("g_email")

        if not name:
            name = "Anonymous"

        msg = GMessages(text=message, name=name, email=email)
        msg.put()

        messages = GMessages.query().fetch()
        params = {"messages": messages}
        return self.render_template("hello.html", params=params)




app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),

], debug=True)
