#Importing the image
import math
import rasterio
import matplotlib.pyplot as plt
from rasterio import plot
#from rasterio import plot

image_file = "photo.tiff"
sat_data = rasterio.open(image_file)

#view original image
plot.show(sat_data)

#Calculating the dimensions of the image on earth in metres
width_in_projected_units = sat_data.bounds.right - sat_data.bounds.left
height_in_projected_units = sat_data.bounds.top - sat_data.bounds.bottom

print("Width: {}, Height: {}".format(width_in_projected_units, height_in_projected_units))

#Rows and Columns
print("Rows: {}, Columns: {}".format(sat_data.height, sat_data.width))

#Converting the pixel co-ordinates to longitudes and latitudes

# Upper left pixel
row_min = 0
col_min = 0

# Lower right pixel.  Rows and columns are zero indexing.
row_max = sat_data.height - 1
col_max = sat_data.width - 1

# Transform coordinates with the dataset's affine transformation.
topleft = sat_data.transform * (row_min, col_min)
botright = sat_data.transform * (row_max, col_max)

print("Top left corner coordinates: {}".format(topleft))
print("Bottom right corner coordinates: {}".format(botright))

#Bands
#The image that we are inspecting is a multispectral image consisting of 4 bands int he order B,G,R,N where N stands for near infrared.each band is stored as a numpy array.

print(sat_data.count)

# sequence of band indexes
print(sat_data.indexes)

#Visualising the Satellite Imagery
#We will use matplotlib to visualise the image since it essentially consists of arrays.

# Load the 3 bands into 2d arrays - recall that we previously learned PlanetScope band order is BGRN.
b, g, r, n = sat_data.read()

# Displaying the blue band.
fig = plt.imshow(b)
plt.show()

# Displaying the green band.
fig = plt.imshow(g)
fig.set_cmap('gist_earth')
plt.show()

# Displaying the red band.
fig = plt.imshow(r)
fig.set_cmap('inferno')
plt.colorbar()
plt.show()

# Displaying the infrared band.

fig = plt.imshow(n)
fig.set_cmap('winter')
plt.colorbar()
plt.show()




