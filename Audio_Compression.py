# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 20:31:57 2023

@author: daveh

To compress .wav files to mp3 format

"""
import pydub
from pydub import AudioSegment
import os
from pathlib import Path


def sliced_wav_to_mp3(wav_file_path, folder_out, slice_len_ms= 60000):

    """
    Convert a WAV file to an MP3 file.
    MP3 files are stored in the specified folder.
    Args:
      wav_file_path (str): Path to the WAV file.
      folder_out (str): Path to the output directory.
      slice_len_ms (int): Length of each slice in milliseconds
    """
    audio = AudioSegment.from_wav(wav_file_path)
    # Splitext to extract the file name without extension
    file_name = os.path.splitext(os.path.basename(wav_file_path))[0]
    mp3_path = os.path.join(folder_out, f"{file_name}.mp3")


    with open(mp3_path, 'wb') as f:
        # opening the file
        # 'wb is 'write binary' mode to write to mp3 file
        pass # Not writing anything, just creating the file

    # Slicing the WAV file for processing
    slice_start = 0
    while slice_start < len(audio):
        slice_end = min(slice_start + slice_len_ms, len(audio))
        audio_slice = audio[slice_start:slice_end]

        # Append each slice to the mp3 file
        with open(mp3_path, 'ab') as f:
            # 'ab' is 'append binary'mode to append to mp3 file
            audio_slice.export(mp3_path, format= "mp3", bitrate= "192k") # Bitrate can be adjusted

        slice_start += slice_len_ms

    print(f"{file_name} converted to mp3 format.")

def main():

    
      wav_file_name = "NoTitle.wav"
      
      wav_file_path = r"C:\Users\You\Music\NoTitle.wav" # Local path to file

      #wav_file_path = Path.home()/'Music'/wav_file_name
      #print(wav_file_path)
      folder_out = r"C:\Users\You\Music\My_mp3s" # Folder to save mp3 locally
      # Create folder if it doesn't exist
      if not os.path.exists(folder_out):
          os.makedirs(folder_out)

      sliced_wav_to_mp3(wav_file_path, folder_out)

if __name__ == "__main__":
    main()