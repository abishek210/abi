from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    return "Hello this is my website! <h1>HELLO</h1>"
    
if __name__ == "__main__":
    app.run(host="", port="", debug=True)