from flask import Flask, jsonify

app = Flask("Useless API server")

@app.route("/<int:size_kb>")
def repos(size_kb):
    return jsonify(["abcd" * 255] * size_kb)
