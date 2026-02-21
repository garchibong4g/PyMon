# PyMon

PyMon is a real-time monitoring system that uses an Arduino Uno with DS18B20 and INA219 sensors to track temperature, voltage, and current.  
Live sensor data is streamed and visualized through a Python-based interface, enabling efficient system monitoring and analysis.

---

## 🎯 Features

### 🔌 Hardware Monitoring
- **Temperature Tracking**: Real-time temperature measurement using the DS18B20 sensor
- **Voltage Monitoring**: Accurate voltage sensing via the INA219 module
- **Current Measurement**: Continuous current tracking for power analysis

### 🖥️ Software Interface
- **Live Data Display**: Real-time visualization through a Python application
- **Serial Communication**: Reliable data transfer between Arduino and Python
- **Cross-Platform Support**: Runs on Windows, macOS, and Linux

---

## 📚 Libraries Used

### Arduino Libraries
- OneWire – Communication with the DS18B20 temperature sensor
- DallasTemperature – Temperature data handling for DS18B20
- Adafruit_INA219 – Voltage and current sensing via INA219
- Wire – I2C communication

### Python Libraries
- pyserial – Serial communication with Arduino
- matplotlib – Real-time data plotting


---

## 🔄 Project Workflow

1. Arduino reads temperature, voltage, and current data from connected sensors.
2. Sensor readings are transmitted to the computer via USB serial communication.
3. Python receives and parses incoming serial data.
4. Data is processed and visualized in real time.
5. Live numerical values and plots are displayed to the user.

---

## 🧰 Hardware Requirements
- Arduino Uno
- DS18B20 Temperature Sensor
- INA219 Voltage and Current Sensor
- Breadboard
- Jumper wires
- USB cable
- External power source (optional)

---

## 💻 Software Requirements
- Arduino IDE
- Python 3.8 or higher
- Installed Arduino sensor libraries
- Installed Python libraries listed above

---

## 📤 Output
- Real-time temperature readings (°C)
- Live voltage measurements (V)
- Live current measurements (A)
- Real-time plots and console output

---

## 🙏 Acknowledgements
- Arduino open-source community
- Adafruit for sensor libraries and documentation
- Python open-source ecosystem
- Embedded systems learning resources
