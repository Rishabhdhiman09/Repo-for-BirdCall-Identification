import pandas as pd
import numpy as np
from os import makedirs, path, listdir
from pydub import AudioSegment

DATA_ROOT = "../input"
DATA_SAVED = "../input/test_data/test_audio"
test_summary = pd.read_csv(path.join(DATA_ROOT, "test_data", "example_test_audio_summary.csv"))

test_audio_files = listdir(path.join(DATA_ROOT, "test_data/test_audio"))
audio_file_names = [name.split(".")[0] for name in test_audio_files]


sec_data = []
def second_list(audio_file_names):
    for audio_file in audio_file_names:
        file_nm = audio_file.split("_")[0]
        data = test_summary[test_summary["filename"] == file_nm]["seconds"].values
        sec_data.append(data)

second_list(audio_file_names)


def cut_audio(audio_file, start_milli, end_milli, audio_name):
    startTime = start_milli
    endTime = end_milli
    audio_path = DATA_ROOT + "/test_data/test_audio/" + audio_file 
    song = AudioSegment.from_mp3(audio_path)
    extract = song[startTime:endTime]
    extract.export( path.join(DATA_ROOT, "test_data", "test_audio", audio_name+"_"+str(int(endTime/1000)) + ".mp3"), format="mp3")




for i, (audio_file, audio_name) in enumerate(zip(test_audio_files, audio_file_names)):
    for sec in sec_data[i]:
        audio_file = audio_file
        start_milli = (sec - 5) * 1000
        end_milli = sec * 1000
        cut_audio(audio_file, start_milli, end_milli, audio_name)


