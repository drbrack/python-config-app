import json
import time
import os

def main():
    config_path = os.getenv('CONFIG_PATH', 'config.json')

    # Read configuration file
    with open(config_path, 'r') as file:
        config = json.load(file)

    # Print the value every 5 seconds
    while True:
        print(config["value"])
        time.sleep(5)

if __name__ == "__main__":
    main()
