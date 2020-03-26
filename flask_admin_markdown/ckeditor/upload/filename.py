#coding:utf8
import random
import time
from pathlib import Path
import os


def generate_filename(file_pre_path,extension='jpg'):
	while True:
		new_filename = 	time.strftime(
			"%Y-%m-%d %H:%M:%S",
			time.localtime(time.time())
		).replace(' ','_') + "_" + \
			"".join(random.sample('zyxwvutsrqponmlkjihgfedcba',5)) + \
			"." + \
			extension
		file_path = os.path.join(file_pre_path, new_filename)
		file = Path(file_path)
		if not file.exists():
			return new_filename
