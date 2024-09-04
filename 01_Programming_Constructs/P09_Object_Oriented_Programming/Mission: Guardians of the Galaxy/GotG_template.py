###
# Guardian of the Galaxy
###

# Your answer here.
class Spaceship:
    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._guardians = []
    
    def get_location(self):
        return self._location

    def go_to(self, planet):
        if not self._guardians:
            return f'{self._name} does not have any guardians on board'
        
        for guardian in self._guardians:
            if planet in guardian.known_planets():
                self._location = planet
                return f'{self._name} travels to {planet}'
        
        return f'{planet} is not a known location'
    
    def contains(self):
        return [guardian._name for guardian in self._guardians]
    
    def add_guardian(self, guardian):
        self._guardians.append(guardian)

class Guardian:
    def __init__(self, name, planet, *planets):
        self._name = name
        self._location = planet
        self._known_planets = {planet, *planets}
    
    def known_planets(self):
        return list(self._known_planets)
    
    def board(self, ship):
        if self._location != ship.get_location():
            return f'{self._name} cannot board the {ship._name}'
        
        ship.add_guardian(self)
        self._location = ship
        for guardian in ship._guardians:
            self._known_planets.update(guardian.known_planets())
            guardian._known_planets.update(self._known_planets)
        return f'{self._name} boards the {ship._name}'
    
    def get_location(self):
        if isinstance(self._location, Spaceship):
            return f'{self._name} is on the ship {self._location._name} at the planet {self._location.get_location()}'
        return f'{self._name} is on the planet {self._location}'

# Tests

def test_gg():
    print("Testing Guardians of the Galaxy")

    milano = Spaceship("Milano", "Morag")
    print(milano.get_location() == 'Morag')

    quill = Guardian("Quill", "Morag", "Earth")
    print(sorted(quill.known_planets()) == sorted(['Earth', 'Morag']))

    groot = Guardian("Groot", "Earth", "Xandar")
    drax = Guardian("Drax", "Earth", "Nowhere")
    gamora = Guardian("Gamora", "Xandar")
    rocket = Guardian("Rocket", "Nowhere")

    print(milano.contains() == [])

    print(milano.go_to("Earth") == 'Milano does not have any guardians on board')

    print(rocket.board(milano) == 'Rocket cannot board the Milano')
    print(quill.board(milano) == 'Quill boards the Milano')
    print(milano.go_to("Earth") == 'Milano travels to Earth')
    print(milano.go_to("Xandar") == 'Xandar is not a known location')
    print(milano.get_location() == 'Earth')

    print(sorted(milano.contains()) == sorted(['Quill']))

    print(sorted(quill.known_planets()) == sorted(['Earth', 'Morag']))
    print(sorted(groot.known_planets()) == sorted(['Earth', 'Xandar']))
    print(groot.board(milano) == 'Groot boards the Milano')
    print(sorted(quill.known_planets()) ==
        sorted(['Earth', 'Morag', 'Xandar']))
    print(sorted(groot.known_planets()) ==
        sorted(['Earth', 'Morag', 'Xandar']))

    print(drax.board(milano) == 'Drax boards the Milano')
    print(sorted(quill.known_planets()) == sorted(
        ['Earth', 'Morag', 'Nowhere', 'Xandar']))
    print(sorted(groot.known_planets()) == sorted(
        ['Earth', 'Morag', 'Nowhere', 'Xandar']))
    print(sorted(drax.known_planets()) == sorted(
        ['Earth', 'Morag', 'Nowhere', 'Xandar']))

    print(milano.go_to("Xandar") == 'Milano travels to Xandar')
    print(gamora.board(milano) == 'Gamora boards the Milano')

    print(rocket.get_location() == 'Rocket is on the planet Nowhere')
    print(milano.go_to("Nowhere") == 'Milano travels to Nowhere')
    print(rocket.board(milano) == 'Rocket boards the Milano')
    print(rocket.get_location() ==
        'Rocket is on the ship Milano at the planet Nowhere')

    print(sorted(milano.contains()) == sorted(
        ['Drax', 'Gamora', 'Groot', 'Quill', 'Rocket']))

    # Let's go and save the Earth
    print(milano.go_to("Earth") == 'Milano travels to Earth')
    print("===========================================")

# Uncomment to test
test_gg()
