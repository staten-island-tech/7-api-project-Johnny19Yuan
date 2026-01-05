import requests

def bus(data):
    response = requests.get(f"https://bustime.mta.info/api/2/siri/stop-monitoring.json?key=b37b2029-5bb8-43dc-bb85-4bc15a1de888&MTA&MonitoringRef=201020&LineRef+79&MaximumStopVisits=10")
    
    
bus(1)