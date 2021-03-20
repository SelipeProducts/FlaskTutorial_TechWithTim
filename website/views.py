#store standered routes for the website
#where users can go to
#anything not related to authentication but can navigate to

from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db
#Blueprint - has a bunch of organized routes
views = Blueprint('views', __name__)

#route holds url
@views.route('/', methods=['GET', 'POST'])
@login_required
def home(): 
  if request.method == 'POST':
    note = request.form.get('note')
    
    if len(note) < 1:
      flash('Note is too short', category='error')
    else:
      new_note = Note(data=note, user_id= current_user.id )
      db.session.add(new_note)
      db.session.commit()

      flash('Note added', category='success')


  #this function runs when route url is entered
  return render_template('home.html', user=current_user)

