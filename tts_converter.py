import os
import soundfile as sf
from kokoro import KPipeline

class TTSConverter:
    def __init__(self):
        # 'a' = American English, 'b' = British English
        # This will download the 300MB model automatically on the first run
        self.pipeline = KPipeline(lang_code='a', device='cuda')
        
        # Kokoro voices (af = American Female, am = American Male)
        # You can try 'af_bella', 'af_sarah', 'am_adam', 'am_michael'
        self.voices = {
            "Host 1": "am_michael", # Male
            "Host 2": "af_bella"    # Female
        }

    def _parse_script(self, script):
        """Standard parser to split the script into segments."""
        segments = []
        for line in script.strip().split('\n'):
            if ':' in line:
                speaker, text = line.split(':', 1)
                segments.append((speaker.strip(), text.strip()))
        return segments

    def _generate_and_save_speech(self, text, speaker_name, output_file):
        # This line is the fix! If it doesn't find 'Host 1', it defaults to michael
        voice_name = self.voices.get(speaker_name, "am_michael")
        
        generator = self.pipeline(text, voice=voice_name, speed=1)
        for _, _, audio in generator:
            sf.write(output_file, audio, 24000)
            break