from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["fintrack"]
collection = db["transactions"]


@app.route("/transactions", methods=["GET"])
def get_transactions():

    transactions = []

    for item in collection.find():
        transactions.append({
            "_id": str(item["_id"]),
            "title": item["title"],
            "amount": item["amount"],
            "type": item["type"]
        })

    return jsonify(transactions)


@app.route("/transactions", methods=["POST"])
def add_transaction():

    data = request.json

    transaction = {
        "title": data["title"],
        "amount": data["amount"],
        "type": data["type"]
    }

    result = collection.insert_one(transaction)

    return jsonify({
        "message": "Transaction Added",
        "id": str(result.inserted_id)
    })


@app.route("/transactions/<id>", methods=["DELETE"])
def delete_transaction(id):

    collection.delete_one({
        "_id": ObjectId(id)
    })

    return jsonify({
        "message": "Transaction Deleted"
    })


if __name__ == "__main__":
    app.run(debug=True)
