"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import mlab
from mongoengine import *
from werkzeug.utils import secure_filename
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

app.config["IMG_PATH"] = os.path.join(app.root_path,"static", "img")
mlab.connect()
###
# Routing for your application.
###
class Item(Document):
    image = StringField()
    title = StringField()
    price = FloatField()


# @app.route("/add_bitch", methods=["GET","POST"])
# def add_bitch():
#     if request.method == "GET":
#         return render_template("add_item.html")
#     elif request.method == "POST": #submit form
#         ##Step 1: get data from form
#         form = request.form
#         title = form['title']
#         price = form['price']
#
#         image = request.files['image']
#         filename = secure_filename(image.filename)
#         save_location = os.path.join(app.config["IMG_PATH"], filename)
#         image.save(save_location)
#         ##Step 2: Create data
#         if title == '' or image == '' or price == '':
#             return render_template("666.html")
#         else:
#             item = Item(title=title, image=url_for("image",image_name= filename),price=price)
#             item.save()
#         ##Step 3: Redirect
#         return  redirect(url_for("index"))

@app.route('/')
def index():
    return render_template("index.html",items = Item.objects())

# @app.route('/about/')
# def about():
#     """Render the website's about page."""
#     return render_template('about.html')
#
# @app.route("/images/<image_name>")
# def image(image_name):
#     return send_from_directory(app.config["IMG_PATH"], image_name)
# ###
# # The functions below should be applicable to all Flask apps.
# ###
# @app.route('/<file_name>.txt')
# def send_text_file(file_name):
#     """Send your static text file."""
#     file_dot_text = file_name + '.txt'
#     return app.send_static_file(file_dot_text)
#
#
# @app.after_request
# def add_header(response):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
#     response.headers['Cache-Control'] = 'public, max-age=600'
#     return response
#
#
# @app.errorhandler(404)
# def page_not_found(error):
#     """Custom 404 page."""
#     return render_template('404.html'), 404
#

if __name__ == '__main__':
    app.run(debug=False)
