from geo_political_zone.political_zone_enum import Zone


def political_zone(state: str):
    for zone in list(Zone):
        if state.upper() in zone.value:
            return zone.name

