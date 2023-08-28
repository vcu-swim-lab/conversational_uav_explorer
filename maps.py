"""This module contains the AddressLocator class which converts a location to an address."""

from datetime import datetime
import googlemaps
import re


class AddressLocator:
    """This class converts a location to an address using Google Maps API"""
    def __init__(self):
        """Initializes the object with the API key"""
        self.maps = googlemaps.Client(key='AIzaSyAFUBwCyykt-8nfOYqGvUZbXV0dMnQYTJ4')

    def get_location(self, sentence):
        """
        Returns the exact address

        :param sentence: command
        :type sentence: str
        :return: address
        :rtype: str
        """
        sentence = sentence.lower()
        commands = ["take picture", "go to", "land", "take off"]
        for command in commands:
            if command in sentence:
                address_start_index = sentence.index(command) + len(command) + 1
                address = sentence[address_start_index:].strip()
                try:
                    response = self.maps.places(query=address)
                    results = response.get('results')
                    if results:
                        return results[0]['formatted_address']
                    else:
                        return None
                except Exception as error:
                    print(error)
        return None

    def compute_route(self, uav_location, destination):
        """
        Returns the route from one location to a single destination.

        :param uav_location: UAV's current location
        :type uav_location: str
        :param destination: destination
        :type destination: str
        :return: directions from UAV to destination
        :rtype: str
        """
        now = datetime.now()
        directions_result = self.maps.directions(uav_location, destination,
                                                 mode="driving",
                                                 optimize_waypoints=True,
                                                 departure_time=now
                                                 )

        directions = directions_result[0]['legs'][0]['steps']
        instructions = [step['html_instructions'] for step in directions]
        text_instructions = [self.strip_html_tags(instruction) for instruction in instructions]
        return text_instructions

    @staticmethod
    def strip_html_tags(text):
        """Removes the HTML tags from the directions"""
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)
