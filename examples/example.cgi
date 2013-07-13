#!/usr/bin/python

from cgi_app import CGI_Application

class Example_App(CGI_Application):
    def setup(self):
        self.start_mode = 'welcome'
    def welcome(self):
        return self.template("welcome.tmpl",{})
    def param_example_form(self):
        return self.template("param_example_form.tmpl",{})
    def param_example(self):
        name = self.param('name')
        return self.template("param_example.tmpl",{'name' : name})
    def cookie_example(self):
        self.set_cookie("fig","newton")
        self.set_cookie("foo","bar",path="/")
        return self.template("cookie_example.tmpl",{})
    def redirect_example(self):
        self.redirect("http://www.google.com/")

# this could be run as a mod_python handler:
def handler(req):
    e = Example_App(req)
    return e.run()

# or as a regular CGI app...
if __name__ == "__main__":
    e = Example_App()
    e.run()
