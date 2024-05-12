from flask import Flask, jsonify
from kafka import KafkaProducer, KafkaConsumer

app = Flask(_name_)




# Initialize Kafka producer and consumer
producer = KafkaProducer(bootstrap_servers='192.168.93.129 :9092')
consumer = KafkaConsumer('user_activity', bootstrap_servers='192.168.93.129 :9092', group_id='music_streaming_group')



@app.route('/')
def index():
    return render_template('index.html')




@app.route('/discover', methods=['GET'])
def discover():
    genres = get_genre_names()
    return render_template('discover.html', genres=genres)




def get_genre_names():
    # Function to get a list of genre names from CSV filenames
    genre_files = [file.split('.')[0] for file in os.listdir(csv_folder_path) if file.endswith('.csv')]
    return genre_files



@app.route('/recommendation', methods=['POST'])
def recommendation():
    selected_genres = request.form.getlist('genres')
    songs = []
    for genre in selected_genres:
        csv_file_path = os.path.join(csv_folder_path, f"{genre}.csv")
        if os.path.exists(csv_file_path):
            df = pd.read_csv(csv_file_path)
            # Sample 10 random songs from the DataFrame
            sampled_songs = custom_random_sample(df.to_dict(orient='records'), 10)
            songs.extend(sampled_songs)
    return render_template('recommendation.html', genres=selected_genres, songs=songs)



@app.route('/play_song/<int:track_id>')
def play_song_by_id(track_id):
    file_path = os.path.join(sample_folder_path, f"{track_id:06d}.mp3")

    if os.path.exists(file_path):
        # Play the song
        return render_template('play_song.html', file_path=file_path)
    else:
        return "Track not found"




@app.route('/search_song', methods=['POST'])
def search_song():
    track_id = request.form.get('track_id')
    if track_id:
        return redirect(url_for('play_song_by_id', track_id=track_id))
    else:
        return "Track ID is required for search"


if __name__ == '__main__':
    app.run(debug=True)
