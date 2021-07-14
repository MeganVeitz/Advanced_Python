import requests
import json


def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

####################################################################
# DO NOT CHANGE CODE ABOVE THIS LINE
####################################################################

# output the number of events
    print("The number of events is:")
    print(theJSON['metadata']['count'])

# for each event, print the place where it occurred
    print("The places where it occurred:")
    for item in theJSON['features']:
        print(item['properties']["place"])

# print the events that only have a magnitude greater than 4
    print("The events that only have a magnitude greater than 4: ")
    for event in theJSON['features']:
        if event['properties']['mag'] > 4:
            print("ID is: {}, the location is: {}, the magnitude is: {}".format(event['id'], event['properties']['place'], event['properties']['mag']))

# print only the events where at least 1 person reported feeling something
    print("The events where at least 1 person reported feeling something: ")
    for events in theJSON['features']:
        if not events['properties']['felt']:
            continue
        if events['properties']['felt'] > 0:
            print("ID is: {}, the location is: {}, the number of people who felt it is: {}".format(events['id'], events['properties']['place'], events['properties']['felt']))

####################################################################
# DO NOT CHANGE CODE BELOW THIS LINE
####################################################################

def main():
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    web = requests.get(urlData)
    if web.status_code == 200:
        printResults(web.content)
    else:
        print('There was an HTTP error with the request')


if __name__ == "__main__":
    main()
