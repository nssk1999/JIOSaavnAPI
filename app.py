import json
import os

import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

import jiosaavn

app = Flask('JIOSaavn API')
CORS(app)

host = "127.0.0.1"
port = 9000
download_location = "downloads"

@app.route("/search")
def search_song():
	#* Args:
	#*		q[required]	: query 
	#*		n			: number of songs per response
	#*		page_num	: page number of response

	query = request.args.get("q", None)
	page_num = request.args.get("page_num", 1)
	result_num = request.args.get("n", 20)

	if query:
		return jsonify(jiosaavn.query_song_by_name(query, page_num, result_num))
	else:
		return jsonify({"error" : True})

@app.route("/details/song")
def song_details():
	#* Args:
	#*		id[required] : ID of the song
	
	id = request.args.get("id", None)
	if id:
		return jiosaavn.query_song_by_id(id)
	else:
		return jsonify({"error" : True})

app.run(host, port, debug=True)
