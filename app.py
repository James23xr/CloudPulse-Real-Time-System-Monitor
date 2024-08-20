import psutil
from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route("/")
def index():
    # Get CPU utilization over a 1 second interval
    cpu_percent = psutil.cpu_percent(interval=0.1)
    
    # Get memory utilization
    mem_percent = psutil.virtual_memory().percent
    
    message = None
    if cpu_percent > 10 or mem_percent > 80:
        message = "ALERT ALERT DANGER! <br> High CPU or Memory Utilization detected.<br> Please Scale Up"
    
    print(f"Rendering template with CPU: {cpu_percent}%, Memory: {mem_percent}%")
    return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=message)

if __name__ == '__main__':
    print("Starting Flask app...")
    print(f"Initial CPU Utilization: {psutil.cpu_percent(interval=1)}%")
    print(f"Initial Memory Utilization: {psutil.virtual_memory().percent}%")
    app.run(debug=True, host='0.0.0.0')