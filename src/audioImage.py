# Converting audio files to spectrogram
from os import path, listdir
import matplotlib.pyplot as plt
import librosa
import librosa.display
import warnings
warnings.filterwarnings("ignore")


DATA_ROOT = "../input"

def image_generator(audio_file_name, train = None):
    if train:
        audio_file_path = path.join(DATA_ROOT, "my_train", "train_audio", audio_file_name)
    else:
        audio_file_path = path.join(DATA_ROOT, "test_data", "test_audio", audio_file_name)

    x, sr = librosa.load(audio_file_path, sr=32000)
    X = librosa.stft(x)  # for FFT
    Xdb = librosa.amplitude_to_db(abs(X))
    fig = plt.figure(figsize=(14, 14))
    librosa.display.specshow(Xdb, sr = sr, x_axis = "time", y_axis = "hz")
    plt.axis("off")
    plt.close(fig)  # Save images without displaying

    image_name = audio_file_name.split(".")[0]
    if train:
        fig.savefig(path.join(DATA_ROOT, "my_train", "train_images",image_name + ".png"), bbox_inches='tight')
    else:
        fig.savefig(path.join(DATA_ROOT, "test_data", "test_images",image_name + ".png"), bbox_inches='tight')


train_images_list = listdir(path.join(DATA_ROOT, "my_train", "train_audio"))
test_images_list = listdir(path.join(DATA_ROOT, "test_data", "test_audio"))

for name in train_images_list:
    image_generator(name, train = True)
for name in test_images_list:
    image_generator(name, train = False)