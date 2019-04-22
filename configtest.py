import configparser
import sys

config = configparser.ConfigParser()
config.read("configtest.cfg")

try:
    directory_settings = config["directories"]
    common_settings = config["common"]
except KeyError as e:
    print("Error reading the configuration section {}".format(e))
    sys.exit(1)

# Get a string value
data_dir = directory_settings.get("data")
print("Data directory: {}".format(data_dir))

# Note: the get methods return None as a fallback value by default
# so there is no exception raised for missing values

# Use getboolean() to figure out yes/no type values
try:
    debug_mode = common_settings.getboolean("debug")
except ValueError as e:
    print("Error interpreting the boolean value for debug setting: {}".format(e))
else:
    if debug_mode is not None:
        print("Debug mode: {}".format(debug_mode))

# getint() also exists
try:
    port = common_settings.getint("port")
except ValueError as e:
    print("Error getting the port number: {}".format(e))
else:
    if port is not None:
        print("Port: {}".format(port))

