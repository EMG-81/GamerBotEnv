import cv2
from pynput.keyboard import Key
import pyaudio
import src.Helper.constance as constance


class Settings:
    capturing = {
        'video_frame_rate': 30,
        'video_resolution': (0, 0),  # (width, height) (0, 0) for original resolution
        'audio_format': pyaudio.paFloat32,
        'audio_sample_rate': 44100,
        'audio_length': 2,  # seconds
    }

    hardware = {
        'screen_resolution': (2560, 1440),  # Your screen resolution. Must be the actual resolution.
        'audio_stereo_mixer_device_id': -1,  # -1 for auto detection
    }

    """-------------------------------------------------------------------------------------------------"""
    template_matching = {
        # do not use normalized ones as that almost always gives you value greater than the threshold
        'method': cv2.TM_CCOEFF_NORMED,
        'threshold': 0.9,
    }

    """-------------------------------------------------------------------------------------------------"""
    neural_network = {
        'time_steps': 10,
        'batch_size': 32,
        'screenshot_input_dim': (1280, 720),
        'model': constance.NN_MODEL_SINGLE
    }

    """-------------------------------------------------------------------------------------------------"""
    keys = {
        'enabled': ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
            "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", ",", ".",
            "Key.space", "Key.shift", "Key.esc", "Key.enter", "Key.backspace", "Key.tab",
            "Key.caps_lock", "Key.left", "Key.up", "Key.right", "Key.down", "Key.alt",
            "Key.f1", "Key.f2", "Key.f3", "Key.f4", "Key.f5", "1", "2", "3", "4", "5",
            "6", "0", "Key.ctrl_l"] + ["Button.left", "Button.right"]
    }
