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
#     ord('??'):'a',
#     ord('??'):'b',
#     ord('??'):'v',
#     ord('??'):'g',
#     ord('??'):'d',
#     ord('??'):'e',
#     ord('??'):'yo',
#     ord('??'):'zh',
#     ord('??'):'z',
#     ord('??'):'i',
#     ord('??'):'y',
#     ord('??'):'k',
#     ord('??'):'l',
#     ord('??'):'m',
#     ord('??'):'n',
#     ord('??'):'o',
#     ord('??'):'p',
#     ord('??'):'r',
#     ord('??'):'s',
#     ord('??'):'t',
#     ord('??'):'u',
#     ord('??'):'f',
#     ord('??'):'h',
#     ord('??'):'c',
#     ord('??'):'ch',
#     ord('??'):'sh',
#     ord('??'):'shch',
#     ord('??'):'y',
#     ord('??'):'y',
#     ord('??'):"'",
#     ord('??'):'e',
#     ord('??'):'yu',
#     ord('??'):'ya',

#     ord('??'):'A',
#     ord('??'):'B',
#     ord('??'):'V',
#     ord('??'):'G',
#     ord('??'):'D',
#     ord('??'):'E',
#     ord('??'):'Yo',
#     ord('??'):'Zh',
#     ord('??'):'Z',
#     ord('??'):'I',
#     ord('??'):'Y',
#     ord('??'):'K',
#     ord('??'):'L',
#     ord('??'):'M',
#     ord('??'):'N',
#     ord('??'):'O',
#     ord('??'):'P',
#     ord('??'):'R',
#     ord('??'):'S',
#     ord('??'):'T',
#     ord('??'):'U',
#     ord('??'):'F',
#     ord('??'):'H',
#     ord('??'):'Ts',
#     ord('??'):'Ch',
#     ord('??'):'Sh',
#     ord('??'):'Shch',
#     ord('??'):'Y',
#     ord('??'):'Y',
#     ord('??'):"'",
#     ord('??'):'E',
#     ord('??'):'Yu',
#     ord('??'):'Ya',
#     }

def normalize(string: str) -> str:
    """
    normalize - is a function that converts Cyrillic
    characters to Latin characters
    param : the string you need normalize
    return : normalize string
    """
    # dict with transliteral letters

    trans_dict = {ord('??'): 'a', ord('??'): 'b', ord('??'): 'v', ord('??'): 'g',
                  ord('??'): 'd', ord('??'): 'e', ord('??'): 'ye', ord('??'): 'zh',
                  ord('??'): 'z', ord('??'): 'y', ord('??'): 'i', ord('??'): 'yi',
                  ord('??'): 'y', ord('??'): 'k', ord('??'): 'l', ord('??'): 'm',
                  ord('??'): 'n', ord('??'): 'o', ord('??'): 'p', ord('??'): 'r',
                  ord('??'): 's', ord('??'): 't', ord('??'): 'u', ord('??'): 'f',
                  ord('??'): 'kh', ord('??'): 'ts', ord('??'): 'ch', ord('??'): 'sh',
                  ord('??'): 'shch', ord('??'): 'yu', ord('??'): 'ya', ord('??'): 'y',
                  ord('??'): 'e', ord('??'): 'yo', ord('??'): 'A', ord('??'): 'B',
                  ord('??'): 'V', ord('??'): 'G', ord('??'): 'D', ord('??'): 'E',
                  ord('??'): 'Ye', ord('??'): 'Zh', ord('??'): 'Z', ord('??'): 'Y',
                  ord('??'): 'I', ord('??'): 'Yi', ord('??'): 'Y', ord('??'): 'K',
                  ord('??'): 'L', ord('??'): 'M', ord('??'): 'N', ord('??'): 'O',
                  ord('??'): 'P', ord('??'): 'R', ord('??'): 'S', ord('??'): 'T',
                  ord('??'): 'U', ord('??'): 'F', ord('??'): 'Kh', ord('??'): 'Ts',
                  ord('??'): 'Ch', ord('??'): 'Sh', ord('??'): 'Shch', ord('??'): 'Yu',
                  ord('??'): 'Ya', ord('??'): 'Y', ord('??'): 'E', ord('??'): 'Yo'}

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
