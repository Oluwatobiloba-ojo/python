from enum import Enum


class Zone(Enum):
    North_Central = {"BENUE", "FCT", "KOGI", "KWARA", "NASARAWA", "NIGER", "PLATEAU"}
    North_East = {"Adamawa", "BAUCHI", "BORNO", "GOMBE", "TARABA", "YOBE"}
    North_West = {"KADUNA", "KATSINA", "KANO", "KEBBI", "SOKOTO", "JIGAWA", "ZAMFARA"}
    South_East = {"ABIA", "ANAMBRA", "EBONYI", "ENUGU", "IMO"}
    South_South = {"AKWA-IBOM", "BAYELSA", "CROSS-RIVER", "DELTA", "EDO", "RIVERS"}
    South_West = {"EKITI", "LAGOS", "OSUN", "ONDO", "OGUN", "OYO"}


