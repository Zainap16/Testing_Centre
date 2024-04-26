from flask import Flask, render_template
from db_operations import fetch_data_from_database
from chart_generation import generate_school_student_chart, generate_district_charts

app = Flask(__name__)

# Define your database query
DB_QUERY = "SELECT * FROM schools"

# Define the maximum number of rows to fetch from the database
MAX_ROWS = 1000

# Create the Flask application object
app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Fetch data from the database with a limit
        df = fetch_data_from_database(DB_QUERY, limit=MAX_ROWS)

        if df is None:
            raise Exception("Failed to fetch data from the database")

        # Generate charts
        school_student_chart_html = generate_school_student_chart(df)
        district_charts_html = generate_district_charts(df)

        # Render the template with the charts
        return render_template('index.html', school_student_chart=school_student_chart_html,
                               district_charts_html=district_charts_html)
    except Exception as e:
        return str(e)

@app.route('/number-of-students')
def number_of_students():
    try:
        # Fetch data from the database with a limit
        df = fetch_data_from_database(DB_QUERY, limit=MAX_ROWS)

        if df is None:
            raise Exception("Failed to fetch data from the database")

        # Generate school student chart
        school_student_chart_html = generate_school_student_chart(df)

        # Render the template with the school student chart
        return render_template('number-of-students.html', school_student_chart=school_student_chart_html)
    except Exception as e:
        return str(e)



@app.route('/powerBi')
def powerbi():
    try:
        # Render the template for Power BI
        return render_template('powerBi.html')
    except Exception as e:
        return str(e)

@app.route('/erd')
def erd():
    try:
        # Render the template for Power BI
        return render_template('erd.html')
    except Exception as e:
        return str(e)

@app.route('/employment-status')
def employment_status():
    try:
        # Fetch data from the database
        df = fetch_data_from_database(DB_QUERY)

        if df is None:
            raise Exception("Failed to fetch data from the database")

        # Generate district charts
        district_charts_html = generate_district_charts(df)

        # Render the template with the district charts
        return render_template('employment-status.html', district_charts_html=district_charts_html)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=False)
