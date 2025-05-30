from openai import OpenAI
from app import app, db
from app.models import Course
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embedding(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

with app.app_context():
    corsi = Course.query.all()
    for corso in corsi:
        if not corso.embedding:
            print(f"⏳ Genero embedding per: {corso.name}")
            corso.embedding = get_embedding(corso.syllabus)
    db.session.commit()
    print("✅ Tutti gli embedding sono stati salvati.")

