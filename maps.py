import googlemaps
from datetime import datetime
from pprint import pprint


class AddressLocator:
    def __init__(self):
        self.maps = googlemaps.Client(key='AIzaSyAFUBwCyykt-8nfOYqGvUZbXV0dMnQYTJ4')

    # Takes the name of a place and returns the exact address
    def get_location(self, sentence):
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
                except Exception as e:
                    print(e)
                    return None
        return None

    # Takes the name of a place and returns the route from one location to a single destination
    def compute_route(self, starting_point, destination):
        now = datetime.now()
        directions_result = self.maps.directions(starting_point, destination,
                                                 mode="driving",
                                                 departure_time=now)

        directions = directions_result[0]['legs'][0]['steps']
        instructions = [step['html_instructions'] for step in directions]
        text_instructions = [self.strip_html_tags(instruction) for instruction in instructions]
        return text_instructions

    @staticmethod
    def strip_html_tags(text):
        import re
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

# Testing
address_locator = AddressLocator()
loc = address_locator.get_location("Go to Chick-fil-a")
loc2 = address_locator.get_location("Go to Roots")
res = address_locator.compute_route(loc, loc2)

for direction in res:
    print(direction)
