import os

INPUT_DATASET = "/content/drive/My Drive/Breast-Cancer-Detection/input/IDC_regular_ps50_idx5"

BASE_PATH = "idc/idc"
TRAIN_PATH = os.path.sep.join([BASE_PATH, "training"])
VAL_PATH = os.path.sep.join([BASE_PATH, "validation"])
TEST_PATH = os.path.sep.join([BASE_PATH, "testing"])

TRAIN_SPLIT = 0.8
VAL_SPLIT = 0.1
