import requests

request = requests.get(url="https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=boolean")
request.raise_for_status()
question_data = request.json()['results']