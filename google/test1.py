from gtts import gTTS
import os
import time
s_t = time.time()
tts = gTTS(text="I would like a shrimp dumpling", lang="en")
tts.save("food.wav")
#当前时间减去预测前的时间
print(f"time cost {time.time() - s_t}")