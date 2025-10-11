from flask import Flask, render_template, url_for, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
import logging
import os
from mysql.connector import Error

app = Flask(__name__)

# Enable CORS
CORS(app)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'Rakshith')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'Rakshith@123')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'construction_management_system')

mysql = MySQL(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Route for the dashboard
@app.route('/')
def index():
    return render_template('index.html')

# Other routes for rendering templates
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/budget')
def budget():
    return render_template('budget.html')

@app.route('/workers')
def workers():
    return render_template('workers.html')

@app.route('/incident')
def incident():
    return render_template('incident.html')

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/attendance')
def attendance():
    return render_template('attendance.html')

@app.route('/incrementor')
def incrementor():
    return render_template('incrementor.html')

@app.route('/shopping')
def shopping():
    return render_template('shopping.html')

@app.route('/plan')
def plan():
    return render_template('plan.html')

@app.route('/alert')
def alert():
    return render_template('alert.html')

@app.route('/fr')
def fr():
    return render_template('fr.html')
# Run Flask application
if __name__ == '__main__':
    app.run(debug=True,host="127.0.0.1", port=5001)