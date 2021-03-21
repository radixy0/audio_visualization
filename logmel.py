import librosa
import librosa.display
import argparse
import matplotlib.pyplot as plt
import numpy as np

class Options:
    """
    A class to manage command line options
    """

    infile = ""         # file list that we will read looking for entries
    
    image = 'logmel.png'  # image name output

    def __init__(self):
        """
        Inits the class
        """
        self.infile = ""
        
        self._get_command_line_arguments()

    # End of init() function


    def _get_command_line_arguments(self):
        """
        Defines and gets all the arguments for the command line using
        argparse module. This function is called in the __init__ function
        of this class.
        """

        parser = argparse.ArgumentParser(description='Script to analyse flexlm log files.')

        parser.add_argument('-i', '--image', action='store', dest='image', help='Image output name, defaults to logmel.png', default='logmel.png')
        parser.add_argument('files', metavar='Files', type=str, help='Input audio file')

        self.options = parser.parse_args()

        
        self.image = self.options.image
        self.infile = self.options.files


my_opts = Options()

filename = my_opts.infile
y, sr = librosa.load(filename)
whale_song, _ = librosa.effects.trim(y)
n_fft = 2048
hop_length = 512
n_mels = 128
D = np.abs(librosa.stft(whale_song, n_fft=n_fft,  hop_length=hop_length))
DB = librosa.amplitude_to_db(D, ref=np.max)
mel = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels)
librosa.display.specshow(DB, sr=sr, hop_length=hop_length, x_axis='time', y_axis='mel')

plt.colorbar(format='%+2.0f dB')
plt.plot(DB)
plt.savefig(Options.image)