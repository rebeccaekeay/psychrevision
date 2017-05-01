from flask import Flask, render_template
app = Flask(__name__, static_url_path="/img", static_folder='img')

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/personality")
def personality():
    return render_template('personality.html')

@app.route("/neuroscience")
def neuroscience():
    return render_template('neuroscience.html')

if __name__ == "__main__":
    app.run()
