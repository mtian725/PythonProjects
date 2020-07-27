# Project 4
This project is going to focus on getting comfortable with classes and basic
Object Oriented Programming. The base class have already been implemented for
you.

Run `python3 test.py` to test your code.

Run `python3 -v test.py` to see the results of each individual test.

To reduce visual clutter while working, I highly recommend commenting out
the tests that you're not working on. (By commenting out the function definition and its contents).

Feel free to add onto test.py if you want to do more thorough testing.

Shapes
---------
You will need to implement 3 classes: Triangle, Square, and Circle. They all
extend Shape. For each you will need to implement:
* A constructor which takes an number, which will either represent the side
length or the length of the radius
* getArea() => returns the area of the shape. For simplicity sake, round to the
nearest whole number.
* getSideLength() => returns either the length of the sides or the radius
* \__str__(self) => Formatted information about the shape. This is how we will
test the classes. Format the string as:
```
This shape is a <shape type> with <side length/radius> of <length> and area of
<area>.
```

Satellites
---------
You will need to implement 2 classes: NaturalSatellite and ArtificialSatellite.
They both extend Satellite.

For NaturalSatellite you will need to implement:
* A constructor which takes a string, number, number, and a string, which
represents name, orbit distance, size, and the primary body.
* getOrbitDistance() => returns the orbit distance
* getSize() => returns the size
* getPrimaryBody() => returns what the primary body is
* \__str__(self) => Formatted information about the satellite. This is how we
will test the classes. Format the string as:
```
<name> has a diameter of about <size> km^3 and orbits <primary body> with an
orbit distance of <orbit distance> km.
```

For ArtificialSatellite you will need to implement:
* A constructor which takes a string, number, string, and a string, which
represents name, orbit distance, owner, and the primary body.
* getOrbitDistance() => returns the orbit distance
* getPrimaryBody() => returns what the primary body is
* getOwner() => returns what the satellite's owner is
* \__str__(self) => Formatted information about the satellite. This is how we
will test the classes. Format the string as:
```
<name> is owned by <owner> and orbits <primary body> with an orbit distance of
<orbit distance> km.
```
