import os, sys, time, glob, csv, math, datetime, sqlite3, numpy as np, pdb # Crucial libraries
import matplotlib.mlab as mlab, matplotlib.pyplot as plt # Plotting libraries
import h5py as parser
import pprint

# Note by Sidwyn:
# Pdb is useful for debugging. Simply put pdb.set_trace() and it will stop at that breakpoint.

# Path to the Million Song Dataset subset
msd_subset_path='/Users/maxwolffe/Documents/Cal/Fall2015/CS194/MillionSongSubset'
msd_subset_data_path=os.path.join(msd_subset_path,'data')
msd_subset_addf_path=os.path.join(msd_subset_path,'AdditionalFiles')
assert os.path.isdir(msd_subset_path),'wrong path' # sanity check

# Path to the Million Song Dataset code
msd_code_path='/Users/maxwolffe/Documents/Cal/Fall2015/CS194/MillionSongSubset/MSongsDB'
assert os.path.isdir(msd_code_path),'wrong path' # sanity check
sys.path.append( os.path.join(msd_code_path,'PythonSrc') )

import hdf5_getters # This has to be after the above for $PATH reasons.
