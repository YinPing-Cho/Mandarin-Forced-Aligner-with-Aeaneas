import os
from aligner import align, split
from split_text import splittext

path = r'main directory here'
dir_list = os.listdir(path)
print(dir_list)

chunks_path = os.path.join(path, 'Chunks')
chunks_list = os.listdir(chunks_path)
print(chunks_list)

def processAll(audio_text_folder, audio_file, text_file):
    ######################## IO Arguments Here ###########################
    syncmap_file = text_file
    main_title = text_file.replace('.txt', '')
    ######################################################################

    audio_file_path = os.path.join(audio_text_folder, audio_file)

    text_file_path = audio_text_folder
    oritext_file_path = os.path.join(text_file_path, text_file)
    splittext_file_path = os.path.join(text_file_path, text_file.replace('.txt', '_split.txt'))

    syncmap_file_path = os.path.join(audio_text_folder, 'syncmap_file')
    if not os.path.exists(syncmap_file_path):
        os.makedirs(syncmap_file_path)
    syncmap_file_path = os.path.join(syncmap_file_path, syncmap_file)

    out_dir = r'output directory here'
    out_dir = os.path.join(out_dir, main_title)
    if os.path.exists(out_dir):
        return
    os.mkdir(out_dir)
    out_dir = os.path.join(out_dir, main_title)

    print("Text processed: ", splittext(oritext_file_path))
    print("Aligned: ", align(audio_file_path, splittext_file_path, syncmap_file_path))
    print("Split: ", split(audio_file_path, syncmap_file_path, out_dir, main_title))
    print("Done.")

for AudioText in chunks_list:
    AudioText_path = os.path.join(chunks_path, AudioText)
    for text_file in os.listdir(AudioText_path):
        if text_file.endswith(".txt") and not text_file.startswith('z_'):
            audio_file = 'NULL'
            with open(os.path.join(AudioText_path, text_file), 'r', encoding="utf8") as istr:
                with open(os.path.join(AudioText_path, 'z_'+text_file), 'w', encoding="utf8") as ostr:
                    for idx, line in enumerate(istr):
                        if idx == 0:
                            audio_file = line.replace('\n', '')
                            if (audio_file == 'NULL'):
                                break
                        else:
                            ostr.write(line)
            if (audio_file != 'NULL'):
                print(AudioText_path)
                print(AudioText)
                print(audio_file)
                processAll(AudioText_path, audio_file, 'z_'+text_file)

