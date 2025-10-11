from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = '12'  # Replace with a strong secret key

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'Rakshith',  # Replace with your MySQL username
    'password': 'Rakshith@123',  # Replace with your MySQL password
    'database': 'construction_management_system'  # Replace with your database name
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

# Incident Reporting Route
@app.route('/report_incident', methods=['POST'])
def report_incident():
    try:
        # Collect form data
        incident_title = request.form['incidentTitle']
        incident_date = request.form['incidentDate']
        location = request.form['location']
        incident_type = request.form['incidentType']
        incident_description = request.form['incidentDescription']
        affected_workers = request.form['affectedWorkers']
        incident_severity = request.form['incidentSeverity']
        reported_by = request.form['reportedBy']
        incident_resolution = request.form.get('incidentResolution', '')  # Optional field

        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert data into the incidents table
        query = """
            INSERT INTO incidents (title, date, location, type, description, affected_workers, severity, reported_by, resolution)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (incident_title, incident_date, location, incident_type,
                               incident_description, affected_workers,
                               incident_severity, reported_by, incident_resolution))
        conn.commit()

        # Provide success feedback to the user
        flash("Incident reported successfully!", "success")
        return redirect(url_for('incident'))

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        flash("Failed to report the incident. Please try again.", "error")
        return redirect(url_for('incident'))

    finally:
        if conn:
            cursor.close()
            conn.close()

# Run the application
if __name__ == '__main__':
    app.run(port=5005, debug=True)
