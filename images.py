import numpy as np
from scipy.ndimage import shift
from skimage.registration import phase_cross_correlation
from tifffile import imwrite


def proper_imwrite(path, data):
    imwrite(
        path,
        data,
        photometric="minisblack",
        compression="deflate",
        metadata={"axes": "ZYX"},
        imagej=True,
    )


def calc_shift(img, ref):
    shift, error, phase = phase_cross_correlation(img, ref, upsample_factor=100)
    return shift


def shift_3d_image_subpixel(im, shift_mat):
    shifted = np.empty_like(im)

    for i in range(im.shape[0]):
        shifted[i] = shift(im[i], shift_mat, mode="constant")
    return shifted
