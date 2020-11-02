#!/usr/bin/env python
"""Magnetic Card Parser."""
import string
import re
import yaml


class InvalidTrackData(Exception):
    """InvalidTrackData Exception."""

    pass


class Parser:
    """Track Parser."""

    TRACKS = {
        "1": re.compile(
            r"%(?P<format>[A-Z])(?P<pan>[0-9]{1,19})\^(?P<name>[^^]*)\^\s?(?P<expiration>\d{4}|\^)(?P<service_code>\d{3}|\^)(?P<discretionary_data>[^\?]*)\?"
        ),
        "2": re.compile(
            r";(?P<pan>[0-9]{1,19})=(?P<expiration>\d{4}|=)(?P<service_code>\d{3}|=)(?P<discretionary_data>[^\?]*)\?.?"
        ),
        "emv": re.compile(
            r";(?P<pan>[0-9 ]{1,19})(d|D)(?P<expiration>\d{4}|(d|D))(?P<service_code>\d{3}|(d|D))(?P<discretionary_data>[^\?fF]*)(f|F)?0?.*"
        ),
    }

    @staticmethod
    def parse(track_data):
        """Parse track_data and return attributes."""
        for k, v in Parser.TRACKS.items():
            match = v.match(track_data)
            if match:
                attributes = {}
                attributes["track_format"] = k
                attributes["pan"] = match.group("pan")
                attributes["discretionary_data"] = match.group(
                    "discretionary_data")
                if k == "1":
                    attributes["format"] = match.group("format")
                    attributes["name"] = match.group("name")
                    if match.group("expiration") == "^":
                        attributes["expiration"] = "00", "00"
                    else:
                        attributes["expiration"] = match.group(
                            "expiration"
                        )  # if == ^ none
                    if match.group("service_code") == "^":
                        attributes["service_code"] = "0", "0", "0"
                    else:
                        attributes["service_code"] = match.group(
                            "service_code"
                        )  # if == ^ none
                elif k == "2" or k == "emv":
                    if match.group("expiration") == "=":
                        attributes["expiration"] = "00", "00"
                    else:
                        attributes["expiration"] = match.group(
                            "expiration"
                        )  # if == = none
                    if match.group("service_code") == "=":
                        attributes["service_code"] = "0", "0", "0"
                    else:
                        attributes["service_code"] = match.group(
                            "service_code"
                        )  # if == = none
                else:
                    pass
                return attributes
            else:
                # raise InvalidTrackData(
                #     f"Track Data: {track_data} is not Valid.")
                pass


