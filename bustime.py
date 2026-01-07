import requests

def bus(stop):
    response = requests.get(f"https://bustime.mta.info/api/2/siri/stop-monitoring.json?key=b37b2029-5bb8-43dc-bb85-4bc15a1de888&MTA&MonitoringRef={stop}&MaximumStopVisits=100")
    data = response.json()
    print({
        "route": data["Siri"]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"][0]["MonitoredVehicleJourney"]["PublishedLineName"],
        "dest" : data["Siri"]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"][0]["MonitoredVehicleJourney"]["DestinationName"]
    })
    
bus(201020)