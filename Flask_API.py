from distutils.log import debug
from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        "ID": 1,
        "Title": "Buy Grocery",
        "Description": "Milk, Cheese, Pizza",
        "Done": False
    },

    {
        "ID": 2,
        "Title": "Learn Python",
        "Description": "Learn python in 1 week",
        "Done": False
    }
]


@app.route('/')
def HelloWorld():
    return "Hello World"


@app.route("/add-data", methods=["POST"])
def Add_Task():
    if not request.json:
        return jsonify({
            "Status": "Error",
            "Message": "Please provide the data."
        }, 400)

    task = {
        "ID": tasks[-1]["ID"] + 1,
        "Title": request.json["Title"],
        "Description": request.json.get("Description", ""),
        "Done": False
    }

    tasks.append(task)
    return jsonify({
        "Status": "Success",
        "Message": "Task added successfully..."
    })


@app.route("/get-data")
def Get_Task():
    return jsonify({
        "Data": tasks
    })


if __name__ == "__main__":
    app.run(debug=True)
