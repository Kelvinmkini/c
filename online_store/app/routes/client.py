from flask import Blueprint, render_template

client_bp = Blueprint('client', __name__, template_folder='../templates/client')

@client_bp.route('/')
def home():
    return render_template('client/home.html')