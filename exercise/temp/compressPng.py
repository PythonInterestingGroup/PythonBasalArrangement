import tinify

tinify.key = "gXGo3SfL0iKAyg13IwgFwx3UHtjXVtu_"

def compress(filename):
	source = tinify.from_file('/Users/ursus/Desktop/' + filename)
	source.to_file('/Users/ursus/Desktop/2' + filename)
	print('压缩 '+ filename + '压缩完成')
	
if __name__ == '__main__':
	compress('esf_house_main_guide.png')
	