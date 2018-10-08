#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This is second try"""
import random
import os
import tornado.web
import tornado.httpserver
import tornado.ioloop


ssl_options = {
    "certfile":os.path.join("Desktop/Tornado_study/test.crt"),
    "keyfile":os.path.join("study.key")}


class MainHandler(tornado.web.RequestHandler):
    """Request handler for the main page of the app localhost:1025"""
    def get(self):
        """Information about server which returns with  HTTP Get"""
        self.render("MainPage.html")
    def post(self):
        """Post function"""
        if self.get_argument('User') == "U" and self.get_argument('Password') == "R":
            self.write("Ok")
            self.redirect("/random")
        else:
            self.write("Nope")

class MathHandler(tornado.web.RequestHandler):
    """Request handler for random page"""
    def get(self):
        """get function"""
        self.write("Random !!!")
        self.write("\n")
        self.write(str(random.randint(0, 1000)))
    def post(self):
        """Post function"""
        self.write(str(random.randint(0, 1000)))

def make_app():
    """Make app with two pages main and random"""
    return tornado.web.Application([(r"/", MainHandler), (r"/random", MathHandler)])

if __name__ == "__main__":
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app, ssl_options)
    app.listen(1025)
    tornado.ioloop.IOLoop.current().start()
