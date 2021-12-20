from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login.utils import login_required, current_user
from . import db
from .get_dates import all_dates_current_month, add_event_to_dates

club = Blueprint('club', __name__, template_folder='templates', static_folder='static')


'''
routes for garabage cleanup, exercise, hydration, sleep, diet, house cleaning, money saving, and reduced screen time
'''

@club.route('/garbageCleanup', methods=['GET', 'POST'])
@login_required
def garbageCleanup():
    return render_template('club_templates/garbage_club.html')

@club.route('/exercise', methods=['GET', 'POST'])
@login_required
def exercise():
    return render_template('club_templates/exercise_club.html')

@club.route('/hydration', methods=['GET', 'POST'])
@login_required
def hydration():
    return render_template('club_templates/hydration_club.html')

@club.route('/sleep', methods=['GET', 'POST'])
@login_required
def sleep():
    return render_template('club_templates/sleep_club.html')

@club.route('/diet', methods=['GET', 'POST'])
@login_required
def diet():
    return render_template('club_templates/diet_club.html')

@club.route('/houseCleaning', methods=['GET', 'POST'])
@login_required
def houseCleaning():
    return render_template('club_templates/cleaning_club.html')

@club.route('/moneySaving', methods=['GET', 'POST'])
@login_required
def moneySaving():
    return render_template('club_templates/saving_club.html')

@club.route('/reducedScreenTime', methods=['GET', 'POST'])
@login_required
def reducedScreenTime():
    return render_template('club_templates/screen_club.html')


'''
routes for garabage cleanup, exercise, hydration, sleep, diet, house cleaning, money saving, and reduced screen time calendars
have a separate route for each club but they all use the same calendar template
'''

@club.route('/garbageCleanupCalendar', methods=['GET', 'POST'])
@login_required
def garbageCleanupCalendar():
    return render_template('calendar.html', events=add_event_to_dates(all_dates_current_month(), 'cleanup 500g of garbage'))

@club.route('/exerciseCalendar', methods=['GET', 'POST'])
@login_required
def exerciseCalendar():
    return render_template('calendar.html', events=add_event_to_dates(all_dates_current_month(), 'exercise for 30 minutes'))

@club.route('/hydrationCalendar', methods=['GET', 'POST'])
@login_required
def hydrationCalendar():
    return render_template('calendar.html', events=add_event_to_dates(all_dates_current_month(), 'hydrate for 1 glass of water'))

@club.route('/sleepCalendar', methods=['GET', 'POST'])
@login_required
def sleepCalendar():
    return render_template('calendar.html', events=add_event_to_dates(all_dates_current_month(), 'go to bed at 10:00pm'))

@club.route('/dietCalendar', methods=['GET', 'POST'])
@login_required
def dietCalendar():
    return render_template('calendar.html', events=add_event_to_dates(all_dates_current_month(), 'eat a healthy meal'))

@club.route('/houseCleaningCalendar', methods=['GET', 'POST'])
@login_required
def houseCleaningCalendar():
    return render_template('calendar.html', events=add_event_to_dates(all_dates_current_month(), 'clean the house'))

@club.route('/moneySavingCalendar', methods=['GET', 'POST'])
@login_required
def moneySavingCalendar():
    return render_template('calendar.html', events=add_event_to_dates(all_dates_current_month(), 'save 10 dollars'))

@club.route('/reducedScreenTimeCalendar', methods=['GET', 'POST'])
@login_required
def reducedScreenTimeCalendar():
    return render_template('calendar.html', events=add_event_to_dates(all_dates_current_month(), 'reduce screen time to an hour minutes'))
    
