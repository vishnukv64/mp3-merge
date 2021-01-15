import glob
from pydub import AudioSegment
import natsort
import time


def audio_concat(files, op_concat_filname):
    filenamesconcat = []
    combined = AudioSegment.empty()
    for filename in files:
        audiofilename = AudioSegment.from_mp3(filename)
        filenamesconcat.extend([audiofilename])

    for fname in filenamesconcat:
        combined += fname

    combined.export(op_concat_filname, format="mp3")


if __name__ == "__main__":
    dirpath = "mp3_files/"
    generated_concat_file = "combined_audio_file.mp3"

    filenames = glob.glob(dirpath+'*.mp3')
    sorted_files = natsort.natsorted(filenames, reverse=False)
    timer = time.perf_counter()
    audio_concat(sorted_files, generated_concat_file)
    print(
        f"time taken to merge all mp3 files is: {time.perf_counter() - timer}")
