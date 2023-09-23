import configparser

config = configparser.ConfigParser()
config.read('config.ini')

### AUDIO CONFIG ###
audio_file_extension = config.get('AUDIO_CONFIG', 'AUDIO_FILE_EXTENSION')
frame_rate = config.getint('AUDIO_CONFIG', 'FRAME_RATE')
bit_depth = config.getint('AUDIO_CONFIG', 'BIT_DEPTH')
segment_duration = config.getint('AUDIO_CONFIG', 'SEGMENT_DURATION')
min_silence_duration = config.getint('AUDIO_CONFIG', 'MIN_SILENCE_DURATION')
silence_threshold = config.getfloat('AUDIO_CONFIG', 'SILENCE_THRESHOLD')

### FOLDER ###
audio_folder_name = config.get('FOLDER', 'AUDIO_FOLDER')
log_folder_name = config.get('FOLDER', 'LOG_FOLDER')



