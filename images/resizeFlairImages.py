from PIL import Image
import os, sys

path = "./flairImages/"
dirs = os.listdir(path)

def resize():
	for item in dirs:
		if not item.endswith('.DS_Store'):
			im = Image.open(path + item)
			f,e = os.path.splitext(item)
			imResize = im.resize((30, 30), Image.ANTIALIAS)
			imResize.save("./resizedFlairImages/" + f + ".png", 'PNG', quality = 100)
		
resize()