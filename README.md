# twitter-recorded-space-downloader
This project is a fun project when you want to have twitter recorded space as .wav file.


### Reuqirements:
* python 3
* wget
* ffmpeg
* sox

### Input:
A url to recorded space playlist like:

``...../audio-space/playlist_1234567890.m3u8...``

You can capture it with developer tools in your browser when you press play button for that twitter space.
#### In firefox:
1. Inspect element
2. Network tab
3. search ``playlist``
4. right click Copy -> Copy URL 

### Output:
A .wav file which is more compatible to messanger's client resides on ``data`` folder created in the 
root folder of project.

### Installation
```sudo apt install -y wget ffmpeg sox```

### Run
```python main.py {playlist_url}``` 
