from flask import Flask, request
from flask import render_template, Response

from interpreter import interpreter

from urllib.parse import quote, unquote
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/inter", methods=['GET'])
def inter():
    try:
        bf = request.args.get('bf')

        encodeBf = request.args.get('encodeBf')

        print("encodeBf")
    except:
        bf = null
        
        encodeBf = request.args.get('encodeBf')

        print("bf")

    if bf:
        return render_template("interprete.html")
    elif encodeBf:
        print("in")
        bf = str(encodeBf)
        print("---------\n" + bf + "---------\n")
        bf = unquote(bf)
        bf = bf.replace(" ", "")
        bf = bf.replace("\n", "")
        bf = bf.replace("\r", "")

        return render_template("interprete.html", err=interpreter(bf)[0], inp=interpreter(bf)[1])
    else:
        return render_template("inter.html")

@app.route("/test", methods=['GET'])
def test(bf):
    bf = request.args.get('bf')
    return render_template("interprete.html", err=interpreter(bf)[0], inp=interpreter(bf)[1])

@app.route("/api", methods=['GET'])
def api():
    bf = request.query_string.decode()
    bf = bf.replace("bf=","")
    if bf:
        print("1.########" + bf + "########\n")
        bf = bf.replace("%20", "")
        bf = bf.replace("\n", "")
        bf = bf.replace("\r", "")
        bf = bf.replace(" ", "+")
        bf = unquote(bf)
        print("2.########" + bf + "########\n")

        result = interpreter(bf)
        
        if (result[0]):
            return Response(f"Error Found:\n{interpreter(bf)[1]}", mimetype='text/plain')
        else:
            return Response(interpreter(bf)[1], mimetype='text/plain')
    else:

        return Response("Error Found:\n<SyntaxError> No Brainfuck code provided!", mimetype='text/plain')

if __name__ == '__main__':
    app.debug = False
    app.run()
