import datetime
import os
import sys


def convert_to_wav(source_dir):
    os.system(f'cd {source_dir};for i in *.aac; do ffmpeg -n -i "$i" "../wav/${{i%.*}}.wav"; done; cd ../wav/')


def create_dir_if_not_exists(dir_):
    if not os.path.exists(dir_):
        os.mkdir(dir_)


def write_lines_to_file(path, lines_list):
    with open(path, 'w') as f:
        f.write('\n'.join(lines_list))


def read_lines_from_file(path):
    with open(path, 'r') as f:
        data = f.read()
    return data.split('\n')


if __name__ == '__main__':
    playlist_url = str(sys.argv[1])
    print(playlist_url)
    end = playlist_url.find('playlist_')
    base_url = playlist_url[:end]

    now = datetime.datetime.now()
    session_name = datetime.datetime.strftime(now, "%Y-%m-%d_%H-%M-%S")
    data_dir = 'data/' + session_name
    aacs_dir = 'aac/'
    wavs_dir = 'wav/'
    aac_files = 'aac_files.txt'

    create_dir_if_not_exists(data_dir)

    # Download playlist
    os.system(f'wget -O {data_dir}/playlist.txt -c {playlist_url}')
    # Filter aac file lines from playlist
    os.system(f'cat {data_dir}/playlist.txt | grep .aac > {data_dir}/aac_files.txt')

    # Add base url to all aac files
    lines = read_lines_from_file(os.path.join(data_dir, aac_files))

    full_lines = [base_url + '/' + line for line in lines]

    write_lines_to_file(os.path.join(data_dir, 'aac_files.txt'), full_lines)

    # Download all aac file parts
    aac_dir = os.path.join(data_dir, aacs_dir)
    create_dir_if_not_exists(aac_dir)

    os.system(f"wget --directory-prefix={aac_dir} -ci {os.path.join(data_dir, aac_files)}")

    wav_dir = os.path.join(data_dir, wavs_dir)
    create_dir_if_not_exists(wav_dir)

    convert_to_wav(aac_dir)
    os.system('ulimit -n 8000')
    # Merge all with sox
    os.system(f'cd {wav_dir};for i in "*.wav"; do sox $i ../../{session_name}.wav; done')
