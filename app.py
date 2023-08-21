from flask import Flask, render_template, request, redirect, url_for
import openai

app = Flask(__name__)

openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    resume = request.files['resume']
    job_description = request.form['job_description']
    context_files = request.files.getlist('context')
    context_text = ''
    for context_file in context_files:
        context_text += f'\n\nAdditional Context:\n{context_file.read().decode('utf-8')}'
    prompt = f'Generate a cover letter based on the following resume, job description, and additional context documents:\n\nResume:\n{resume}\n\nJob Description:\n{job_description}{context_text}'
    response = openai.Completion.create(engine='text-davinci-002', prompt=prompt, max_tokens=150, n=1, stop=None, temperature=0.5)
    cover_letter = response.choices[0].text.strip()
    return render_template('index.html', cover_letter=cover_letter)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
