import cv2
import numpy as np


def generate_heatmap(bbox_locations, frame_shape, scale_factor=0.8):
    """Generate a coloured heatmap from a list of bounding-box locations."""
    heatmap = np.zeros((frame_shape[0], frame_shape[1]), dtype=np.float32)
    for x, y, w, h in bbox_locations:
        center_x = int(x + w / 2)
        center_y = int(y + h / 2)
        heatmap[center_y, center_x] += 1
    heatmap = cv2.GaussianBlur(heatmap, (21, 21), 0)
    heatmap = cv2.normalize(heatmap, None, 0, 255, cv2.NORM_MINMAX)
    heatmap = np.uint8(heatmap)
    heatmap_colored = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    heatmap_colored = cv2.cvtColor(heatmap_colored, cv2.COLOR_BGR2RGB)
    resized_heatmap = cv2.resize(
        heatmap_colored,
        (int(frame_shape[1] * scale_factor), int(frame_shape[0] * scale_factor)),
    )
    return resized_heatmap


# Mapping of YOLO class IDs to species names
CLASS_ID_TO_SPECIES = {
    0: "Human",
    1: "Elephant",
    2: "Lion",
    3: "Giraffe",
}
