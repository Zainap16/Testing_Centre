import plotly.graph_objs as go

def generate_school_student_chart(df):
    # Create a bar chart for number of students per school
    school_student_counts = df.groupby('School_Name')['Learners2022'].sum()
    school_student_chart = go.Bar(x=school_student_counts.index, y=school_student_counts.values)
    school_student_chart_html = go.Figure(school_student_chart).to_html(full_html=False)
    return school_student_chart_html

def generate_district_charts(df):
    # Create separate bar charts for employment status per district
    district_charts_html = {}
    for district, data in df.groupby('District'):
        district_employment_counts = data['Employed'].value_counts()
        district_employment_labels = district_employment_counts.index.tolist()
        district_employment_values = district_employment_counts.values.tolist()
        district_employment_chart = go.Pie(labels=district_employment_labels, values=district_employment_values)
        district_charts_html[district] = go.Figure(district_employment_chart).to_html(full_html=False)
    return district_charts_html
