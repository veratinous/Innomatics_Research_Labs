from flask import Flask, render_template, request
import re

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/regex', methods=['GET','POST'])
def regex():
    if request.method == 'POST':
        string = request.form['string']
        pattern = request.form['pattern']
        results = re.findall(pattern, string)
        num_match = len(results)
        return render_template('regex.html', string=string, pattern=pattern, results=results, num_match=num_match)
    else:
         return render_template('regex.html')
    

@app.route('/email', methods=['GET','POST'])
def email():
    if request.method == 'POST':
            email = request.form['email']
            regex_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

            # performing regex matching to validate email
            is_valid_email = re.match(regex_pattern, email) is not None

            return render_template('email.html', email=email, is_valid_email=is_valid_email)
    else:
        return render_template('email.html')

       

if __name__ == '__main__':
    app.run(debug=True)
