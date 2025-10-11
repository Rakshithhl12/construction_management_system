from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = '20'

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'Rakshith',
    'password': 'Rakshith@123',
    'database': 'construction_management_system'
}

@app.route('/')
def index():
    return render_template('index.html')  # Ensure your HTML file exists in the templates folder

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
    return render_template('document.html')

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

# Route to add a task to the database
@app.route('/add_tasks', methods=['POST'])
def add_tasks():
    try:
        # Get form data
        task_name = request.form['taskName']
        task_type = request.form['taskType']
        task_priority = request.form['taskPriority']
        assigned_to = request.form['assignedTo']
        task_status = request.form['taskStatus']
        start_date = request.form['startDate']
        due_date = request.form['dueDate']
        task_description = request.form['taskDescription']

        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert task into the database
        query = """
            INSERT INTO tasks (task_name, task_type, priority, assigned_to, status, start_date, due_date, description)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (task_name, task_type, task_priority, assigned_to, task_status, start_date, due_date, task_description)
        cursor.execute(query, values)
        connection.commit()

        # Close the connection
        cursor.close()
        connection.close()

        # Flash success message
        flash("Task added successfully!", "success")
        return redirect(url_for('tasks'))
    except Exception as e:
        print("Error: ", e)
        flash("An error occurred while adding the task.", "danger")
        return redirect(url_for('tasks'))

# Run the application
if __name__ == '__main__':
    app.run(port=8020, debug=True)
