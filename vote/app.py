from flask import Flask, render_template_string, request, redirect
import redis

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379)

html = """
<!DOCTYPE html>
<html>
<head>
  <title>Voting App</title>
</head>
<body>
  <h2>Vote for your favorite!</h2>
  <form method="POST">
    <button type="submit" name="vote" value="cats">Cats</button>
    <button type="submit" name="vote" value="dogs">Dogs</button>
  </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        vote = request.form["vote"]
        r.rpush("votes", vote)
        return redirect("/")
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

