import whois

def perform_whois_lookup(domain_name):
    try:
        whois_info = whois.whois(domain_name)
        print(whois_info)
                
    except Exception as e:
        print("Error:",e)
 
if __name__ == "__main__":
    while True:
        choice = str(input("Enter in yes/no to use the function: "))
        if choice.lower() == "yes":
            domain_name = str(input("Enter the url/domain name: "))
            perform_whois_lookup(domain_name)
        elif choice.lower() == "no":
            break
        else:
            print("Enter in yes/no")
