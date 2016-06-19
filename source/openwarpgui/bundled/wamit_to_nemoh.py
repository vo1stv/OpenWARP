# Import the bemio.mesh_utilities module
import os
import sys
import subprocess
from bemio.mesh_utilities import mesh
import numpy as np

for subdir, dirs, files in os.walk("wamit"):
 for name in  files:
  filepath = os.getcwd() + os.sep + subdir + os.sep + name
  if filepath.endswith(".gdf"): 
   # Read WAMIT mesh
   print filepath
   filetr = os.getcwd() + os.sep + subdir + os.sep + 'tr.' + name
   #subprocess.call('cat ' + filepath + ' | tr -s " " > ' + filetr , shell=True)
   try:
    # Save to a NEMOH mesh
    buoy = mesh.read(file_name=filepath)
    buoy.write(mesh_format='NEMOH')  
   except:
    print "exception %s reading gdf" % sys.exc_info()[0]


