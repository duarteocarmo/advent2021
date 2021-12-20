import numpy as np
from scipy.ndimage import generic_filter

with open("20/input.txt") as file:
    data = file.readlines()
    data = [line.rstrip() for line in data]

algo = data[0].replace("#", "1").replace(".", "0")
algo = [int(x) for x in algo]
image_data = data[2:]
image_data = [list(el.replace("#", "1").replace(".", "0")) for el in image_data]
image_data = np.array(image_data, dtype=int)
footprint = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])


PADDING = int(image_data.shape[0] / 2) + 10


def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get("padder", 0)
    vector[: pad_width[0]] = pad_value
    vector[-pad_width[1] :] = pad_value

    return vector


def function(values):
    list_ = [int(x) for x in values.tolist()]
    binary = "".join([str(x) for x in list_])
    binary_value = int(binary, 2)
    return algo[binary_value]


padded = np.pad(image_data, PADDING, pad_with)

results = generic_filter(
    padded,
    function,
    footprint=footprint,
    # mode="constant",
    cval=0,
)

padded = np.pad(results, PADDING, pad_with)

results = generic_filter(
    padded,
    function,
    footprint=footprint,
    # mode="constant",
    cval=0,
)

print(np.sum(results))
