import torch
import torchaudio as ta

from chatterbox.vc import ChatterboxVC

# Require CUDA GPU
if not torch.cuda.is_available():
    raise RuntimeError("CUDA GPU not available. This script requires a CUDA-capable GPU.")

device = "cuda"
print("Using device: cuda")

AUDIO_PATH = "YOUR_FILE.wav"
TARGET_VOICE_PATH = "YOUR_FILE.wav"

model = ChatterboxVC.from_pretrained(device)
wav = model.generate(
    audio=AUDIO_PATH,
    target_voice_path=TARGET_VOICE_PATH,
)
ta.save("testvc.wav", wav, model.sr)
