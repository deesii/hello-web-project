from flask import Flask, request
import os
app = Flask(__name__)

@app.route("/submit", methods = ["POST"])
def hello_name():
    name_input = request.form["name"]
    message_input = request.form["message"]
    return f"Thanks {name_input}, you sent this message: '{message_input}'"



# # Request:
# POST /submit

# # With body parameters:
# name=Leo
# message=Hello world

# # Expected response (2OO OK):
# Thanks Leo, you sent this message: "Hello world"


@app.route('/wave' , methods = ["GET"])

def wave():
    name = request.args["name"]
    return f"I am waving at {name}"


# Create a new route that responds to requests sent with:

# A method GET
# A path /wave
# A query parameter name
# It should return the text 'I am waving at [NAME]', where [NAME] is replaced by the value of the name query parameter.

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))