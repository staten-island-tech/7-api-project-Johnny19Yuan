import requests
def bus(stop,x):
    response = requests.get(f"https://bustime.mta.info/api/2/siri/stop-monitoring.json?key=fad509a0-390b-44d5-a448-7d9bd3ca1bdb&MTA&MonitoringRef={stop}&MaximumStopVisits=100")
    data = response.json()
    return {
        "route": data["Siri"]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"][x]["MonitoredVehicleJourney"]["PublishedLineName"],
        "dest" : data["Siri"]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"][x]["MonitoredVehicleJourney"]["DestinationName"],
        "exatime": data["Siri"]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"][x]["MonitoredVehicleJourney"]["MonitoredCall"]["ExpectedArrivalTime"],
        "currtime": data["Siri"]["ServiceDelivery"]["ResponseTimestamp"],
        "distance": data["Siri"]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"][x]["MonitoredVehicleJourney"]["MonitoredCall"]["Extensions"]["Distances"]["PresentableDistance"],
        
    }

print(bus(200700,0))