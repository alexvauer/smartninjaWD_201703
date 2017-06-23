#!/usr/bin/env python
import datetime
import os
import random
import jinja2
import webapp2
import cgi

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

        params['css-nav'] = ''
        params['navbar'] = ''
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
        params = {'currenttime': tt[11:19]}
        return self.render_template("time.html", params=params)


class LotteryHandler(BaseHandler):
    def lottery(self, numbers):
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
        lottery_numbers = sorted(self.lottery(lottonumbers))
        params = {'lottery_numbers': lottery_numbers}
        return self.render_template("lottery.html", params=params)


class CalcHandler(BaseHandler):
    def get(self):
        return self.render_template("calculator.html")

    def post(self):
        try:
            result = ""
            fail = []
            number1 = float(self.request.get("number1"))
            number2 = float(self.request.get("number2"))
            operator = self.request.get("operation")

            if not number1:
                if number1 != 0:
                    fail.append("Type in Number 1")

            if not operator:
                operator = "?"
                result = "?"
                fail.append("Choose an operator")

            if not number2:
                if number2 != 0:
                    fail.append("Type in Number 2")

            if operator == "add":
                result = number1 + number2
                operator = "+"

            if operator == "sub":
                result = number1 - number2
                operator = "-"

            if operator == "multi":
                result = number1 * number2
                operator = "x"

            if operator == "divi":
                operator = "/"
                if number2 == 0:
                    fail.append("Div through 0")
                    result = "?"
                else:
                    result = number1 / number2

            params = {"number1": str(number1), "number2": str(number2), "result": str(result), "operator": operator,
                      "fail": fail}
            return self.render_template("calculator.html", params=params)
        except:
            result = ""
            fail = []
            number1 = self.request.get("number1")
            number2 = self.request.get("number2")
            operator = self.request.get("operation")

            if not number1:
                fail.append("Type in Number 1")
                number1 ="?"
                if number2:
                    number2 = float(number2)

            if not operator:
                operator = "?"
                result = "?"
                fail.append("Choose an operator")


            if not number2:
                fail.append("Type in Number 2")
                number2 = "?"
                if number1:
                    number1 = float(number1)


            params = {"number1": str(number1), "number2": str(number2), "result": str(result), "operator": operator,
                      "fail": fail}
            return self.render_template("calculator.html", params=params)

class SecretHandler(BaseHandler):
    def get(self):
        return self.render_template("secretnumber.html", params={'first': 1})

    def post(self):
        lowerBound = 1
        upperBound = 45

        secret = random.randint(lowerBound, upperBound)

        try:
            number = int(self.request.get("number1"))

            if int(number) == secret:
                right = 1
                fail = ""

            elif 1 < int(number) > 45:
                right= 0
                fail = "Insert a number between 1 and 45"

            else:
                right = 0
                fail =""

            params = {"right":right, "secret": secret, 'number': number, 'fail':fail}
            return self.render_template("secretnumber.html", params=params)

        except:
            right = 0
            fail = "Please type in numbers"
            params = {"right":right, "secret": secret, 'fail':fail}
            return self.render_template("secretnumber.html", params=params)


class SecretFollowHandler(BaseHandler):
    def post(self):

        secret = int(self.request.get("secret"))

        try:
            number = int(self.request.get("number1"))

            if int(number) == secret:
                right = 1
                fail = ""

            elif int(number) > 45:
                right= 0
                fail = "Insert a number between 1 and 45"
            elif int(number) < 1:
                right= 0
                fail = "Insert a number between 1 and 45"

            else:
                right = 0
                fail = ""

            params = {"right": right, "secret": secret, 'number': number, 'fail': fail}
            return self.render_template("secretnumber.html", params=params)

        except:
            right = 0
            fail = "Please type in numbers"
            params = {"right": right, "secret": secret, 'fail': fail}
            return self.render_template("secretnumber.html", params=params)

class ConvertHandler(BaseHandler):
    def get(self):
        return self.render_template("convert.html")

    def post(self):
        con_mikm = 0.621371
        con_kmmi = 1.60934


        kilometers = self.request.get("kilometer")
        miles = self.request.get("miles")

        if kilometers and not miles:
            miles = float(kilometers)*con_mikm
            kilometers = float(kilometers)
            kilometers2 = 0
            miles2 = 0

        elif miles and not kilometers:
            kilometers = float(miles)*con_kmmi
            miles = float(miles)
            kilometers2=0
            miles2=0

        elif miles and kilometers:
            kilometers2 = float(miles) * con_kmmi
            miles2 = float(kilometers) * con_mikm
            miles = float(miles)
            kilometers = float(kilometers)

        elif not miles and not kilometers:
            kilometers = 0
            miles = 0
            kilometers2 = 0
            miles2 = 0

        params = {'kilometer': round(kilometers,2), 'miles': round(miles,2), 'kilometers2': kilometers2, 'miles2':miles2 }
        return self.render_template("convert.html", params=params)


html_escape_table = {
        "&": "&amp;",
        '"': "&quot;",
      "'": "&apos;",
        ">": "&gt;",
        "<": "&lt;",
        }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


class GuestbookHandler(BaseHandler):
    def get(self):
        messages = GMessages.query().fetch()
        params = {"messages": messages}
        return self.render_template("guestbook.html", params=params)

    def post(self):
        message = html_escape(self.request.get("g_text"))
        name = html_escape(self.request.get("g_name"))
        email = html_escape(self.request.get("g_email"))

        if not name:
            name = "Anonymous"

        msg = GMessages(text=message, name=name, email=email)
        msg.put()

        messages = GMessages.query().fetch()
        params = {"messages": messages}
        return self.render_template("guestbook.html", params=params)


class EditMessageHandler(BaseHandler):
    def get(self, message_id):
        message = GMessages.get_by_id(int(message_id))
        params = {"message": message}
        return self.render_template("message_edit.html", params=params)

    def post(self, message_id):
        new_text = html_escape(self.request.get("g_text"))
        new_mail = html_escape(self.request.get("g_email"))
        new_name = html_escape(self.request.get("g_name"))
        message = GMessages.get_by_id(int(message_id))
        message.text = new_text
        message.email = new_mail
        message.name = new_name
        message.put()
        return self.redirect_to("msg-list")


class DeleteMessageHandler(BaseHandler):
    def get(self, message_id):
        message = GMessages.get_by_id(int(message_id))
        params = {"message": message}
        return self.render_template("message_delete.html", params=params)

    def post(self, message_id):
        message = GMessages.get_by_id(int(message_id))
        message.key.delete()
        return self.redirect_to("msg-list")




app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/guestbook', GuestbookHandler,name="msg-list"),
    webapp2.Route('/guestbook/message/<message_id:\d+>/edit', EditMessageHandler),
    webapp2.Route('/guestbook/message/<message_id:\d+>/delete', DeleteMessageHandler),
    webapp2.Route('/fakebook', FakebookHandler),
    webapp2.Route('/time', TimeHandler),
    webapp2.Route('/lottery', LotteryHandler),
    webapp2.Route('/calc', CalcHandler),
    webapp2.Route('/secretnumber', SecretHandler),
    webapp2.Route('/secretnumberfollow', SecretFollowHandler),
    webapp2.Route('/convert', ConvertHandler),


], debug=True)
