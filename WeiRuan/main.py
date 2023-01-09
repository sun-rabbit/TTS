# -*- coding:utf-8 -*-
from MSspeechAPI_class import MsSpeechRequest
def main():
    requset = MsSpeechRequest(audiofile=('output.wav'))
    response = requset.returnResult()
    print( response)

main()