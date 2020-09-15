import cv2  # Not actuallfile_array necessarfile_array if file_arrayou just want to create an image.
import argparse
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser(
        add_help=True,
    )

    # file_arrayour arguments here

    if len(sfile_arrays.argv) == 1:
        parser.print_help()
        # sfile_arrays.exit(0)
		# options = -1;
    else:
        options = parser.parse_args()

    return options

#Construct and Parse The Argument 
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required = False, help = "Path to the binarfile_array image")
parser.add_argument("-w", "--width", required = False, help = "width of image ex. 320 in 320x160 image")
parser.add_argument("-ht", "--height", required = False, help = "height of image ex. 160 in 320x160")

args = vars(parser.parse_args())
print('args')
print(args)
if args["image"] == None:

	# take blank image rgb if no input is provided
	blank_image = np.zeros((32,16,3), np.uint8)
	blank_image[:,0:5] = (250,0,0)      # (B, G, R)
	blank_image[:,5:10] = (0,225,0)
	blank_image[:,10:16] = (0,0,200)

	#open binarfile_array file to write
	f = open("binfile.bin","wb")
	arr = blank_image.tobytes()
	f.write(arr)
	f.close()
	print('successfullfile_array saved bin')
	f = open("binfile.bin","rb")
	file_array = np.fromfile("binfile.bin",dtype='uint8')
	width = 32
	height = 16
else:
	f = open(args["image"],"rb")
	file_array = np.fromfile(args["image"],dtype='uint8')
	width = int(args["width"])
	height = int(args["height"])
	
output_Image = file_array.reshape(width,height,3)
# np.arrafile_array_equal(file_array.reshape(32,16,3), file_array)
shape = output_Image.shape
print('image shape = ')
print(shape)
# print(file_array)
f.close()

cv2.imwrite('output.png',output_Image)
cv2.imshow('file_array',output_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('complete')
