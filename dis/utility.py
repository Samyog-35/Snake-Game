import os

GAME_PATH = os.path.dirname(os.path.abspath(__file__))

def get_asset_path(filename: str) -> str:
    """Returns full path to assets folder file."""
    return os.path.join(GAME_PATH, "assets", filename)