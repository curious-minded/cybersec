from ipwhois import IPWhois

def perform_ip_whois(ip_address):
    try:
        ip = IPWhois(ip_address)
        ip_info1 = ip.lookup_rdap()
        result = ip.lookup_whois()

        asn = result['asn']
        asn_cidr = result['asn_cidr']
        asn_country_code = result['asn_country_code']
        asn_description = result['asn_description']

        print(f"ASN: {asn}")
        print(f"ASN CIDR: {asn_cidr}")
        print(f"ASN Country Code: {asn_country_code}")
        print(f"ASN Description: {asn_description}")
        print("RDAP lookup:", ip_info1)
    except Exception as e:
        print("Error:",e)

if __name__ == "__main__":
    while True:
        choice = str(input("Enter in yes/no if you want to use this function: "))
        if choice.lower() == "yes":
            ip_address = str(input("Enter the IP address: "))
            perform_ip_whois(ip_address)
        elif choice.lower() == "no":
            break
        else:
            print("Enter choice in yer/no")
