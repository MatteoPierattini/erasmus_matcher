from flask import request, render_template
from app import app
from app.models import Course
from flask_sqlalchemy import SQLAlchemy
import os

from dotenv import load_dotenv
load_dotenv()

from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

from app.models import Course

from deep_translator import GoogleTranslator


def get_embedding(text):
    response = client.embeddings.create(input=text,
    model="text-embedding-ada-002")
    return response.data[0].embedding

def translate_to_english(text):
    return GoogleTranslator(source='auto', target='en').translate(text)

@app.route('/', methods=['GET', 'POST'])
def confronta_multiplo():
    risultati_per_universita = {}
    universita_data = []

    if request.method == 'POST':
        syllabus_list = request.form.getlist('syllabi')
        embeddings_input = [
            (i + 1, get_embedding(translate_to_english(s))) for i, s in enumerate(syllabus_list) if s.strip()
        ]

        corsi_db = Course.query.all()

        for input_index, embedding in embeddings_input:
            best_match = None
            best_sim = 0

            for corso in corsi_db:
                if corso.embedding:
                    sim = cosine_similarity([embedding], [corso.embedding])[0][0]
                    if sim > best_sim:
                        best_sim = sim
                        best_match = corso

            if best_sim >= 0.20 and best_match:
                uni = best_match.university.name
                if uni not in risultati_per_universita:
                    risultati_per_universita[uni] = []

                risultati_per_universita[uni].append({
                    'corso': best_match.name,
                    'similarita': round(best_sim * 100, 2),
                    'input_index': input_index
                })

        for uni, matches in risultati_per_universita.items():
            similarita_media = sum([m['similarita'] for m in matches]) / len(matches)
            universita_data.append({
                'nome': uni,
                'match_count': len(matches),
                'similarita_media': round(similarita_media, 2),
                'dettagli': matches
            })

        universita_data.sort(key=lambda u: (-u['match_count'], -u['similarita_media']))
    
    else:
        return render_template('index.html', universita=None, ricerca_effettuata=False)

    return render_template('index.html', universita=universita_data, ricerca_effettuata=True)

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/corsi')
def lista_corsi():
    corsi = Course.query.all()
    return render_template('corsi.html', corsi=corsi)
