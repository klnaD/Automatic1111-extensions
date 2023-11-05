import os
from pathlib import Path

IS_RUN: bool = False
BASE_PATH = os.path.join(Path(__file__).parents[1])
DEVICE_LIST: list = ["CPU", "CUDA"]

def updateDevice():
    try:
        LAST_DEVICE_PATH = os.path.join(BASE_PATH, "last_device.txt")
        with open(LAST_DEVICE_PATH) as f:
            for el in f:
                device = el.strip()
    except:
        device = "CPU"
    return device

DEVICE = updateDevice()
