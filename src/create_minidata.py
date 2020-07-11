from os import makedirs, path, listdir
import random
from shutil import copy
import pandas as pd

DATA_NAME = "train_data"
DATA_ROOT = "../input"
DATA_SAVED = "../input"

# Function for getting file names and their path
def get_my_train():
    data_path = path.join(DATA_ROOT, DATA_NAME)
    # Check whether this path exists
    if not path.exists(data_path):
        raise Exception("{} path is not found please check".format(data_path))
    files_name_path = []
    for i, files in enumerate(listdir(path.join(data_path, "train_audio"))):
        file_name = files
        file_path = path.join(data_path, "train_audio", files)
        files_name_path.append((file_name, file_path))
        if i == 100:
            break

    return files_name_path


# Move files to new folder
def move_files(mini_arr):
    makedirs(path.join(DATA_SAVED, "my_train", "train_audio"))
    for file, file_path in mini_arr:
        dst_path = path.join(DATA_SAVED, "my_train", "train_audio", file)
        copy(file_path, dst_path)

# Get csv for extracted trained data
def get_mini_train(mini_arr):
    csv_path = path.join(DATA_SAVED, "my_train")
    file_names = list(zip(*mini_arr))[0]
    train_initial = pd.read_csv(path.join(DATA_ROOT, DATA_NAME, "train.csv"))
    train_final = train_initial[train_initial["filename"].isin(file_names)]
    train_final.to_csv(path.join(csv_path, "train.csv"))


if __name__ == "__main__":
    mini_arr = get_my_train()
    move_files(mini_arr)
    get_mini_train(mini_arr)