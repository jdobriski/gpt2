from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resume = request.files['resume']
        job_description = request.form['job_description']
        # TODO: Process resume and job description
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5001)