import requests
import csv
from bs4 import BeautifulSoup

API_KEY = "1fca6cbb30b0f3195699c1a5093e1a85c505d81ea7b6cee4e687af2970b687f8"

def scan_ip(ip_address):
    ip_scan_endpoint = "https://www.virustotal.com/vtapi/v2/ip-address/report"
    params = {"apikey" : API_KEY,"ip" : ip_address}
    response = requests.get(ip_scan_endpoint,params = params)
    return response.json()

def extract_detection_info(scan_result):
    detection_count = scan_result.get("detected_communicating_samples",0)
    scan_date = scan_result.get("scan_date","")
    return detection_count,scan_date

if __name__ == "__main__":
    ips_to_scan = list()
    
    while True:
        print("1 : enter ip address , 2 : exit")
        choice = int(input("Enter choice in 1/2: "))
        if choice == 1:
            IP_ADDRESS = input("Enter an ip address: ")
            ips_to_scan.append(IP_ADDRESS)
            print("IP address saved in list")
        elif choice == 2:
            break
    
    results = []
    for ip in ips_to_scan:
        ip_result = scan_ip(ip)
        detection_count,scan_date = extract_detection_info(ip_result)
        results.append({"IP" : ip,"Detection Count" : detection_count,"Scan Date" : scan_date})

    csv_path = "ip_scan_results.csv"
    with open(csv_path,'w',newline = '',encoding = "utf-8") as csv_file:
        fieldnames = ["IP","Detection Count","Scan Date"]
        csv_writer = csv.DictWriter(csv_file,fieldnames = fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(results)

    print("IP scan results saved to ",{csv_path},".")


        
