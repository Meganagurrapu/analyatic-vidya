from flask import Flask, render_template, request

app = Flask(__name__)  # Corrected the typo here

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for searching courses
@app.route('/courses', methods=['GET'])
def search_courses():
    query = request.args.get('search')  # Get the search query from the URL
    courses = fetch_courses(query)  # Get courses based on the search query
    return render_template('courses.html', courses=courses, search_query=query)

# Mock function to simulate fetching courses based on search query
def fetch_courses(query):
    courses = []
    if query:
        # Data Science courses
        if "data science" in query.lower():
            courses = [
                {"title": "Data Science Basics", "link": "https://www.example.com/data-science-basics"},
                {"title": "Machine Learning 101", "link": "https://www.example.com/machine-learning-101"},
                {"title": "Python for Data Science", "link": "https://www.example.com/python-for-data-science"},
                {"title": "Deep Learning Specialization", "link": "https://www.example.com/deep-learning-specialization"},
                {"title": "Data Science with R", "link": "https://www.example.com/data-science-with-r"}
            ]
        
        # Python courses
        elif "python" in query.lower():
            courses = [
                {"title": "Python for Beginners", "link": "https://www.example.com/python-for-beginners"},
                {"title": "Advanced Python Programming", "link": "https://www.example.com/advanced-python"},
                {"title": "Automate the Boring Stuff with Python", "link": "https://www.example.com/automate-stuff-python"},
                {"title": "Python for Data Science", "link": "https://www.example.com/python-for-data-science"},
                {"title": "Python Flask Tutorial", "link": "https://www.example.com/python-flask-tutorial"}
            ]
        
        # Web Development courses
        elif "web development" in query.lower():
            courses = [
                {"title": "The Web Developer Bootcamp", "link": "https://www.example.com/web-developer-bootcamp"},
                {"title": "HTML & CSS for Beginners", "link": "https://www.example.com/html-css-for-beginners"},
                {"title": "JavaScript Essentials", "link": "https://www.example.com/javascript-essentials"},
                {"title": "Full Stack Web Development", "link": "https://www.example.com/full-stack-web-dev"},
                {"title": "Responsive Web Design", "link": "https://www.example.com/responsive-web-design"}
            ]
        
        # Machine Learning courses
        elif "machine learning" in query.lower():
            courses = [
                {"title": "Machine Learning with Andrew Ng", "link": "https://www.example.com/ml-andrew-ng"},
                {"title": "Introduction to Machine Learning", "link": "https://www.example.com/introduction-to-ml"},
                {"title": "Machine Learning A-Z", "link": "https://www.example.com/machine-learning-a-z"},
                {"title": "Deep Learning Specialization", "link": "https://www.example.com/deep-learning-specialization"},
                {"title": "Hands-On Machine Learning with Scikit-Learn", "link": "https://www.example.com/hands-on-ml"}
            ]
        
        # Data Analytics courses
        elif "data analytics" in query.lower():
            courses = [
                {"title": "Data Analytics with Python", "link": "https://www.example.com/data-analytics-python"},
                {"title": "Data Analysis and Visualization", "link": "https://www.example.com/data-analysis-visualization"},
                {"title": "Power BI for Beginners", "link": "https://www.example.com/power-bi-for-beginners"},
                {"title": "SQL for Data Analytics", "link": "https://www.example.com/sql-for-data-analytics"},
                {"title": "Google Analytics for Beginners", "link": "https://www.example.com/google-analytics-beginners"}
            ]
        
    return courses

# Corrected condition to run the app
if __name__ == '__main__':
    app.run(debug=True)
