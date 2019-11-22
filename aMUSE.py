import warnings
import glob
import os

warnings.filterwarnings('ignore')


########## USER PARAMETERS ######################

path = '/Users/fgran/Dropbox/MUSE_GCs/CL0349/' #with final /
datacube_name = 'CL0349.fits' #image names will be datacube_name without .fits
img_name = datacube_name.split('.fits')[0]
#v_image = 'IMAGE_FOV_0002.fits'
#r_image = 'IMAGE_FOV_0003.fits'
#i_image = 'IMAGE_FOV_0004.fits'
#w_image = 'Cl0034_white.fits'
#reference_image = w_image

#detect_tresh = 2.0
#analysis_tresh = 2.0

#################################################

#Create Folders 
os.chdir('%s' %path) #move to path
os.system('mkdir fits slice_catalogs')

os.chdir('%sfits/' %path) #move to path/fits/
os.system('mv ../%s %sfits/' %(datacube_name, path)) #move the datacube to the /fits/ folder
os.system('missfits -c ../../default_files/default.missfits %s' %datacube_name) #extract the datacubes
