import os

# get the config from adaship_config.ini
if "adaship_config.ini" in os.listdir(os.path.join(os.path.dirname(__file__))):
    with open(os.path.join(os.path.dirname(__file__), "adaship_config.ini"), 'r') as config_ini:
        ships = dict()
        for line in config_ini.readlines():
            key, value = tuple(map(lambda x: x.strip(), line.split(":")))
            if key.lower() == "board":
                try:
                    board_size = tuple(map(lambda x: int(x.strip()), value.strip().split("x")))
                    if not (5 <= board_size[0] <= 80 or 5 <= board_size[1] <= 80):
                        print("Not a valid board size!")
                        print("Auto setting board size to 10 x 10")
                        board_size = (10, 10)
                except ValueError:
                    print("Error: Cannot parse board size from the adaship_config.ini")
                    print("Auto setting board size to 10 x 10")
                    board_size = (10, 10)
            elif key.lower() == "boat":
                boat, size = tuple(map(lambda x: x.strip(), value.split(",")))
                # boat size must be a natural number
                ships[boat] = int(size)
else:
    print("Could not find adaship_config.ini")
    print("Setting the default value ...")
    board_size = (10, 10)
    ships = {
      'Carrier': 5,
      'Battleship': 4,
      'Destroyer': 3,
      'Submarine': 3,
      'Patrol Boat': 2
    }
