import requests

def bus(data):
    response = requests.get(f"https://bustime.mta.info/api/2/siri/stop-monitoring.json?key=b37b2029-5bb8-43dc-bb85-4bc15a1de888&MTA&MonitoringRef=200700&LineRef=MTA%20NYCT_S53&MaximumStopVisits=10")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
bus(1)