#!/usr/bin/env python
import datetime
import os
import random

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
        return self.render_template("index.html")

class FakebookHandler(BaseHandler):
    def get(self):
        return self.render_template("fakebook.html")

class TimeHandler(BaseHandler):
    def get(self):
        tt = str(datetime.datetime.now())
        params = {'currenttime':tt[11:19]}
        return self.render_template("time.html", params=params)

class LotteryHandler(BaseHandler):
    def lottery(numbers):
        lowerBound = 1
        upperBound = 45
        number = 0
        lottery_numbers = []


        if numbers > 45:
            print "Maximum 45 numbers: set to 45"
            numbers = 45

        while number < numbers:
            new_number = random.randint(lowerBound, upperBound)
            if new_number not in lottery_numbers:
                lottery_numbers.append(new_number)
                number += 1

        return lottery_numbers

    def get(self):
        lottonumbers = 6
        lottery_numbers = self.lottery(lottonumbers)
        params = {'lottery_numbers': lottery_numbers}
        return self.render_template("lottery.html", params=params)



class GuestbookHandler(BaseHandler):
    def get(self):
        messages = GMessages.query().fetch()
        params = {"messages": messages}
        return self.render_template("guestbook.html", params=params)

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
        return self.render_template("guestbook.html", params=params)



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/guestbook', GuestbookHandler),
    webapp2.Route('/fakebook', FakebookHandler),
    webapp2.Route('/time', TimeHandler),
    webapp2.Route('/lottery', LotteryHandler)

], debug=True)
