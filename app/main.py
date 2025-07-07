import json
import psycopg2
import sqlalchemy
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models
from app import loadData
from app import schema
from app.database import SessionLocal, engine, session

# Chargement en base des données des fichiers JSON
loadData.load_data()


# Getion des sessions pour sqlalchemy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Gestion de l'API
app = FastAPI()

@app.get("/TotalCount")
def TotalCount(db: Session = Depends(get_db)) -> int :
    total = db.query(func.sum(models.Observation.nb_individus)).scalar()
    return total


@app.get("/CountBySpecies")
def CountBySpecies(db: Session = Depends(get_db)) :
    results = db.query(models.Observation.espece,func.sum(models.Observation.nb_individus)).group_by(models.Observation.espece)

    bird_counts = [
        {"espece": espece, "total": total or 0}
        for espece, total in results
    ]
    return bird_counts


@app.get("/CountSpeciesByCity")
def CountSpeciesByCity(db: Session = Depends(get_db)) :
    results = db.query(models.Observation.commune,models.Observation.espece,func.sum(models.Observation.nb_individus)).group_by(models.Observation.commune,models.Observation.espece).order_by(models.Observation.commune)

    bird_counts = [
        {"commune":commune,"espece": espece, "total": total or 0}
        for commune, espece, total in results
    ]
    return bird_counts


@app.get("/CountSpeciesByPeriod")
def CountSpeciesByPeriod(db: Session = Depends(get_db)) :
    results = db.query(models.Observation.periode,models.Observation.espece,func.sum(models.Observation.nb_individus)).group_by(models.Observation.periode,models.Observation.espece).order_by(models.Observation.periode)

    bird_counts = [
        {"periode":periode,"espece": espece, "total": total or 0}
        for periode, espece, total in results
    ]
    return bird_counts

@app.post("/InsertObservation")
def InsertObservation(obs:schema.ObservationCreate,db: Session = Depends(get_db)) :
    observation = models.Observation(**obs.dict())
    db.add(observation)
    db.commit()
    db.refresh(observation)

    return observation



