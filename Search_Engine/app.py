from flask import Flask, render_template


app = Flask(__name__, static_url_path='/static')



def preprocess_text(text):
    #process query
    return text


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def predict():
    subtitles = []
    return render_template('results.html', subtitles=subtitles)



if __name__ == '__main__':
    app.run(debug=True)