from aeneas.executetask import ExecuteTask
from aeneas.task import Task
from pydub import AudioSegment

def align(audio_file_path, text_file_path, syncmap_file_path):
    # create Task object
    config_string = "task_language=zh|is_text_type=plain|os_task_file_format=txt"
    task = Task(config_string=config_string)
    task.audio_file_path_absolute = audio_file_path
    task.text_file_path_absolute = text_file_path
    task.sync_map_file_path_absolute = syncmap_file_path

    # process Task
    ExecuteTask(task).execute()
    # output sync map to file
    task.output_sync_map_file()

    return True

def split(audio_file_path, syncmap_file_path, out_dir, title):
    OriAudio = AudioSegment.from_mp3(audio_file_path)
    file_count = 0
    with open(syncmap_file_path, 'r', encoding="utf8") as istr:
        with open(out_dir+'.txt', 'w', encoding="utf8") as ostr:
            for line in istr:
                formatted = line.split()
                t1 = float(formatted[1]) * 1000 #Works in milliseconds
                t2 = float(formatted[2]) * 1000
                newAudio = OriAudio[t1:t2]
                file_count += 1
                newAudio.export(out_dir+'_'+ str(file_count).zfill(6) +'.wav', format="wav") #Exports to a wav file in the current path.

                text = title+'_'+ str(file_count).zfill(6) +'.wav' + '|'
                formatted = formatted[3:]
                for word in formatted:
                    text += word
                text += '\n'
                ostr.write(str(text))

    return True