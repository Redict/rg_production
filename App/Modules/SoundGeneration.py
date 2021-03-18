import os
import sys
sg_path = os.path.join(os.getcwd(), '..\\..\\rg_sound_generation\\sound_generator')
print(os.path.exists(sg_path))
sys.path.insert(0, sg_path)
print(sg_path)
# from TheSoundOfAIOSR.audiointerface.async_io import stream_capture
#
from sound_generator import get_prediction

async def get_sound():

    inputs = {
        'velocity': 75,
        'pitch': 60,
        'source': 'acoustic',
        'qualities': ['bright', 'percussive'],
        'latent_sample': [0.] * 16
    }

    audio = get_prediction(inputs)

    print(audio)