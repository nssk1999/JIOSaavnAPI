# JioSaavn API v1
JioSaavn API implemented in Python using Flask

## Features:
#### Currently the API can serve the following queries:

- **Search for Songs**
- **Details of a Song with download URL**
- .... a lot will be added in future

## Usage:
- **Searching Songs: /search?q=photograph&n=2&page_num=1**
	- **Parameters**
		- q: query [required]
		- n: number of songs [default: 20]
		- page_num: page number of response [default: 1]
	- **Response**
		```json
		{
		"results": [
			{
				"artists": "Ed Sheeran",
				"id": "CBGvoIP8",
				"image": "https://c.saavncdn.com/835/x-English-2014-150x150.jpg",
				"title": "Photograph"
			},
			{
				"artists": "Ed Sheeran",
				"id": "td4mU-9E",
				"image": "https://c.saavncdn.com/748/Photograph-Felix-Jaehn-Remix-English-2015-150x150.jpg",
				"title": "Photograph (Felix Jaehn Remix)"
			}
		],
		"start": 1,
		"total": 3179
		}
		```
- **Song Details: /details/song?id=CBGvoIP8**
	- **Parameters**
		- id: id of song [required]
	- **Response**
		```json
		{
			"album": "x",
			"album_url": "https://www.jiosaavn.com/album/x/dZ9OOF6Jq4o_",
			"albumid": "1188602",
			"duration": "258",
			"id": "CBGvoIP8",
			"image": "https://c.saavncdn.com/835/x-English-2014-500x500.jpg",
			"language": "english",
			"media_url": "https://sdlhivkecdnems01.cdnsrv.jio.com/h.saavncdn.com/835/2d0cf8c83a9f3b900ac214e21d07badc_320.mp4",
			"play_count": 9147693,
			"release_date": "2014-06-20",
			"singers": "Ed Sheeran",
			"song": "Photograph",
			"year": "2014"
		}
		```
## Installation:

Clone this repository using
```sh
$ git clone https://github.com/priyansh-anand/JioSaavnAPI
```
Enter into the directory and install all the requirements using

```sh
$ cd JioSaavnAPI
$ pip3 install -r requirements.txt
```
Run the app using

```sh
$ python3 app.py
```


**Note:** This flask application is being served with the development server provided with Flask, if you want to deploy it on Heroku or on any server, then use a production server such as Gunicorn.

## License
MIT
**Free Software, Hell Yeah!**

## Contribution

If you want to add any new feature or fix any bug, you are welcomed to do that. You can also request/suggest for more awesome features to be added in this API