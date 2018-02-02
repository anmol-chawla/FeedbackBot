from flask import Flask
from flask import request
from flask import jsonify
from flask import abort
from flask import make_response
from datetime import datetime
from datetime import timezone
import uuid
import models as dbHandler
import chatbot

app = Flask(__name__)


@app.route('/talk/bot', methods=['POST'])
def getResponse():
    if not request:
        abort(404)
    query = request.form['query']
    response = chatbot.getResponse(query)
    uid = uuid.uuid4()
    timeStamp = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S %Z")
    items = {
        'Query': query,
        'Response': response,
        'UUID': uid,
        'Time': timeStamp
    }
    dbHandler.insertQueries(str(uid), timeStamp, query, response)
    return jsonify({'Items': items})


@app.route('/talk/all', methods=['GET'])
def getAll():
    feedbacks = dbHandler.retrieveFeedback()
    return jsonify({'Response': feedbacks})


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'ERROR': 'not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
