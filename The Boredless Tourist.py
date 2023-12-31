#question 3
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

#question 4
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#question 8
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index
#question 11 (should return 2)
#print(get_destination_index("Los Angeles, USA"))
#question 12 (shoul return 0)
#print(get_destination_index("Paris, France"))
#question 13 (should give a Value Error)
#print(get_destination_index("Hyderabad, India"))

#question 15, 16,17, 18
def get_traveler_location(traveler):
  #question 16
  traveler_destination = traveler[1]
  #question 17
  traveler_destination_index = get_destination_index(traveler_destination)
  #question 18
  return traveler_destination_index

#question 19
test_destination_index = get_traveler_location(test_traveler)
#question 20
#print(test_destination_index)

#question 24
attractions = []
for destination in destinations:
  attractions.append([])

#question 26
#print(attractions)

#question 27, 28, 31 & 32
def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index].append(attraction)
  return attractions_for_destination

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#print(attractions)

#question 38, 39, 40, 41, 42, 43, 44, 45, 46, 49
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest


#question 47, 48
la_arts = find_attractions('Los Angeles, USA', ['art'])
#print(la_arts)

#question 53, 54, 55, 56, 57, 58, 59, 60
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = 'Hi ' + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
  for i in range(len(traveler_attractions)):
    if traveler_attractions[-1] == traveler_attractions[i]:
      interests_string += "the " + traveler_attractions[i] + ". "
    else:
      interests_string += "the " + traveler_attractions[i] + ", "
  return interests_string

#question 61, 62
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
