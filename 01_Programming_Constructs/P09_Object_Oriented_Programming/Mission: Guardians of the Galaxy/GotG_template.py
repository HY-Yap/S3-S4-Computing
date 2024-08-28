###
# Guardian of the Galaxy
###

# Your answer here.


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
# test_gg()
