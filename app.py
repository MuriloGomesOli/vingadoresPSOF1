from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/ola")
def hello_world():
    return "<p>olá mundo...<p>"


# from model.interface import Interface

# def main():
#     Interface()



# if __name__ == '__main__':
    
#     main()