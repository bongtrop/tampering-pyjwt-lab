from flask import Flask, request, render_template, redirect, make_response
from gevent.pywsgi import WSGIServer
import jwt

app = Flask(__name__)
SK = open("jwt").read().strip()
PK = open("jwt.pub").read().strip()
FLAG = "flag{What_do_you_like_server_session_or_jwt?}"

@app.route("/")
def index():
    token = request.cookies.get('token')
    flag = "Be the admin to get flag."
    if token:
        data = jwt.decode(token, PK, algorithms=["HS256", "ES256"])
        if data.get("name") == "admin":
            flag = FLAG
    else:
        redirect_to_index = redirect('/')
        response = make_response(redirect_to_index)
        response.set_cookie('token', value=jwt.encode({"name": "chicken_user"}, SK, algorithm="ES256"))
        return response

    return render_template("index.html", flag=flag, name=data.get("name"))

@app.route("/robots.txt")
def robot():
    return app.send_static_file("robots.txt")


if __name__ == "__main__":
    http_server = WSGIServer(('', 1337), app)
    http_server.serve_forever()
