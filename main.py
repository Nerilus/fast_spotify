from flask import Flask, jsonify
import pandas as pd

#Charger les données à partir du fichier CSV
file_path = 'spotify_tracks (1).csv'  # Remplacer par le chemin complet si nécessaire
df = pd.read_csv(file_path)

#Initialiser l'application Flask
app = Flask(__name__)

#Route pour récupérer toutes les données
@app.route('/data', methods=['GET'])
def get_data():
    data = df.to_dict(orient='records')  # Convertir les données en format JSON
    return jsonify(data)

#Route pour récupérer un morceau spécifique par son track_id
@app.route('/data/<track_id>', methods=['GET'])
def get_track(track_id):
    track = df[df['track_id'] == track_id].to_dict(orient='records')
    if track:
        return jsonify(track[0])
    else:
        return jsonify({'error': 'Track not found'}), 404

@app.route('/')
def home():
    return "Bienvenue sur l'API Spotify !"

if __name__ == '__main__':
    app.run(debug=True)