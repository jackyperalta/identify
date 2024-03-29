from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room , leave_room, send
# from vision import list_of_objects

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/chat")
def chat():
    username = request.args.get('username')
    room = request.args.get('room')

    if username and room:
        return render_template('chat.html', username=username, room=room)
    else:
        return redirect(url_for('home'))

@socketio.on('join_room')
def handle_join_room_event(data):
    app.logger.info("{} has joined the room {}".format(data['username'], data['room']))
    join_room(data['room'])
    socketio.emit('join_room_announcement', data)

@socketio.on('send_message')
def handle_join_send_message(data):
    app.logger.info("{} has sent a message to the room: {}".format(data['username'], data['room'], data['message']))
    socketio.emit('receive_message', data, room=data['room'])

if __name__ == "__main__":
    socketio.run(app, debug=True)