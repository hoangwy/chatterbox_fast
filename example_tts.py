import torchaudio as ta
import torch
from chatterbox.tts import ChatterboxTTS

# Automatically detect the best available device
if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"

print(f"Using device: {device}")

model = ChatterboxTTS.from_pretrained(device=device)

text = "On November seventh, Air France-KLM announced its intention to formally bid for a significant stake in TAP Air Portugal. This move comes as the Portuguese government plans to privatize a portion of its national airline.\n\nAir France-KLM's CEO, Ben Smith, shared this news during a press conference where the company presented its quarterly financial results. This confirms earlier speculation that the airline group was interested in TAP.\n\nMeanwhile, the Portuguese government confirmed nearly two years ago, in September two thousand twenty-three, its plan to privatize part of TAP. The government aims to sell forty-four point nine percent to a private investor and five percent to employees, while retaining a fifty point one percent majority stake.\n\nAccording to officials, interested parties must submit their proposals by November twenty-second. This follows a long history of TAP moving between state and private ownership, with the government fully taking over again during the COVID-nineteen pandemic.\n\nEarlier this year, in July, the government approved the law outlining TAP's privatization, stating its goal was to stop \"pouring money into a bottomless pit.\" This upcoming bid from Air France-KLM marks a significant step in that process.",
wav = model.generate(text)
ta.save("test-1.wav", wav, model.sr)

# If you want to synthesize with a different voice, specify the audio prompt
AUDIO_PROMPT_PATH = "YOUR_FILE.wav"
wav = model.generate(text, audio_prompt_path=AUDIO_PROMPT_PATH)
ta.save("test-3.wav", wav, model.sr)
