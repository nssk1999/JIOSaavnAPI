import base64

import requests
from pyDes import ECB, PAD_PKCS5, des

__des_cipher__ = des(b"38346591", ECB, b"\0\0\0\0\0\0\0\0",pad=None, padmode=PAD_PKCS5)

def __generate_media_url__(url):
	url = url.replace("preview", "h")
	url = url.replace("_96_p.mp4", "_320.mp4")
	req = requests.head(url, allow_redirects=True)

	if req.status_code == 403:
		url = url.replace(".mp4", ".mp3")
		return url
	else:
		return req.url

def __decrypt_song_url__(url):
	enc_url = base64.b64decode(url.strip())
	dec_url = __des_cipher__.decrypt(enc_url, padmode=PAD_PKCS5).decode('utf-8')
	dec_url = dec_url.replace("_96.mp4", "_320.mp4")
	req = requests.head(url, allow_redirects=True)

	if req.status_code == 403:
		dec_url = url.replace(".mp4", ".mp3")
		return dec_url
	else:
		return req.url

def __fix_song_title__(title):
	title = title.replace('&quot;', '')
	return title

def query_song_by_name(song_name, page_num = 1, result_num = 20):
	query_base_url = "https://www.jiosaavn.com/api.php?p={page_num}&q={song_name}&_format=json&_marker=0&api_version=4&ctx=web6dot0&n={result_num}&__call=search.getResults".format(song_name = song_name, page_num = page_num, result_num = result_num)
	resp = requests.get(query_base_url)
	songs_json = resp.json()
	songs_data = list()
	
	for song in songs_json["results"]:
		song_data = dict()
		
		song_data["id"] = song["id"]
		song_data["image"] = song["image"]
		song_data["title"] = __fix_song_title__(song["title"])
		song_data["artists"] = list()

		for artist in song["more_info"]["artistMap"]["primary_artists"]:
			song_data["artists"].append(artist["name"])
		
		song_data["artists"] = ", ".join(song_data["artists"])

		songs_data.append(song_data)

	return_json = dict()
	return_json["results"] = songs_data
	return_json["start"] = songs_json["start"]
	return_json["total"] = songs_json["total"]
	
	return return_json

def query_song_by_id(song_id):
	song_base_url = "https://www.jiosaavn.com/api.php?__call=song.getDetails&_marker=0%3F_marker%3D0&_format=json&pids={}".format(song_id)
	song_response = requests.get(song_base_url)
	
	songs_json = song_response.json()

	try:
		songs_json[song_id]['media_url'] = __generate_media_url__(songs_json[song_id]['media_preview_url'])
	except KeyError:
		songs_json[song_id]['media_url'] = __decrypt_song_url__(songs_json[song_id]['encrypted_media_url'])
	
	songs_json[song_id]['song'] = __fix_song_title__(songs_json[song_id]['song'])
	songs_json[song_id]['album'] = __fix_song_title__(songs_json[song_id]['album'])
	songs_json[song_id]['image'] = songs_json[song_id]['image'].replace("150x150", "500x500")

	key_to_pass = ["album", "album_url", "albumid", "duration", "id", "image", "language", "play_count", "release_date", "singers", "song", "year", "media_url"]
	for key in list(songs_json[song_id].keys()):
		if key not in key_to_pass:
			songs_json[song_id].pop(key)

	return songs_json[song_id]
