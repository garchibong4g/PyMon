import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Serial Configuration
PORT = 'COM3'       
BAUD_RATE = 9600

ser = serial.Serial(PORT, BAUD_RATE, timeout=1)

#Data Lists
temperature = []
voltage = []
current = []

MAX_POINTS = 50  

# Plot Setup 
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 8))

def animate(i):
    line = ser.readline().decode('utf-8').strip()
    
    try:
        temp, volt, curr = map(float, line.split(","))

        # Add new values to lists
        temperature.append(temp)
        voltage.append(volt)
        current.append(curr)

        # Keep only last MAX_POINTS values
        if len(temperature) > MAX_POINTS:
            temperature.pop(0)
            voltage.pop(0)
            current.pop(0)

        # Clear and plot
        ax1.clear()
        ax2.clear()
        ax3.clear()

        ax1.plot(temperature, 'r')
        ax1.set_ylabel("Temperature (°C)")
        ax1.set_title("Real-Time Sensor Monitoring")

        ax2.plot(voltage, 'b')
        ax2.set_ylabel("Voltage (V)")

        ax3.plot(current, 'g')
        ax3.set_ylabel("Current (mA)")
        ax3.set_xlabel("Samples")

    except ValueError:
        pass  # Ignore malformed data

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.tight_layout()
plt.show()