import os

IMAGE_SIZE = 128
SCREEN_HEIGHT = 512
SCREEN_WIDTH = 768
NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 16
MARGIN = 8

ASSET_DIR = 'assets2'
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']
assert len(ASSET_FILES) == 8
