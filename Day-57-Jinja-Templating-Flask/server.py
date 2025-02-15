from flask import Flask, render_template
import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/<name>')
def predict(name):
    # Gets predicted age for a name from Agify API
    def get_age(name):
        response = requests.get(f"https://api.agify.io?name={name}")
        return response.json() if response.status_code == 200 else None

    # Gets predicted gender for a name from Genderize API
    def get_gender(name):
        response = requests.get(f"https://api.genderize.io?name={name}")
        return response.json() if response.status_code == 200 else None

    # Gets most likely country of origin for a name from Nationalize API
    def get_location(name):
        response = requests.get(f"https://api.nationalize.io?name={name}")
        if response.status_code == 200:
            data = response.json()
            return max(data['country'], key=lambda x: x['probability'])['country_id']
        return None

    # Render template with name predictions
    return render_template('name.html',
                           name=name,
                           age_data=get_age(name),
                           gender_data=get_gender(name),
                         location_data=get_location(name))
@app.route('/')
def home():
    # Generate data for homepage
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template('index.html', num=random_number, year=current_year)
@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/02230a1416e0114489ee"
    response = requests.get(blog_url)   # Get blog data from API
    all_posts = response.json() if response.status_code == 200 else None
    return render_template('blog.html', posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)
