import tkinter as tk
import requests

def bus(stop):
    response = requests.get(f"https://bustime.mta.info/api/2/siri/stop-monitoring.json?key=fad509a0-390b-44d5-a448-7d9bd3ca1bdb&MTA&MonitoringRef={stop}&MaximumStopVisits=100")
    data = response.json()
    return {
        "route": data["Siri"]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"][0]["MonitoredVehicleJourney"]["PublishedLineName"],
        "dest" : data["Siri"]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"][0]["MonitoredVehicleJourney"]["DestinationName"],
        "exatime": data["Siri"]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"][0]["MonitoredVehicleJourney"]["MonitoredCall"]["ExpectedArrivalTime"],
        "currtime": data["Siri"]["ServiceDelivery"]["ResponseTimestamp"],
        "distance": data["Siri"]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"][0]["MonitoredVehicleJourney"]["MonitoredCall"]["Extensions"]["Distances"]["PresentableDistance"],
        "estpass": data["Siri"]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"][0]["MonitoredVehicleJourney"]["MonitoredCall"]["Extensions"]["Capacities"]["EstimatedPassengerCount"],
    }

window = tk.Tk()
window.title("Is it Here")
window.geometry("600x400")
window.resizable(False, False)
tk.Label
prompt = tk.Label(window, text="Type your message below:")
bustime = bus(201020)
for key, value in bustime.items():
    print(f"{key.title()}: {value}")
