from pydub import AudioSegment
from pydub.silence import split_on_silence
from settings import(
    audio_file_extension,
    frame_rate,
    bit_depth,
    segment_duration,
    min_silence_duration,
    silence_threshold,
    audio_folder_name
)
import os
import log.messages as messages

class AudioProcessor:

    def __init__(self, input_path):
        self.input_path = input_path
        self.input_filename = os.path.splitext(os.path.basename(self.input_path))[0]
        self.input_file_extension = os.path.splitext(self.input_path)[-1].lower()
        self.output_audio_file = f"{self.input_filename}.{audio_file_extension}"
        self.audio_path = os.path.join(audio_folder_name, self.output_audio_file)

    def extract_audio(self):
        
        messages.conversion_started_message(self.input_filename, self.input_file_extension, self.output_audio_file)
        audio = AudioSegment.from_file(self.input_path)
        audio = audio.set_frame_rate(frame_rate).set_sample_width(bit_depth // 8)
        
        audio = self.crop_silence(audio)
        messages.silent_removed_message(self.input_filename)

        audio_path = os.path.join(audio_folder_name, self.output_audio_file)
        audio.export(audio_path, format=audio_file_extension)
        messages.audio_extracted_message(self.input_filename)

    def crop_silence(self, audio):
        
        non_silent_segments = split_on_silence(audio.reverse(), silence_thresh=silence_threshold, min_silence_len=min_silence_duration)
        total_duration = sum(segment.duration_seconds for segment in non_silent_segments)
        cropped_audio = audio[:int(total_duration * 1000)]
        
        return cropped_audio
        
