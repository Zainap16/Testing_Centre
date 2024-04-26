from flask import Flask, render_template
from sqlalchemy import create_engine
import pandas as pd
import plotly.graph_objs as go

app = Flask(__name__)

# Define your database connection URI
DB_URI = "postgresql://matric_user:YlFGQ4TUvdU6937gns6IUdflTGoDnvmk@dpg-cokgiiv79t8c73ca77kg-a.oregon-postgres.render.com/matric"

# Function to query data and create charts
def generate_charts():
    try:
        # Create a SQLAlchemy engine
        engine = create_engine(DB_URI)

        # Query data from the database
        df = pd.read_sql_query("SELECT * FROM schools", engine)

        # Create a bar chart for number of students per school
        school_student_counts = df.groupby('School_Name')['Learners2022'].sum()
        school_student_chart = go.Bar(x=school_student_counts.index, y=school_student_counts.values)
        school_student_chart_html = go.Figure(school_student_chart).to_html(full_html=False)

        # Create separate bar charts for employment status per district
        district_charts_html = {}
        for district, data in df.groupby('District'):
            district_employment_counts = data['Employed'].value_counts()
            district_employment_labels = district_employment_counts.index.tolist()
            district_employment_values = district_employment_counts.values.tolist()
            district_employment_chart = go.Pie(labels=district_employment_labels, values=district_employment_values)
            district_charts_html[district] = go.Figure(district_employment_chart).to_html(full_html=False)

        return school_student_chart_html, district_charts_html
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    try:
        # Generate charts
        school_student_chart_html, district_charts_html = generate_charts()

        # Render the template with the charts
        return render_template('index.html', school_student_chart=school_student_chart_html, district_charts_html=district_charts_html)
    except Exception as e:
        return str(e)

@app.route('/number-of-students')
def number_of_students():
    try:
        # Generate charts
        school_student_chart_html, _ = generate_charts()

        # Render the template with the school student chart
        return render_template('number-of-students.html', school_student_chart=school_student_chart_html)
    except Exception as e:
        return str(e)

@app.route('/powerBi')
def powerbi():
    try:

        # Render the template
        return render_template('powerBi.html')
    except Exception as e:
        return str(e)


@app.route('/employment-status')
def employment_status():
    try:

        # Render the template with the district charts
        return render_template('employment-status.html', district_charts_html=district_charts_html)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
