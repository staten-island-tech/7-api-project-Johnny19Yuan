import requests

def bus():
    response = requests.get("https://bustime.mta.info/api/2/siri/stop-monitoring.json?key=b37b2029-5bb8-43dc-bb85-4bc15a1de888&MTA&MonitoringRef=201020&MaximumStopVisits=100")
    response.json()
    
bus()