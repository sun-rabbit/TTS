## 输入文件text.txt
## 输出文件file.wav

from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig
import azure.cognitiveservices.speech as speechsdk
import time
s = time.time()
speech_key, service_region = "9bdc7c4062614491960aeb0da531f9e5", "eastus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

speech_config.speech_synthesis_language = "en"
# speech_config.speech_synthesis_voice_name ="zh-CN-XiaoyouNeural"
speech_config.speech_synthesis_voice_name ="en-US-AriaNeural "

audio_config = AudioOutputConfig(filename="file.wav")
synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

with open('text', 'r',encoding='utf-8',errors='ignore') as f:
    text = f.read()

result = synthesizer.speak_text_async(text).get()
stream = AudioDataStream(result)
stream.save_to_wav_file("file.wav")
#当前时间减去预测前的时间
print(f"time cost {time.time() - s}")