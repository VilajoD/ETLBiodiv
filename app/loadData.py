import json
from app import models
from app.database import SessionLocal, engine, session
from sqlalchemy.orm import Session

# Partie qui s'occupe de récupérer les fichiers dans le dossier Files.
# Dans le fichier "A_traiter" est noté tous les fichiers à traiter present dans le dossier Files.
# Tous les fichiers sont du même format et sont inserés dans la base les uns à la suite des autres

def load_data():
    fic = open('./app/Files/A_traiter.txt', 'r', encoding="utf-8")
    fichier_oiseau = fic.readline().replace("\n", "")

    while  fichier_oiseau != "" :
        with open(f"./app/Files/{fichier_oiseau}", "r", encoding="utf-8") as f:
            content = json.load(f)

        # Création des tables (à faire une seule fois)
        models.Base.metadata.create_all(bind=engine)

        db = SessionLocal()
        for ligne in content :

            observation = models.Observation(
                commune=ligne.get('commune'),
                nb_individus = int(ligne.get('nb_individus')) if ligne.get('nb_individus') else None,
                date_vue=ligne.get('date_vue'),
                geo_shape_type=ligne.get('geo_shape').get('type'),
                geo_shape_geometry_coordinates=ligne.get('geo_shape').get('geometry').get('coordinates'),
                geo_shape_geometry_type=ligne.get('geo_shape').get('geometry').get('type'),
                geo_point_2d_lon=ligne.get('geo_point_2d').get('lon'),
                geo_point_2d_lat=ligne.get('geo_point_2d').get('lat'),
                espece=ligne.get('espece'),
                periode=ligne.get('periode')
            )
            db.add(observation)

        db.commit()
        fichier_oiseau = fic.readline().replace("\n", "")

    fic.close()