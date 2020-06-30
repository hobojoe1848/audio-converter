import argparse
from pydub import AudioSegment

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file",
        help = "Path to the audio file that needs to be converted.")
ap.add_argument("-n", "--name",
        help = "Name of the output file.")
args = vars(ap.parse_args())
if not any(args.values()):
    ap.error("Must at least specify the input file.")

inputaudio = args["file"]
outputname = args["name"]

m4a_audio = AudioSegment.from_file(inputaudio, format="m4a")
#raw_audio = AudioSegment.from_file(inputaudio, format="raw",
                                   #frame_rate=44100, channels=2, sample_width=2)

m4a_audio.export(f"Completed\{outputname}.mp3", format="mp3")
# raw_audio.export(f"Completed\{outputname}_raw.mp3", format="mp3")
