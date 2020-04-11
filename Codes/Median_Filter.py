import nibabel as nib
from scipy import signal, misc
import numpy as np
path = 'E:/Research Materials/Hapetocellular Carcinoma/Dataset/volume-0.nii'
img = nib.load(path)
data = img.get_fdata()
Filtered_Image=signal.medfilt(data, kernel_size=3)
#new_image = nib.Nifti1Image(Filtered_Image, affine=np.eye(4))
ni_img = nib.Nifti1Image(Filtered_Image, img.affine)
nib.save(ni_img, 'output.nii.gz')