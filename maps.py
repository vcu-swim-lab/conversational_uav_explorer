import googlemaps


class AddressLocator:
    def __init__(self):
        self.maps = googlemaps.Client(key='AIzaSyAFUBwCyykt-8nfOYqGvUZbXV0dMnQYTJ4')

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
