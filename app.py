from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Python Question App</title>
    <style>
      body { font-family: Arial, sans-serif; background: #f4f4f9; margin: 0; padding: 0; }
      .container { max-width: 600px; margin: 5rem auto; background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.1); }
      input, button { width: 100%; padding: 0.75rem; margin: 0.5rem 0; border-radius: 6px; border: 1px solid #ccc; }
      button { background: #2d7ff9; color: white; border: none; cursor: pointer; }
      button:hover { background: #1e63d1; }
      .answer { margin-top: 1rem; padding: 1rem; background: #eef5ff; border-radius: 8px; }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Python Question App</h1>
      <p>Type your question and submit to see the response.</p>
      <form method="post">
        <input type="text" name="question" placeholder="Ask something..." required>
        <button type="submit">Submit</button>
      </form>
      {% if answer %}
      <div class="answer">
        <strong>Question:</strong> {{ question }}<br>
        <strong>Answer:</strong> {{ answer }}
      </div>
      {% endif %}
    </div>
  </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    question = ''
    answer = ''
    if request.method == 'POST':
        question = request.form.get('question', '').strip()
        if question:
            answer = f'You asked: "{question}". This app is running on Python and Docker!'
    return render_template_string(HTML, question=question, answer=answer)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
