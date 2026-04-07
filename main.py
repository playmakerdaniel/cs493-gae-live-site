from flask import Flask, request, render_template_string

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>GAE Live Greeting App</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 760px;
      margin: 40px auto;
      padding: 0 16px;
      line-height: 1.5;
    }
    .card {
      border: 1px solid #ddd;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    input, button {
      padding: 10px;
      font-size: 16px;
      margin-top: 8px;
    }
    input {
      width: 100%;
      max-width: 360px;
      box-sizing: border-box;
    }
    button {
      cursor: pointer;
    }
    .result {
      margin-top: 18px;
      padding: 12px;
      background: #f6f8fa;
      border-radius: 8px;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>Google App Engine Live Greeting App</h1>
    <p>This site is hosted on Google App Engine and uses server-side Python to respond to form submissions.</p>

    <form method="post" action="/greet">
      <label for="name">Enter your name:</label><br>
      <input id="name" name="name" type="text" required>
      <br>
      <button type="submit">Send to server</button>
    </form>

    {% if message %}
      <div class="result">
        <strong>Server response:</strong>
        <p>{{ message }}</p>
      </div>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(PAGE, message=None)

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name", "Guest").strip()
    if not name:
        name = "Guest"
    message = f"Hello, {name}! Your request was processed by the Python server on Google App Engine."
    return render_template_string(PAGE, message=message)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)