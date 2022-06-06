
import time
from pytube import Playlist
from moviepy.editor import *
import os
import shutil
import socket
hostname=socket.gethostname()
ip=socket.gethostbyname(hostname)

def videodownload(playlistLink):
    current_count = 0
    if playlistLink.__contains__("https://www.youtube.com/playlist?list="):    
        playlist = Playlist(playlistLink)
        if len(playlist.video_urls) == 0:
            print("Please enter a valid link")
            videodownload()
        CHECK_FOLDER = os.path.isdir("./Videos")
        if not CHECK_FOLDER:
            os.mkdir("./Videos")


        download= "./Videos/"
        ttl = playlist.title
        download_folder =  download +hostname+"_"+ip+"_"+ttl
        CHECK_FOLDER = os.path.isdir(download_folder)

        if not CHECK_FOLDER:
            os.mkdir(download_folder)
            print("Videos will be downloaded to  ", download_folder)

        else:
            print(download_folder, " Already exist!")
            print("Try Again")
            time.sleep(1)
            videodownload()

        print("Total Video Count: ", len(playlist.video_urls))    

        print("\n\n Youtube Videos Link \n")

        for url in playlist.video_urls:
            print(url)
        
        for video in playlist.videos:
            print('Downloading : {} with url : {}'.format(video.title, video.watch_url))
            video.streams.\
                filter(type='video', progressive=True, file_extension='mp4').\
                order_by('resolution').\
                desc().\
                first().\
                download(download_folder)
            current_count += 1
        print("Process Completed. Videos Downloaded To"+download_folder)
        shutil.make_archive(ttl, 'zip', download_folder)
        for f in os.listdir(download_folder):
            os.remove(os.path.join(download_folder, f))
        shutil.move(ttl+".zip", download_folder)        
        
        time.sleep(1)
    else:
        print("Please enter a valid link")
        videodownload()

    


def audiodownload(playlistLink):
    if playlistLink.__contains__("https://www.youtube.com/playlist?list="):   
        playlist = Playlist(playlistLink)
        if len(playlist.video_urls) == 0:
            print("Please enter a valid link")
            audiodownload()
        CHECK_FOLDER = os.path.isdir("./Songs")
        if not CHECK_FOLDER:
            os.mkdir("./Songs")
        
        download = "./Songs/"
        ttl = playlist.title
        download_folder =  download +hostname+"_"+ip+"_"+ttl
        CHECK_FOLDER = os.path.isdir(download_folder)

        if not CHECK_FOLDER:
            os.mkdir(download_folder)
            print("Videos will be downloaded to ", download_folder)

        else:
            print(download_folder, " Already exist!")
            print("Try Again")
            time.sleep(1)
            audiodownload()

        print("Total Video Count: ", len(playlist.video_urls))    

        print("\n\n Youtube Songs Link\n")

        for url in playlist.video_urls:
            print(url)

        for video in playlist.videos:
            print('Downloading : {} with url : {}'.format(video.title, video.watch_url))
            audio = video.streams.filter(only_audio=True).first()
            audio.download(download_folder)
        for filename in os.listdir(download_folder):
                infilename = os.path.join(download_folder,filename)
                if not os.path.isfile(infilename): continue
                oldbase = os.path.splitext(filename)
                newname = infilename.replace('.mp4', '.mp3')
                output = os.rename(infilename, newname)
                
        print("Process Completed. Videos Downloaded To"+download_folder)

        shutil.make_archive(ttl, 'zip', download_folder)


        for f in os.listdir(download_folder):
            os.remove(os.path.join(download_folder, f))
        shutil.move(ttl+".zip", download_folder)
            

            
        time.sleep(1)
        return("nothing")
        
    else:
        print("Please enter a valid link")
        audiodownload()