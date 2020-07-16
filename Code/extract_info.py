from PIL import Image
import pytesseract
import os
import sys

folder = "../Data/Chapter-{}".format(sys.argv[1])
out_folder = "../Results/Chapter-{}".format(sys.argv[1])

if os.path.exists("../Results") == False:
	os.mkdir("../Results")

if os.path.exists(out_folder) == False:
	os.mkdir(out_folder)

for file in os.listdir(folder):
	filepath = os.path.join(folder, file)
	img = Image.open(filepath)
	text = pytesseract.image_to_string(img)
	out_fpath = os.path.join(out_folder, file.replace('.jpg', '.txt'))
	with open(out_fpath, 'w') as f:
		f.write(text)