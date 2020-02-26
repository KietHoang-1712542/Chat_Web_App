from flask import Flask, render_template, url_for, redirect, request, session, jsonify
from client import Client
from threading import Thread
import time

NAME_KEY = 'name'

client = None
messages = []

app = Flask(__name__)
app.secret_key = "helloeveryoneiloverealmadrid"

def disconnect():
    """
    call this before the client disconnect from server
    :return:
    """
    global client
    if client:
        client.disconnect()

@app.route("/login", methods=["POST", "GET"])
def login():
    """
    display main login page and handles saving name in session
    :return: None
    """
    if request.method == "POST":
        session[NAME_KEY] = request.form["inputName"]
        return redirect(url_for("home"))
    return render_template("login.html", **{"session": session})


@app.route("/logout")
def logout():
    """
    logs the user out by popping name from session
    :return:
    """
    session.pop(NAME_KEY, None)
    return redirect(url_for("login"))


@app.route("/")
@app.route("/home")
def home():
    """
    display homepage if logged in
    :return: None
    """
    global client

    if NAME_KEY not in session:
        return redirect(url_for("login"))

    client = Client(session[NAME_KEY])

    return render_template("index.html", **{"login": True, "session": session})


@app.route("/send_message")
def send_message():
    """
    called from JQuery to send messages
    :return:
    """
    global client
    msg = request.args.get("val")
    if client:
        client.send_message(msg)


    return "None"


@app.route("/get_messages")
def get_messages():
    return jsonify({"messages": messages})


def update_messages():
    """
    updates the local list of messages
    :return: None
    """
    global messages

    run = True
    while run:
        time.sleep(0.1) # update every 1/10 of a second
        if not client:
            continue
        new_messages = client.get_messages()    # get any new messages from client
        messages.extend(new_messages)   # add to local list of messages
        #messages = new_messages[:]

        for msg in new_messages:    # display new messages
            if msg == "{quit}":
                run = False
                break


if __name__ == "__main__":
    Thread(target=update_messages).start()
    app.run(debug=True, host='0.0.0.0')