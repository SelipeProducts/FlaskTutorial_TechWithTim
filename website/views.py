#store standered routes for the website
#where users can go to
#anything not related to authentication but can navigate to

from flask import Blueprint, render_template

#Blueprint - has a bunch of organized routes
views = Blueprint('views', __name__)

#route holds url
@views.route('/')
def home(): 
  #this function runs when route url is entered
  return render_template('home.html')

