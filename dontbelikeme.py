# -*- coding: utf-8 -*-
import glob
from ntpath import join
import os
import pathlib
import shutil
from sys import argv
from os import path, rmdir

folder = []
home_dir = pathlib.Path.home()
name, path_dir = argv

images = ['.jpeg','.png','.jpg','.svg']
video = ['.avi','.mp4','.mov','.mkv']
documents = ['.doc','.docx','.txt','.pdf','.xlsx','.pptx']
music = ['.mp3','.ogg','.wav','.amr']
archives = ['.zip','.gz','.tar','.rar']

img_location = ('images')
vid_location = ('videos')
doc_location = ('documents')
mus_location = ('audio')
arc_location = ('archives')

location_dirs = [img_location, vid_location, doc_location, mus_location, arc_location]

def del_empty_dirs(path):
    for dir in os.listdir(path):
        if os.path.isdir(os.path.join(path_dir, dir)):
            inner_dir = os.listdir(os.path.join(path_dir, dir))
            if not len(inner_dir):
                os.rmdir(os.path.join(path_dir, dir))
        

def make_dirs(location):
    if not os.path.isdir(os.path.join(path_dir, location)):
        os.makedirs(os.path.join(path_dir, location))

def move_files(pa):
    # filename = glob.glob(pa)
    # for files in filename:
    #    os.rename(files, normalize(files))

    # filename = glob.glob(pa)
    
    file = os.path.split(pa)[1]
    
    file_name, file_ext = os.path.splitext(file)
    
    new_file_name = normalize(file_name)
    
    new_file = new_file_name + file_ext
        
    if file_ext in images:
        # if(path.exists(img_location)):
        os.replace(pa, os.path.join(path_dir, img_location, new_file))
        return file_ext
        # else:
        #     os.makedirs(img_location)
        #     shutil.move(file,img_location)
    if file_ext in video:
        # if(path.exists(vid_location)):
        os.replace(pa, os.path.join(path_dir, vid_location, new_file))
        return file_ext
        # else:
            # os.makedirs(vid_location)
            # shutil.move(file,vid_location)
    if file_ext in documents:
        # if(path.exists(doc_location)):
        os.replace(pa, os.path.join(path_dir, doc_location, new_file))
        return file_ext
        # else:
            # os.makedirs(doc_location)
            # shutil.move(file,doc_location)
    if file_ext in music:
        # if(path.exists(mus_location)):
        os.replace(pa, os.path.join(path_dir, mus_location, new_file))
        return file_ext
        # else:
            # os.makedirs(mus_location)
            # shutil.move(file,mus_location)
    if file_ext in archives:
        # if(path.exists(arc_location)):
        os.replace(pa, os.path.join(path_dir, arc_location, new_file))
        shutil.unpack_archive(os.path.join(path_dir, arc_location, new_file), os.path.join(path_dir, arc_location, new_file_name))
        return file_ext
            # shutil.move(file, arc_location)
        # else:
            # os.makedirs(arc_location)
            # shutil.unpack_archive(file,'./archives/' + os.path.splitext(os.path.basename(file))[0] + '/')
            # shutil.move(file, arc_location)
    else:
        os.replace(pa, os.path.join(path_dir, new_file))
        return file_ext
# def normalize (some_string, dic):
#     n_string = some_string.translate(dic)
#     return n_string

# legend = {
#     '~':'_',
#     '@':'_',
#     '#':'_',
#     '$':'_',
#     '%':'_',
#     '^':'_',
#     '-':'_',
#     ' ':'_',
#     '(':'_',
#     ')':'_',
#     '{':'_',
#     '}':'_',
#     ',':'',
#     ord('а'):'a',
#     ord('б'):'b',
#     ord('в'):'v',
#     ord('г'):'g',
#     ord('д'):'d',
#     ord('е'):'e',
#     ord('ё'):'yo',
#     ord('ж'):'zh',
#     ord('з'):'z',
#     ord('и'):'i',
#     ord('й'):'y',
#     ord('к'):'k',
#     ord('л'):'l',
#     ord('м'):'m',
#     ord('н'):'n',
#     ord('о'):'o',
#     ord('п'):'p',
#     ord('р'):'r',
#     ord('с'):'s',
#     ord('т'):'t',
#     ord('у'):'u',
#     ord('ф'):'f',
#     ord('х'):'h',
#     ord('ц'):'c',
#     ord('ч'):'ch',
#     ord('ш'):'sh',
#     ord('щ'):'shch',
#     ord('ъ'):'y',
#     ord('ы'):'y',
#     ord('ь'):"'",
#     ord('э'):'e',
#     ord('ю'):'yu',
#     ord('я'):'ya',

