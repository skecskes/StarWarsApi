from strenum import StrEnum

import requests


class SortBy(StrEnum):
    NAME = "name"
    MODEL = "model"
    MANUFACTURER = "manufacturer"
    COST_IN_CREDITS = "cost_in_credits"
    LENGTH = "length"
    MAX_ATMOSPHERING_SPEED = "max_atmosphering_speed"
    CREW = "crew"
    PASSENGERS = "passengers"
    CARGO_CAPACITY = "cargo_capacity"
    CONSUMABLES = "consumables"
    HYPERDRIVE_RATING = "hyperdrive_rating"
    MGLT = "MGLT"
    STARSHIP_CLASS = "starship_class"


class SwApi:

    def __init__(self):
        pass

    @staticmethod
    def get_starships(asc: bool = False, sort_by: SortBy = SortBy.NAME):
        url = "https://swapi.dev/api/starships"
        our_starships = []

        while url:
            # get the starships objects
            r = requests.get(url=url)
            r.raise_for_status()
            json = r.json()

            # validate, improve some fields = casting length
            fixed_starships = []
            for ship in json['results']:
                validated_ship = SwApi.validate_ship(ship)
                fixed_starships.append(validated_ship)

            # starships list into our list
            our_starships.extend(fixed_starships)
            url = json['next']

        # sort our list (default ascending)
        sort = not asc

        our_starships.sort(key=lambda s: s[sort_by], reverse=sort)
        # default sort key is name, but can be something else

        return our_starships

    @staticmethod
    def validate_ship(ship):
        length = ship['length'].replace(',', '').replace('unknown', '-1')
        ship['length'] = float(length)

        cost_in_credits = ship['cost_in_credits'].replace(',', '').replace('unknown', '-1')
        ship['cost_in_credits'] = float(cost_in_credits)

        return ship
