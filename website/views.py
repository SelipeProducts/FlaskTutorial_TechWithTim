#store standered routes for the website
#where users can go to
#anything not related to authentication but can navigate to

from flask import Blueprint, render_template
from flask_login import login_required, current_user

#Blueprint - has a bunch of organized routes
views = Blueprint('views', __name__)

#route holds url
@views.route('/')
@login_required
def home(): 
  #this function runs when route url is entered
  return render_template('home.html', user=current_user)

