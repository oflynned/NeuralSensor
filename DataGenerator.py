from Sensor import Sensor
from Constants import Constants

with open(Constants.DATA_FILE_NAME, 'w') as file_data:
    sensor_data = Sensor.generate_n_sensors(Constants.MAX_ROWS, Constants.MAX_COLS)
    print sensor_data
    file_data.write(str(sensor_data))