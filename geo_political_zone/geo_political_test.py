from unittest import TestCase
from geo_political import political_zone
from political_zone_enum import Zone


class TestSomething(TestCase):
    def test_for_the_geopolitical_zone_for_fct(self):
        zone = political_zone("fct")
        self.assertEqual(Zone.North_Central.name, zone)

    def test_for_the_geo_political_zone_for_yobe(self):
        zone = political_zone("yobe")
        self.assertEqual(Zone.North_East.name, zone)

    def test_for_the_geo_political_zone_for_lagos(self):
        zone = political_zone("lagos")
        self.assertEqual(zone, Zone.South_West.name)

    def test_for_the_geo_political_zone_for_imo(self):
        zone = political_zone("imo")
        self.assertEqual(zone, Zone.South_East.name)

    def test_for_the_geo_political_zone_for_katsina(self):
        zone = political_zone("katsina")
        self.assertEqual(zone, Zone.North_West.name)