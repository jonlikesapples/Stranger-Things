from flask import Flask, jsonify
import json
import pyrebase

app = Flask(__name__)

#https://github.com/thisbejim/Pyrebase

config = {
  "apiKey": "AIzaSyAb0csAFZDQoYIJrflFTuYAwx7rS1t3oYg",
  "authDomain": "stranger-things-ce12a.firebaseapp.com",
  "databaseURL": "https://stranger-things-ce12a.firebaseio.com/",
  "storageBucket": "stranger-things-ce12a.appspot.com",
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

#get from firebase server
@app.route("/")
def nothing():
	return "WELCOME TO STRANGER THINGS! <br> \
	possible endpoints: <br> /allusers <br> /post <br> /delete"
@app.route("/allusers", methods=['GET'])
def get():
	# queryresult = db.child("users").get().val() #type orderedDict
	# data = json.loads(json.dumps(queryresult)) #type (regular) dict
	# stringdata = json.dumps(data) #type string, no real use for this
	QUERY_RESULT = ""
	dbresult = db.child("users").get() #type orderedDict
	for user in dbresult.each(): 
		QUERY_RESULT += "key: " + str(user.key()) + " " + "val: " + str(user.val()) + "<br>"
	return QUERY_RESULT

@app.route('/post')
def redirect():
	data = {"name": "aang the avatar"}
	age = {"age": "12"}
	db.child("users").child("account2").update(data) #ALWAYS USE .UPDATE to post, will create a new key too
	db.child("users").child("account2").update(age)
	return "posted"

@app.route("/update")
def post(param):
	return "nothing."

@app.route("/delete")
def delete():
	db.child("users").child("account2").remove()
	return "deleted"

if __name__ == '__main__':
    app.run(debug=True)