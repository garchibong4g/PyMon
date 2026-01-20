#include <Wire.h>
#include <Adafruit_INA219.h>
#include <OneWire.h>
#include <DallasTemperature.h>

//Pin Definitions
#define ONE_WIRE_BUS 2   // DS18B20 data pin

//Sensor Objects 
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature tempSensor(&oneWire);
Adafruit_INA219 ina219;

//Variables 
float temperatureC;
float voltage;
float current;

void setup() {
  Serial.begin(9600);
  Wire.begin();

  tempSensor.begin();

  if (!ina219.begin()) {
    Serial.println("INA219 not detected!");
    while (1);
  }

  Serial.println("Temperature(C),Voltage(V),Current(mA)");
}

void loop() {
  // Read temperature
  tempSensor.requestTemperatures();
  temperatureC = tempSensor.getTempCByIndex(0);

  // Read voltage & current
  voltage = ina219.getBusVoltage_V();
  current = ina219.getCurrent_mA();

  // Send CSV-formatted data
  Serial.print(temperatureC);
  Serial.print(",");
  Serial.print(voltage);
  Serial.print(",");
  Serial.println(current);

  delay(1000);  
}