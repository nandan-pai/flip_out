import random
import os
import game_config2 as gc2

from pygame import image, transform

animals_count = dict((a, 0) for a in gc2.ASSET_FILES)

def available_animals():
    return [animal for animal, count in animals_count.items() if count < 2]

class Animal2:
    def __init__(self, index):
        self.index = index
        self.name = random.choice(available_animals())
        self.image_path = os.path.join(gc2.ASSET_DIR, self.name)
        self.row = index // gc2.NUM_TILES_SIDE
        self.col = index % gc2.NUM_TILES_SIDE
        self.skip = False
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image, (gc2.IMAGE_SIZE - 2 * gc2.MARGIN, gc2.IMAGE_SIZE - 2 * gc2.MARGIN))
        self.box = self.image.copy()
        self.box.fill((150, 150, 150))

        animals_count[self.name] += 1
