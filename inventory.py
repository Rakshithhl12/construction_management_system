from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = '13'  # Change to a strong secret key

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


# Inventory Submission Route
@app.route('/submit_inventory', methods=['POST'])
def submit_inventory():
    try:
        # Collect form data
        item_name = request.form['itemName']
        category = request.form['category']
        quantity = request.form['quantity']
        unit = request.form['unit']
        supplier = request.form['supplier']
        purchase_date = request.form['purchaseDate']
        expiry_date = request.form['expiryDate']
        description = request.form['description']

        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert data into the inventory table
        query = """
            INSERT INTO inventory (item_name, category, quantity, unit, supplier, purchase_date, expiry_date, description)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (item_name, category, quantity, unit, supplier, purchase_date, expiry_date, description))
        conn.commit()

        # Provide success feedback to the user
        flash("Inventory item added successfully!", "success")
        return redirect(url_for('inventory'))

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        flash("Failed to add inventory item. Please try again.", "error")
        return redirect(url_for('inventory'))

    finally:
        if conn:
            cursor.close()
            conn.close()


if __name__ == '__main__':
    app.run(port=7003, debug=True)
