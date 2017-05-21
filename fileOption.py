try:
    fh=open("res/demoFile", "w")
    fh.write("test file option")
except IOError:
    print("fail to read this file")
else:
    print("option success")
    fh.close()