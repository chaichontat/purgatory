# %%
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


# %%
from imagecodecs import (
    imread,
    jpegxl_decode,
    jpegxl_encode,
    jpegxr_decode,
    jpegxr_encode,
)

# fig, axs = plt.subplots(ncols=4, figsize=(20, 5), dpi=200)

# axs[0].imshow(ex[20, 1600:1800, 400:600], interpolation="none")
# axs[0].axis("off")
# # title is the size of the object
# axs[0].set_title(f"Original {ex.size * 2 / 1024 / 1024:.2f} MB")
# for level, ax in zip([0.5, 0.6, 0.7], axs[1:]):
#     res = jpegxr_decode(b := jpegxr_encode(ex, level=level, photometric=2))[
#         20, 1600:1800, 400:600
#     ]
#     ax.imshow(res, interpolation="none")
#     ax.set_title(f"JPEG-XL, {level=}, {len(b)/ 1024 / 1024:.2f} MB")
#     ax.axis("off")
# %%

# imread("output_22610.tif")

# %%
img = np.random.randint(0, 256, size=(100, 100, 8), dtype=np.uint16)
jpegxr_decode(jpegxr_encode(img))

# %%
