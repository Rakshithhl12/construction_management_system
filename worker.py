from flask import Flask, render_template, request, redirect, flash, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = '234'  # Required for flashing messages

# MySQL Configuration
mysql_config = {
    'host': 'localhost',
    'user': 'Rakshith',  # Replace with your MySQL username
    'password': 'Rakshith@123',  # Replace with your MySQL password
    'database': 'construction_management_system'  # Replace with your database name
}

# Database connection function
def get_db_connection():
    return mysql.connector.connect(**mysql_config)

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


@app.route('/add_worker', methods=['POST'])
def add_worker():
    # Retrieve form data
    worker_name = request.form['workerName']
    worker_id = request.form['workerId']
    department = request.form['department']
    contact_number = request.form['contactNumber']
    date_of_joining = request.form['dateOfJoining']
    worker_status = request.form['workerStatus']
    salary = request.form['salary']
    performance_rating = request.form.get('performanceRating', None)  # Optional field

    try:
        # Establish database connection
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert worker data into the database
        query = """
        INSERT INTO workers (worker_name, worker_id, department, contact_number, date_of_joining, worker_status, salary, performance_rating)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        data = (worker_name, worker_id, department, contact_number, date_of_joining, worker_status, salary, performance_rating)

        cursor.execute(query, data)
        conn.commit()

        # Flash success message
        flash('Worker added successfully!', 'success')

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        flash('An error occurred while adding the worker. Please try again.', 'error')

    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('workers'))

if __name__ == '__main__':
    app.run(debug=True, port=8230)
