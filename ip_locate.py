from geoip2 import database
a = "2600:1408:c400:388::3831"
database_path = input("Enter database path: ")

def get_ip_location(ip_address):
    reader = database.Reader(database_path)
    try:
        response = reader.city(ip_address)
        country = response.country.name
        city = response.city.name
        latitude = response.location.latitude
        longitude = response.location.longitude
        print(f"IP: {ip_address}\nCountry: {country}\nCity: {city}\nLatitude: {latitude}\nLongitude: {longitude}")
    except Exception as e:
        print("Error:",e)
    finally:
        reader.close()

if __name__ == "__main__":
    ip_to_lookup = a
    get_ip_location(ip_to_lookup)
