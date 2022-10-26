"""MemeEngine class using Pillow."""

from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine:
    """Class to generate actual meme files."""

    meme_font = './LilitaOne-Regular.ttf'
    meme_width = 500
    meme_fill = 'white'
    meme_factor = 18

    def __init__(self, meme_dir: str):
        """Initiate meme engine with path there store produced meme files."""
        self.mem_dir = meme_dir

    def make_meme(self, img: str, body: str, author: str) -> str:
        """Generate Meme with given img, text, and author."""
        caption = f'{body}, {author}'

        with Image.open(img) as meme:
            # resize img
            old_width, old_height = meme.size
            scale = self.meme_width/old_width
            new_size = new_width, new_height = self.meme_width, int(scale*old_height)
            meme = meme.resize(new_size)

            # caption image to a random location on the left half of the image
            # depending on font size
            draw = ImageDraw.Draw(meme)
            font_size = self.meme_width//self.meme_factor
            x, y = 10, random.randint(font_size, new_height-font_size)
            font = ImageFont.truetype(font=self.meme_font, size=font_size)
            draw.text((x, y), caption, fill=self.meme_fill, font=font)

            # save meme to out path determined by MemeEngine object
            meme_name = f'meme_{img.split("/")[-1]}'
            out_path = f'{self.mem_dir}/{meme_name}'
            meme.save(out_path)
        return out_path