class Card:
    """
    Card Class.

    attr_accessor :allowed_services, :authorization_processing,
    :discretionary_data, :expiration_year, :expiration_month, :first_name,
    :format, :initial, :interchange, :last_name, :number, :pin_requirements,
    :technology, :title, :track_format."""

    ALLOWED_SERVICES = {
        "0": "no_restrictions",
        "1": "no_restrictions",
        "2": "goods_and_services_only",
        "3": "atm_only",
        "4": "cash_only",
        "5": "goods_and_services_only",
        "6": "no_restrictions",
        "7": "goods_and_services_only",
    }
    AUTHORIZATION_PROCESSING = {
        "0": "normal",
        "2": "by_issuer",
        "4": "by_issuer_unless_explicit_agreement",
    }
    FORMAT = {
        "A": "reserved",
        "B": "bank",
    }
    FORMAT.update({c: "available" for c in string.ascii_uppercase[2:13]})
    FORMAT.update({c: "available" for c in string.ascii_uppercase[13:]})
    INTERCHANGE = {
        "1": "international",
        "2": "international",
        "5": "national",
        "6": "national",
        "7": "private",
        "9": "test",
    }
    PIN_REQUIREMENTS = {
        "0": "pin_required",
        "3": "pin_required",
        "5": "pin_required",
        "6": "prompt_for_pin_if_ped_present",
    }
    TECHNOLOGY = {
        "2": "integrated_circuit_card",
        "6": "integrated_circuit_card",
    }

    def __init__(self):
        self.allowed_services = None
        self.authorization_processing = None
        self.discretionary_data = None
        self.expiration_month = None
        self.expiration_year = None
        self.first_name = None
        self.format = None
        self.interchange = None
        self.last_name = None
        self.number = None
        self.pin_requirements = None
        self.technology = None
        self.title = None
        self.track_format = None

    @staticmethod
    def parse(track_data, parser=Parser()):
        attributes = parser.parse(track_data)
        if not attributes:
            return Card()
        # print(yaml.dump(attributes))
        position1, position2, position3 = attributes.get("service_code")
        year, month = attributes.get("expiration")[
            :2], attributes.get("expiration")[2:]
        if attributes.get("name"):
            title, first_name, initial, last_name = Card.parse_name(
                attributes.get("name", "")
            )
        else:
            title, first_name, initial, last_name = Card.parse_name("")
        card = Card()
        card.allowed_services = Card.ALLOWED_SERVICES.get(position3)
        card.authorization_processing = Card.AUTHORIZATION_PROCESSING.get(
            position2)
        card.discretionary_data = attributes.get("discretionary_data")
        card.expiration_month = month
        card.expiration_year = year
        card.first_name = first_name
        card.format = Card.FORMAT.get(attributes.get("format"))
        card.interchange = Card.INTERCHANGE.get(position1)
        card.last_name = last_name
        card.number = attributes.get("pan").replace(" ", "")
        card.pin_requirements = Card.PIN_REQUIREMENTS.get(position3)
        card.technology = Card.TECHNOLOGY.get(position1)
        card.title = title
        card.track_format = attributes.get("track_format")
        return card

    @staticmethod
    def parse_name(name):
        title, first, initial, last = "", "", "", ""
        try:
            last, first = name.split("/")[0:2]
        except ValueError:
            first = name
            last = ""
        if first:
            try:
                first, initial = first.split(" ")
            except ValueError:
                initial = ""
        if initial:
            try:
                initial, title = initial.split(".")[0:2]
            except ValueError:
                title = ""
        return (title, first, initial, last)

    @property
    def atm_only(self):
        return self.allowed_services == "atm_only"

    @property
    def cash_only(self):
        return self.allowed_services == "cash_only"

    @property
    def goods_and_services_only(self):
        return self.allowed_services == "goods_and_services_only"

    @property
    def no_service_restrictions(self):
        return self.allowed_services == "no_restrictions"

    @property
    def integrated_circuit_card(self):
        return self.technology == "integrated_circuit_card"

    @property
    def international(self):
        return self.interchange == "international"

    @property
    def test(self):
        return self.interchange == "test"

    @property
    def national(self):
        return self.interchange == "national"

    @property
    def private(self):
        return self.interchange == "private"

    @property
    def pin_required(self):
        return self.pin_requirements == "pin_required"

    @property
    def prompt_for_pin_if_ped_present(self):
        return self.pin_requirements == "prompt_for_pin_if_ped_present"

    @property
    def process_by_issuer(self):
        return self.authorization_processing == "by_issuer"

    @property
    def process_by_issuer_unless_explicit_agreement(self):
        return self.authorization_processing == "by_issuer_unless_explicit_agreement"

    @property
    def process_normally(self):
        return self.authorization_processing == "normal"

    @property
    def as_dict(self):
        return {
            "allowed_services": self.allowed_services,
            "authorization_processing": self.authorization_processing,
            "discretionary_data": self.discretionary_data,
            "expiration_month": self.expiration_month,
            "expiration_year": self.expiration_year,
            "first_name": self.first_name,
            "format": self.format,
            "interchange": self.interchange,
            "last_name": self.last_name,
            "number": self.number,
            "pin_requirements": self.pin_requirements,
            "technology": self.technology,
            "title": self.title,
            "track_format": self.track_format,
        }

    def __str__(self):
        return yaml.dump(self.as_dict)

    def __repr__(self):
        return f"Card: {self.as_dict}"


if __name__ == "__main__":
    test_track1_data = (
        "%B5350290149345177^FATEHI/SUALEH^16042010000000000000000000000000000567001000?"
    )
    test_track2_data = ";5350290149345177=16042010000056700100?"
    card = Card.parse(test_track1_data)
    print(card)
    pass
