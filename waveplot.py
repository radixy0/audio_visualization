import librosa
import librosa.display
import argparse

class Options:
    """
    A class to manage command line options
    """

    infile = None           # file list that we will read looking for entries
    
    image = 'output.png'  # image name output

    def __init__(self):
        """
        Inits the class
        """
        self.infile = None
        
        self._get_command_line_arguments()

    # End of init() function


    def _get_command_line_arguments(self):
        """
        Defines and gets all the arguments for the command line using
        argparse module. This function is called in the __init__ function
        of this class.
        """

        parser = argparse.ArgumentParser(description='Script to analyse flexlm log files.')

        parser.add_argument('-i', '--image', action='store', dest='image', help='Image output name, defaults to image.png', default='image.png')
        parser.add_argument('files', metavar='Files', type=str, nargs='+', help='Input audio file')

        self.options = parser.parse_args()

        
        self.image = self.options.image
        self.infile = self.options.files


my_opts = Options()

filename = my_opts.infile
y, sr = librosa.load(filename)
# trim silent edges
whale_song, _ = librosa.effects.trim(y)
librosa.display.waveplot(whale_song, sr=sr)