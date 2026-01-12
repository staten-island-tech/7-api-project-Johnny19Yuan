import tkinter as tk
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

bus(201020,0)



window = tk.Tk()
window.title("Bustime")
window.geometry("1168x728")
btn = tk.Button(
    window,
    text="Enter",
    width=120,
    height=2,
    font=("Helvetica", 32, "bold"),
    bg="black",
    fg="white",
    activebackground="gray",
    padx=10,
    pady=5
) 
btn.grid(row=10, column=0, padx=10, pady=20)
label = tk.Label(
    window,
    text="Welcome to mta bus time enhanced™ super editon®",
    font=("Comic Sans MS", 14),
    fg="red"
)
label.grid(row=1, column=0, pady=10)

def search():
    print("Searching for:", entry.get())

entry = tk.Entry(window, width=30)
button = tk.Button(window, text="Search", command=search)

entry.grid(row=0, column=0, padx=10, pady=20)
button.grid(row=0, column=1, padx=5, pady=20)
data = bus(201020,0)

label.grid(pady=10)

window.mainloop()