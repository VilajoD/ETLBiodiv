from pydantic import BaseModel
from typing import Optional

# Pour mise en forme et vérification lors d'un appel à l'API

class ObservationCreate(BaseModel):
    commune: Optional[str]
    nb_individus: Optional[int]
    date_vue: Optional[str]
    geo_shape_type: Optional[str]
    geo_shape_geometry_coordinates: Optional[str]
    geo_shape_geometry_type: Optional[str]
    geo_point_2d_lon: Optional[str]
    geo_point_2d_lat: Optional[str]
    espece: Optional[str]
    periode: Optional[str]