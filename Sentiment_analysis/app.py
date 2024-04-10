from flask import Flask, render_template, request
import  re
import joblib

app = Flask(__name__, static_url_path='/static')


model = joblib.load('model\naive_bayes.pkl')


def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove special characters, punctuation, and extra whitespaces
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text


@app.route('/')
def home():
    render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        
        review = request.form['review']
        # Preprocess the input review
        processed_review = preprocess_text(review)
        # Use the best model to predict the sentiment
        prediction = best_model.predict([processed_review])[0]
        # Map prediction to sentiment label
        sentiment = "Positive" if prediction == 'Positive' else "Negative"
        return render_template('results.html', sentiment=sentiment, review=review)



if __name__ == '__main__':
    app.run(debug=True)