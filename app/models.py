from sqlalchemy import Column, Integer, String
from app.database import Base

# Descriptif de la base de donnée

class Observation(Base):
    __tablename__ = "Observation"

    id = Column(Integer, primary_key=True, index=True)
    commune = Column(String, nullable=True)
    nb_individus = Column(Integer)
    date_vue = Column(String, nullable=True)
    geo_shape_type = Column(String, nullable=True)
    geo_shape_geometry_coordinates = Column(String, nullable=True)
    geo_shape_geometry_type = Column(String, nullable=True)
    geo_point_2d_lon = Column(String, nullable=True)
    geo_point_2d_lat = Column(String, nullable=True)
    espece = Column(String, nullable=True)
    periode = Column(String, nullable=True)