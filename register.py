from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = '19'  # Set a secret key for flash messages

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'Rakshith',  # Replace with your MySQL username
    'password': 'Rakshith@123',  # Replace with your MySQL password
    'database': 'construction_management_system'  # Your database name
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
 # Make sure the register.html file exists

@app.route('/submit_register', methods=['POST'])
def submit_register():
    conn = None  # Initialize conn here to ensure it's in scope for the finally block
    cursor = None  # Initialize cursor here to ensure it's in scope for the finally block

    try:
        # Collect form data
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        role = request.form['role']

        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert data into the users table
        query = """
            INSERT INTO users (name, email, password, phone, role)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, email, password, phone, role))
        conn.commit()

        # Provide success feedback to the user
        flash("Registration successful!", "success")
        return redirect(url_for('register'))  # Redirect back to the register page after successful registration

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        flash("Registration failed. Please try again.", "error")
        return redirect(url_for('register'))  # Redirect back to the register page in case of an error

    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(port=8060, debug=True)
