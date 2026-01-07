import requests

def bus():
    response = requests.get(f"https://bustime.mta.info/api/2/siri/stop-monitoring.json?key=b37b2029-5bb8-43dc-bb85-4bc15a1de888&MTA&MonitoringRef={201020}&MaximumStopVisits=100")
    data = response.json()
    print({
        "route": data["Siri"]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"][0]["MonitoredVehicleJourney"]["PublishedLineName"],
    
    })
    
bus()