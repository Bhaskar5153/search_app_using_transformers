from flask import Flask, render_template, request
from transformers import pipeline


app = Flask(__name__)

qa_pipeline = pipeline('question-answering')

with open(file='ar_wiki.txt', mode='r', encoding='utf-8') as f:
    data = f.read()


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/ask', methods=['GET', 'POST'])
def ask():

    question = request.form.get('question')

    if not question:
        return render_template('index.html', answer='Please enter a question')
    

    answer = qa_pipeline(question=question, context=data)
    return render_template('index.html', answer=answer)




if __name__ == '__main__':
    app.run()