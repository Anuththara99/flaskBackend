from flask import Flask,jsonify, request

app = Flask(__name__)

songs = [
    {
        'mood': 'happy',
        'song': [
            {
                'title': 'Someone like you',
                'artist': 'Adele',
                'link': '34567894321234567890'
            },
            {
                'title': 'Skyfall',
                'artist': 'Adele',
                'link': '34567894321234567890'
            },
            {
                'title': 'Hello',
                'artist': 'Adele',
                'link': '34567894321234567890'
            },
            {
                'title': 'Rolling in the deep',
                'artist': 'Adele',
                'link': '34567894321234567890'
            },
            {
                'title': 'I Have a Dream',
                'artist': 'westlife',
                'link': '34567894321234567890'
            },
            {
                'title': 'Make you feel my love',
                'artist': 'Adele',
                'link': '34567894321234567890'
            },
            {
                'title': 'Set Fire to the rain',
                'artist': 'Adele',
                'link': '34567894321234567890'
            },
            {
                'title': 'Love your self',
                'artist': 'Justin Bieber',
                'link': '34567894321234567890'
            },
            {
                'title': 'Memories',
                'artist': 'Maroon 5',
                'link': '34567894321234567890'
            },
            {
                'title': 'Perfect',
                'artist': 'Ed Sheeran',
                'link': '34567894321234567890'
            },
            {
                'title': 'My love',
                'artist': 'westlife',
                'link': '34567894321234567890'
            }
        ]
    },
    {
        'mood': 'sad',
        'song': [
            {
                'title': 'RockaBye',
                'artist': 'Clean Bandit',
                'link': '34567894321234567890'
            }
        ]
    },
    {
        'mood': 'angry',
        'song': [
            {
                'title': 'Raabtha',
                'artist': 'argith singh',
                'link': '34567894321234567890'
            }
        ]
    },
    {
        'mood': 'neutral',
        'song': [
            {
                'title': 'As long as you love me',
                'artist': 'backstreet boys',
                'link': '34567894321234567890'
            },
            {
                'title': 'You Raise me up',
                'artist': 'westlife',
                'link': '34567894321234567890'
            },
            {
                'title': 'I want it that Way',
                'artist': 'backstreet boys',
                'link': '34567894321234567890'
            }
        ]
    },
    {
        'mood': 'surprise',
        'song': [
            {
                'title': 'A Milloion Dreams',
                'artist': 'Michelle Williams',
                'link' : '34567894321234567890'
            }
        ]
    }
]

@app.route('/')
def hello_world():
    return 'Emoscape Backend !'

@app.route('/song', methods=['POST'])
def create_newPlaylist():
    request_data = request.get_json()
    new_store = {
        'mood': request_data['mood'],
        'song': []
    }
    songs.append(new_store)
    return jsonify(new_store)


@app.route('/song/<string:mood>')
def get_mood_playlist(mood):
    for song in songs:
        if(song['mood'] == mood):
            return jsonify(song)
    return jsonify({'message': 'store not found'})


@app.route('/song')
def get_all_playlists():
    return jsonify({'songs': songs})


@app.route('/song/<string:mood>/song', methods=['POST'])
def add_songs(mood):
    request_data = request.get_json()
    for song in songs:
        if(song['mood'] == mood):
            new_item = {
                'title': request_data['title'],
                'artist': request_data['artist'],
                'link' : request_data['link']
            }
            song['song'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})


@app.route('/song/<string:mood>/song')
def get_playlist_songs(mood):
    for song in songs:
        if(song['mood'] == mood):
            return jsonify(song['song'])
    return jsonify({'message': 'store not found'})


# @app.route('/song/<string:mood>/song', methods=['DELETE'])
# def add_songs(mood):
#     request_data = request.get_json()
#     for song in songs:
#         if(song['mood'] == mood):
#             new_item = {
#                 'title': request_data['title'],
#                 'artist': request_data['artist'],
#                 'link' : request_data['link']
#
#             }
#             song['song'].pop(new_item)
#             return jsonify(new_item)
#     return jsonify({'message':'store not found'})

if __name__ == '__main__':
    app.run()
