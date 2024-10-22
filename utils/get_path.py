import os.path

def get_path():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"file/gameboy.webp")
    return path