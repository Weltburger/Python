import sys
import argparse
import shutil
import os
import subprocess


def main():

    m = argparse.ArgumentParser(description="Trackmix", epilog="Good listening!")
    m.add_argument('--source', '-s', type=str, required=True, help='Source')
    m.add_argument('--destination', '-d', type=str, default=None, help='Output')
    m.add_argument('--count', '-c', type=int, default=None, help='How many files should i cut?')
    m.add_argument('--frame', '-f', type=int, default=10, help='How long(sec)?')
    m.add_argument('--log', '-l', action='store_true', help='Should i log it?')
    m.add_argument('--extended', '-e', action='store_true', help='Little fade in/out')

    source = m.parse_args().source
    destination = m.parse_args().destination
    if destination is None:
        destination = source
    count = m.parse_args().count
    frame = m.parse_args().frame

    # Log
    log = m.parse_args().log
    if log is True:
        log = ' -i '
        log = str(log)
    else:
        log = ' '
        log = str(log)

    # Fade(Угасание)
    fade = m.parse_args().extended
    justForFade = frame - 2
    justForFade = str(justForFade)
    if fade is True:
        fadeStr = ' -ss 00:00:00 -t 00:00:' + str(frame) + '.00 -af \"afade=t=in:ss=0:d=2,afade=t=out:st=' + justForFade + ':d=2"\' -y '
        fadeStr = str(fadeStr)
    else:
        fadeStr = ''
        fadeStr = str(fadeStr)

    # Test source
    if os.path.exists(source) is True:
        # Path exist?
        files = os.listdir(source)
        fileName = os.listdir(source)

        files = [os.path.join(source, file) for file in files]
        files = [file for file in files if os.path.isfile(file)]  # files only in list
        for i in range(len(files)):
            files[i] = '"' + files[i] + '"'
            # fileName[i] = '"'+fileName[i]+'"'
        path_to_ffmpeg = os.path.join(sys.path[0], r'ffmpeg\bin\ffmpeg.exe')  # Path to ffmeg

        # --------------------------------------------------------------------------------------------------------
        # Start side process 'ffmpeg.exe' with params
        # CountParam = 1
        if count is not None:
            for i in range(count):
                subprocess.call(path_to_ffmpeg + log + files[i] + ' -acodec copy -ss 00:00:00 -t 00:00:' + str(
                    frame) + '.00' + ' "' + destination + '\\' + fileName[i] + '"', shell=True)
                if fade is True:
                    subprocess.call(
                        path_to_ffmpeg + log + files[i] + fadeStr + '"' + destination + '\\' + fileName[i] + '"',
                        shell=True)
        else:
            for i in range(len(files)):
                subprocess.call(path_to_ffmpeg + log + files[i] + ' -acodec copy -ss 00:00:00 -t 00:00:' + str(
                    frame) + '.00' + ' "' + destination + '\\' + fileName[i] + '"', shell=True)
                if fade is True:
                    subprocess.call(
                        path_to_ffmpeg + log + files[i] + fadeStr + '"' + destination + '\\' + fileName[i] + '"',
                        shell=True)

        files_arr = os.listdir(destination)
        files_arr = [os.path.join(destination, file) for file in files_arr]
        files_arr = [file for file in files_arr if os.path.isfile(file)]  # files only in list
        fname = ''
        for i in range(len(files_arr)):
            files_arr[i] = files_arr[i].replace(destination + '\\', '')
            fname += 'file ' + "'" + files_arr[i] + "'" + '\n'
        file_info = open(r'' + destination + '/123.txt', 'w')
        file_info.writelines(fname)
        file_info.close()
        subprocess.call(path_to_ffmpeg + ' -f concat -i ' + destination + '/123.txt' + ' -c copy ' + 'mix.mp3' + '', shell=True)

        for the_file in os.listdir(destination):
            file_path = os.path.join(destination, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)

    else:
        print('Wrong path!')


main()
