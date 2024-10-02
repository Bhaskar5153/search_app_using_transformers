from transformers import pipeline

qa_pipe_line = pipeline('question-answering')


# load the data

with open(file='ar_wiki.txt', mode='r', encoding='utf-8') as f:
    data = f.read()

# print(data)

def question_answer(question, context):
    result = qa_pipe_line(question=question, context=context)
    return result['answer']


answer = question_answer(question='what is augumented reality?', context=data)

print(f"The answer is:  {answer}")






