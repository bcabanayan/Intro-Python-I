# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return F"The location is called {self.name}. The latitude is {self.lat}. The longitude is {self.lon}."

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return F"The location is called {self.name}. The latitude is {self.lat}. The longitude is {self.lon}. The difficulty is {self.difficulty}. The size is {self.size}."

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

catacombs = Waypoint(41.70505, -121.51521, "Catacombs")
print(catacombs)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

geocache = Geocache(44.052137, -121.41556, "Newberry Views", 1.5, 2)

# Print it--also make this print more nicely
print(geocache)

class Animal:
    # define attributes, assign initial values
    def __init__(self, name, sound, species, num_legs):
    # self: with this specific instance, set this value to this parameter
        self.name = name
        self.sound = sound
        self.species = species
        self.num_legs = num_legs

    # define class methods
    def set_num_legs(self, num):
        self.num_legs = num

    def make_sound(self, sound):
        print(sound)

# instance of class
animal_a = Animal('ernie', 'elephant', 'pbbbbbbbbbt', 4)

# animal_a.make_sound(animal_a, 'pbbbbbt')
print(animal_a.num_legs)
# animal_a.num_legs(3)
print(animal_a.num_legs)
