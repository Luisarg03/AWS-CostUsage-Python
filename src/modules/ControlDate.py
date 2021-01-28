import datetime
import os

def controltime():
    '''Crea/lee el archivo que contiene la hora
     de la ultima fecha ingestada'''

    path = '../ControlDownload/'

    if not os.path.exists(path):
        os.makedirs(path)

        file_time = open(path + 'UltimaHora.txt', 'a+')

        start = datetime.datetime.now()
        start = start.strftime("%Y-%m-%d")

        file_time.write(start+'\n')
        file_time.close()

    else:
        pass

    try:
        with open(path + 'UltimaHora.txt', 'r') as file:
            for start in file:
                pass

    except FileNotFoundError:
        file_time = open(path + 'UltimaHora.txt', 'a+')

        start = datetime.datetime.now()
        start = start.strftime("%Y-%m-%d")

        file_time.write(start+'\n')
        file_time.close()
    
    start = datetime.datetime.strptime(start.strip(), "%Y-%m-%d")
    end = start + datetime.timedelta(days=1)

    start = start.strftime("%Y-%m-%d")
    end = end.strftime("%Y-%m-%d")

    with open(path + 'UltimaHora.txt', 'a+') as f:
        f.write(end+'\n')

    time_dict = {'start': start,
                 'end': end, }

    return time_dict