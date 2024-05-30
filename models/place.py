#!/usr/bin/python3
""" this module contains the class Place thats inherit from BaseModel """


class Place(BaseModel):
    """ the class place """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_roo, = 0
    number_bathroom = 0
    max_gust = 0
    price_by_night = 0
    latitude = 0.0
    longtitude = 0.0
    amenity_id = []
