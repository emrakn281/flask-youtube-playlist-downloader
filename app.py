from argparse import FileType
from importlib.resources import path
from itertools import count
from tabnanny import check
from telnetlib import TTYLOC
from turtle import title
from flask import Flask, render_template,Response, request, redirect, url_for, flash, jsonify,send_file
import pl_dwn
from pytube import Playlist
import time
import socket
hostname=socket.gethostname()
ip=socket.gethostbyname(hostname)


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "POST":
        playlist = request.form.get("yt_link")
        if request.form.get("yt_link").__contains__("https://www.youtube.com/playlist?list=")==False:
            return render_template("index.html",color="red",errorTitle="Invalid Playlist l-Link",status="fail",icon="fa fa-warning", buttonText="Try Again",buttonLink="/")
        elif isempty(playlist) is None:
            print("Empty playlist")
            return render_template("index.html",color="red",errorTitle="Empty Playlist",status="fail",icon="fa fa-warning",buttonText="Try Again" ,buttonLink="/")
        else:
            if request.form.get("format") != "select":
                convert(playlist)
                return render_template("index.html",color="green",errorTitle="Playlist Converted Successfully",status="success",icon="fa fa-check",buttonText="Download",buttonLink="/download")
            else:
                return render_template("index.html",color="blue",errorTitle="Please Select a Format",status="fail",icon="fa fa-warning",buttonText="Try Again",buttonLink="#")
    else:
        return render_template("index.html",errorTitle="")


def isempty(playlist_link):
    try:
        pl = Playlist(playlist_link)
        return len(pl.video_urls)
    except:
        return None

def convert(playlist):
    pl = Playlist(playlist)
    global ttl
    global fileType
    ttl = pl.title
    if request.form['format'] == 'mp4':
        fileType = './Videos/'
        pl_dwn.videodownload(playlist)
    if request.form['format'] == 'mp3':
        fileType = './Songs/'
        pl_dwn.audiodownload(playlist)


@app.route('/download', methods=['GET', 'POST'])
def download_file():

    path=fileType+hostname+"_"+ip+"_"+ttl+"/"+ttl+".zip"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
    
