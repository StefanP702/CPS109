def compute() :
 distanceInMiles = 3279.8
 metersPerMile = 1609.34
 distanceInMeters = distanceInMiles * metersPerMile
 turtleSpeed = 0.5
 timeSeconds = distanceInMeters / turtleSpeed
 print('Time in seconds for turtle to go from Miami to Seattle')
 print(timeSeconds)
 minutes = timeSeconds / 60
 print(minutes)
 hours = minutes / 60
 days = hours / 24
 weeks = days / 7
 print("In weeks")
 print weeks 
 
def compute2():
  gravity = 6.67384E-11
  earthMass = 5.9736E24
  earthRadius = 6371000
  velocity = (2 * gravity * earthMass) / earthRadius
  result = sqrt(velocity)
  print "Escape velocity:"
  print result 


def compute3():
  heightInStories = 3
  feetPerStory = 10
  heightInFeet = heightInStories * feetPerStory
  metersPerFoot = 0.3048
  heightInMeters = heightInFeet * metersPerFoot
  gravityMeters = 9.81
  timeToFall = sqrt((2*heightInMeters)/gravityMeters)
  print("Time to fall (seconds):")
  print(timeToFall)
