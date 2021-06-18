def number(bus_stops):

    people = bus_stops[0][0]

    for i in range(1, len(bus_stops)):

        people += bus_stops[i][0]
        people -= bus_stops[i][1]
    
    return people

# One-liner:

def number2(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])