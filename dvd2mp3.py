#!/usr/bin/python3
#
# reads an input file of the following format
#
# track_number;track_name;artist_name;album_title;album_artist;year;start_time;end_time
#
# and creates MP3 files for each line of the file by reading the audio between the
# given times and converting to MP3 with ID3 tags according to the data
#
# flac files are created with Vorbis tags and then downscaled to stereo audio and
# converted to mp3 separately
# 

import subprocess
import csv
import sys
import re
import datetime as dt


def process_track(input, number, title, artist, atitle, aartist, year, start, end, volboost):
    filename = make_filename_from_title(number, title, 'flac')

    # calculate the duration since ffmpeg wants start+duration rather than start to stop times
    start_time = datetime_from_str(start)
    end_time = datetime_from_str(end)
    duration = end_time - start_time

    # build the command to rip to flac audio
    flaccmd = 'ffmpeg -ss "{}" -t "{}" -i "{}" -metadata TITLE="{}" -metadata ARTIST="{}" -metadata ALBUM="{}" -metadata ALBUM_ARTIST="{}" -metadata DATE="{}" -metadata TRACKNUMBER="{}" -acodec flac "{}"'.format(
        start, str(duration), input, title, artist, atitle, aartist, year, number, filename)
    print(flaccmd)
    subprocess.run(flaccmd, shell=True)

    # now convert the flac to mp3 with proper tags
    mp3name = make_filename_from_title(number, title, 'mp3')
    mp3cmd = 'ffmpeg -i "{}" -q:a 1 -ac 2 "{}"'.format(filename, mp3name)
    if volboost is not None:
        mp3cmd = 'ffmpeg -i "{}" -filter:a "volume={}" -q:a 1 -ac 2 "{}"'.format(filename, volboost, mp3name)
    subprocess.run(mp3cmd, shell=True)


def datetime_from_str(str):
    t = None
    try:
        t = dt.datetime.strptime(str, '%H:%M:%S.%f')
    except ValueError:
        t = dt.datetime.strptime(str, '%H:%M:%S')
    return t


def is_integer(s):
    "returns True if the string is an integer and False otherwise"
    try:
        int(s)
        return True
    except ValueError:
        return False


def make_filename_from_title(track, title, ext):
    track_num = '{:02d}'.format(int(track))
    s = re.sub('[\s/\'\"]', '_', title)
    return '{}_{}.{}'.format(str(track_num), s, ext).lower()


def read_track_info(ifile):
    "reads the given input file and returns a list of lists"
    tracks = []
    with open(ifile) as f:
        r = csv.reader(f, delimiter=';')
        for row in r:
            # if first field is not a number, skip it (probably a header row)
            if not is_integer(row[0]):
                continue
            else:
                tracks.append(row)
    return tracks

 
if __name__ == '__main__':
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("usage: dvd2mp3.py <source_file> <track_file> [<volume_scale>]")
        sys.exit(1)
    volboost = None
    if len(sys.argv) == 4:
        volboost = sys.argv[3]
    source_file = sys.argv[1]
    track_file = sys.argv[2]
    tracks = read_track_info(track_file)
    for track in tracks:
        print('processing track \'{}\'...'.format(track[1]))
        process_track(source_file, track[0], track[1], track[2], track[3],
                      track[4], track[5], track[6], track[7], volboost)
