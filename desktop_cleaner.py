import os



def remove_files():
    desktop = "/users/spcarton/desktop"
    for f in os.listdir(desktop):
        os.remove("/users/spcarton/desktop/" + f)


remove_files()
