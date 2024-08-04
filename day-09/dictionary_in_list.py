travel_log = [
    {
        "country": "france",
        "visits": 12,
        "cities": ["paris", "lille", "dijon"]
    },
    {
        "country": "germany",
        "visits": 5,
        "cities": ["berlin", "hamburg", "stuttgart"]
    },
]

def add_new_country(country, visits, cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities
    })

add_new_country("russia", 5, ["moscow", "Saint Petersburg", "Novosibirsk"])
print(travel_log)