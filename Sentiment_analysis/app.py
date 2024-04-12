from flask import Flask, render_template, request
import  re
import joblib

app = Flask(__name__, static_url_path='/static')


model = joblib.load('model/naive_bayes.pkl')


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        processed_review = preprocess_text(review)
        prediction = model.predict([processed_review])[0]
        sentiment = "Positive" if prediction == 'Positive' else "Negative"
        return render_template('results.html', sentiment=sentiment, review=review)
    else:
        return render_template('home.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0")