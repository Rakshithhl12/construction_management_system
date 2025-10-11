from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = '13'  # Change this to a strong secret key

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'Rakshith',  # Replace with your MySQL username
    'password': 'Rakshith@123',  # Replace with your MySQL password
    'database': 'construction_management_system'
}

# Routes for navigation
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


# Document Submission Route
@app.route('/submit_document', methods=['POST'])
def submit_document():
    try:
        # Collect form data
        document_title = request.form['documentTitle']
        document_type = request.form['documentType']
        document_date = request.form['documentDate']
        document_description = request.form['documentDescription']
        document_content = request.form['documentContent']
        document_author = request.form['documentAuthor']
        document_status = request.form['documentStatus']

        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert data into the documents table
        query = """
            INSERT INTO documents (document_title, document_type, document_date, document_description,
                                   document_content, document_author, document_status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            document_title, document_type, document_date, document_description,
            document_content, document_author, document_status
        ))
        conn.commit()

        # Provide success feedback to the user
        flash("Document added successfully!", "success")
        return redirect(url_for('documents'))

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        flash("Failed to add document. Please try again.", "error")
        return redirect(url_for('documents'))

    finally:
        if conn:
            cursor.close()
            conn.close()

# Run the app
if __name__ == '__main__':
    app.run(port=7078, debug=True)
