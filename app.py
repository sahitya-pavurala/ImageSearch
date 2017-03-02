import sys
from flask import Flask, render_template, request
from api import get_clarifai_app_object
from resources import load_urls

app = Flask(__name__)
app.config['DEBUG'] = True
c_app = None

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/search")
def search():
    """
    Function to search the Clarifai API
    and tag the images
    :return:
    """
    keyword = request.args.get('keyword')
    results = c_app.inputs.search_by_predicted_concepts(concept=keyword)
    # Clean the results and avoid duplicate urls
    results = list(set([result.url.strip() for result in results]))
    return render_template('search-results.html', results=results)


if __name__ == "__main__":
    path = sys.argv[0]
    urls = load_urls(path)
    c_app = get_clarifai_app_object(urls)
    app.run()
