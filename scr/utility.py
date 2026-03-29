import os

GAME_PATH = os.path.dirname(os.path.abspath(__file__))

def get_asset_path(filename):
    """Returns the full path to a file in the assets folder."""
    return os.path.join(GAME_PATH, "assets", filename)