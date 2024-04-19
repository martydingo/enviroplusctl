import time
import enviroplus
import bme280
import ltr559
import pms5003
import vcgencmd


class EnvPlus:
    useParticulateMatterSensor = True

    def __init__(self) -> None:
        self.__initialize_sensors__()

    def __initialize_sensors__(self):
        # BME280 climate sensor
        self.climateSensor = bme280.BME280()
        # LTR559 light sensor
        self.lightSensor = ltr559.LTR559()

        if self.useParticulateMatterSensor == True:
            # PMS5003 particulate sensor
            self.particulateSensor = pms5003.PMS5003()
            self.particulateSensor

        # MICS6814 Gas sensor
        gasSensor = enviroplus.gas
        while not gasSensor.available():
            time.sleep(1)
        self.GAS_SENSOR = gasSensor

    def __calibrate_temperature__(self, temperature):
        vcGenCMD = vcgencmd.Vcgencmd()
        cpuTemp = vcGenCMD.measure_temp()
        return temperature - (cpuTemp * (self.temperatureTuningFactor * 10))

    def getTemperature(self):
        return self.climateSensor.get_temperature()

    def getHumidity(self):
        return self.climateSensor.get_humidity()

    def getPressure(self):
        return self.climateSensor.get_pressure()