#     ord('А'):'A',
#     ord('Б'):'B',
#     ord('В'):'V',
#     ord('Г'):'G',
#     ord('Д'):'D',
#     ord('Е'):'E',
#     ord('Ё'):'Yo',
#     ord('Ж'):'Zh',
#     ord('З'):'Z',
#     ord('И'):'I',
#     ord('Й'):'Y',
#     ord('К'):'K',
#     ord('Л'):'L',
#     ord('М'):'M',
#     ord('Н'):'N',
#     ord('О'):'O',
#     ord('П'):'P',
#     ord('Р'):'R',
#     ord('С'):'S',
#     ord('Т'):'T',
#     ord('У'):'U',
#     ord('Ф'):'F',
#     ord('Х'):'H',
#     ord('Ц'):'Ts',
#     ord('Ч'):'Ch',
#     ord('Ш'):'Sh',
#     ord('Щ'):'Shch',
#     ord('Ъ'):'Y',
#     ord('Ы'):'Y',
#     ord('Ь'):"'",
#     ord('Э'):'E',
#     ord('Ю'):'Yu',
#     ord('Я'):'Ya',
#     }

def normalize(string: str) -> str:
    """
    normalize - is a function that converts Cyrillic
    characters to Latin characters
    param : the string you need normalize
    return : normalize string
    """
    # dict with transliteral letters

    trans_dict = {ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g',
                  ord('д'): 'd', ord('е'): 'e', ord('є'): 'ye', ord('ж'): 'zh',
                  ord('з'): 'z', ord('и'): 'y', ord('і'): 'i', ord('ї'): 'yi',
                  ord('й'): 'y', ord('к'): 'k', ord('л'): 'l', ord('м'): 'm',
                  ord('н'): 'n', ord('о'): 'o', ord('п'): 'p', ord('р'): 'r',
                  ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f',
                  ord('х'): 'kh', ord('ц'): 'ts', ord('ч'): 'ch', ord('ш'): 'sh',
                  ord('щ'): 'shch', ord('ю'): 'yu', ord('я'): 'ya', ord('ы'): 'y',
                  ord('э'): 'e', ord('ё'): 'yo', ord('А'): 'A', ord('Б'): 'B',
                  ord('В'): 'V', ord('Г'): 'G', ord('Д'): 'D', ord('Е'): 'E',
                  ord('Є'): 'Ye', ord('Ж'): 'Zh', ord('З'): 'Z', ord('И'): 'Y',
                  ord('І'): 'I', ord('Ї'): 'Yi', ord('Й'): 'Y', ord('К'): 'K',
                  ord('Л'): 'L', ord('М'): 'M', ord('Н'): 'N', ord('О'): 'O',
                  ord('П'): 'P', ord('Р'): 'R', ord('С'): 'S', ord('Т'): 'T',
                  ord('У'): 'U', ord('Ф'): 'F', ord('Х'): 'Kh', ord('Ц'): 'Ts',
                  ord('Ч'): 'Ch', ord('Ш'): 'Sh', ord('Щ'): 'Shch', ord('Ю'): 'Yu',
                  ord('Я'): 'Ya', ord('Ы'): 'Y', ord('Э'): 'E', ord('Ё'): 'Yo'}

    stringN = []
    # # main part of function
    for c in string:
        if not c.isalpha() and not c.isdigit():
            c = '_'
            stringN.append(c)
        else:
            c = c.translate(trans_dict)
            stringN.append(c)
    return ''.join(stringN)


for locations in location_dirs:
    make_dirs(locations)

for i in os.walk(path_dir):
    folder.append(i)
    
for address, dirs, files in folder:
    for file in files:
        x = os.path.join(address,file)
        move_files(x)
        
del_empty_dirs(path_dir)
