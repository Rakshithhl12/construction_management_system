from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = '11'

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'Rakshith',  # Replace with your MySQL username
    'password': 'Rakshith@123',  # Replace with your MySQL password
    'database': 'construction_management_system'
}

  # Your HTML form file
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


@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    try:
        # Collect form data
        feedback_title = request.form['feedbackTitle']
        feedback_rating = request.form['feedbackRating']
        feedback_description = request.form['feedbackDescription']
        feedback_author = request.form['feedbackAuthor']
        feedback_email = request.form['feedbackEmail']

        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert data into the feedback table
        query = """
            INSERT INTO feedback (title, rating, description, author, email)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (feedback_title, feedback_rating, feedback_description, feedback_author, feedback_email))
        conn.commit()

        # Provide success feedback to the user
        flash("Feedback submitted successfully!", "success")
        return redirect(url_for('feedback'))

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        flash("Failed to submit feedback. Please try again.", "error")
        return redirect(url_for('index'))

    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(port=8000, debug=True)