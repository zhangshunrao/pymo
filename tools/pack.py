# Copyright (c) 2005 Nokia Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ROTATE_90=3,ROTATE_180=4,ROTATE_270=5,

import string
import os
import struct

voice_folder=u'C:\\S60\\devices\\S60_3rd_FP2_SDK_v1.1\\epoc32\\winscw\\c\\Data\\python\\voice\\'
file_extension=u'.wav'
nullstring='\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'
voice=[]
voicefile=file(u'voice.pak','wb')
voicefiles=os.listdir(voice_folder)
voiceoffset=0
for voicefilename in voicefiles:
    if voicefilename.endswith(file_extension):
        voicesize=os.path.getsize(voice_folder+voicefilename)
        voice.append((voicefilename[:-len(file_extension)],voiceoffset,voicesize))
        voiceoffset+=voicesize
contentoffset=len(voice)*(32+4*2)+4
voicefile.write(struct.pack('i',len(voice)))
for voiceentry in voice:
    voicefile.write(voiceentry[0])
    voicefile.write(nullstring[:32-len(voiceentry[0])])
    voicefile.write(struct.pack('i',voiceentry[1]+contentoffset))
    voicefile.write(struct.pack('i',voiceentry[2]))
for voiceentry in voice:
    singlevoicefile=file(voice_folder+voiceentry[0]+file_extension,'rb')
    rawbuffer=singlevoicefile.read()
    voicefile.write(rawbuffer)
    singlevoicefile.close()
voicefile.close()
