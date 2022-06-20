[![header](https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=300&section=header&text=DATAMOSHER%20PRO&fontSize=90&fontAlignY=30&desc=Automated%20Glitching!&descAlign=80&descSize=30&animation=scaleIn)](https://akascape.gumroad.com/l/Datamosher-Pro)
# Datamosher Pro
<b>Datamoshing is a cool video effect and if you want to achieve this glitch with your videos, then you are in the right place!
<br><img align="right" src="https://user-images.githubusercontent.com/89206401/141642297-7c62cf6f-7024-430f-88a2-c9cbbf0dc655.png" width="300">
<br> Datamosher Pro is an automated glitching application for free (python version)! With Datamosher Pro you can quickly and easily datamosh your videos! </b> <br>
### Why I made this?
I was also looking for some good datamoshing software and I found that you have to either use those old softwares like Avidemux or have to look for some paid plugins, so I created my own python based application 'Datamosher Pro'. It contains `30+` different effects which can replicate any type of datamoshing style.
It comes in two version, one paid and one basic free source code version.
# DOWNLOAD
### <p align='center'> Support Datamosher-Pro Development by purchashing its executable version for *windows* on Gumroad which have a modern UI and lots of other features. It will be really helpful!
### <p align='center'> MODERN VERSION (SEE DETAILS)
<br> <p align='center'> [<img src="https://img.shields.io/badge/WINDOWS-DATAMOSHER_PRO-informational?style=for-the-badge&logo=Microsoft&logoColor=blue&color=007ec6" width="500">](https://akascape.gumroad.com/l/Datamosher-Pro)  </br>
<br>
### <p align='center'> FREE BASIC SOURCE CODE VERSIONS
<br> <p align='center'> [<img src="https://img.shields.io/badge/Python_Version-Windows-informational?style=flat&logo=Microsoft&logoColor=blue&color=1bdce3" width=300>](https://github.com/Akascape/Datamosher-Pro/releases/download/Datamosher_Prov1.7/Datamosher_Pro-python_version-win.zip)
<br> <p align='center'> [<img src="https://img.shields.io/badge/Python_Version-MacOS-informational?style=flat&logo=apple&logoColor=b0b5b9&color=b2b7bb" width=300 height=35>](https://github.com/Akascape/Datamosher-Pro/releases/download/Datamosher_Prov1.7/Datamosher_Pro-python_version-mac.zip)
<br> <p align='center'> [<img src="https://img.shields.io/badge/Python_Version-Linux-informational?style=flat&logo=linux&logoColor=black&color=eaea4a" width=300 height=35>](https://github.com/Akascape/Datamosher-Pro/releases/download/Datamosher_Prov1.7/Datamosher_Pro-python_version-linux.zip) <br> Don't forget to give a ⭐ :) </p>

# How to Install?
- For those who are using the python-version,
<br> Download the correct python version (3.10+ recomended) and make sure you have python installed properly. Extract the zip file and open the "datamosher_pro-python_version" folder and just run that Datamosher-Pro.py file. If any module error pops up then just click on yes and the required modules will get downloaded automatically. You can also do that manually if it doesn't work. Then it is ready to use! (No python skills needed)
- For the executable version, just extract the downloaded zip file and run the Datamosher_Pro.exe application.
# How to Use?
For the basic python version:

• Input the video file first (supported formats- mp4, gif, avi, mov, mkv, wmv)
<br>• Choose the desired datamosh mode and the export format (mp4 is recommended)
<br>• Use the advanced options to get more accurate results
<br>• Check/uncheck the highest quality box for quality adjustments
<br>• Then simply click on the datamosh button and wait for a few seconds
<br>• After conversions, your video will be moshed and saved in the same directory

### A documentation will be available in the [Wiki](https://github.com/Akascape/Datamosher-Pro/wiki) page

## Gallery
[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://github.com/Akascape/Datamosher-Pro/blob/Datamosher-Pro-v1.7/Demos.md)
# Effects Info
### Effects List available in the python version:
<br> TIP: Major effects used for datamoshing are Classic, Bloom, Glide, Repeat, Motion Transfer, Rise, Fluid
<br>
| Effect Name     | Description                                                           |
| ----------------| --------------------------------------------------------------------- |
| Rise            | another classic i frames removal effect|
| Shuffle         | randomly shuffles chunks of video frames with the classic ffglitch datamosh (unstable with short videos)|
| Buffer          | creates ring buffers to mosh|
| Delay           | another delaying ffglitch effect|
| Invert-Reverse  | applies both inverse and reverse mode|
| Mirror          | does the mosh with ffglitch but with mirrored X|
| Noise           | makes large noisy mosh|
| Shear           | tilt the video clockwise and merges the mosh|
| Shift           | shifts random blocks of the video upwards|
| Sink            | drowns the next frame of the video in the previous one|
| Slam Zoom       | applies zoom with the sink effect|
| Slice           | randomly zooms and slices the video in parts|
| Stop            | similar to sink but stops the XY values|
| Vibrate         | works as a randomizer|
| Zoom            | simply zooms inside the moshed video|
| Fluid           | this is a ffglitch's average effect which gives a smooth liquid type motion in the video|
| Repeat          | repeats a series of p frames which gives the melting effect|
| Motion Transfer | a powerful ffglitch feature that can transfer the vector motion data from one video to another. Make sure both videos have the same resolution, this effect is also known as style transfer/swap motion.|
| Stretch         | stretches the p-frames horizontally and vertically|
| Glide           | duplicates number of n frames and show it as a flow before reaching the p-frame|
| Sort            | sorts video frames by data size in a rapid movement|
| Echo            | duplicates the single video and apply the mosh effect in the midpoint|
| Shake           | randomly shakes the pixels/blocks throughout the video|
| Classic         | uses the traditional ffmpeg way to convert and corrupt the video by removing the i-frames|
| Random          | randomizes frame order|
| Reverse         | reverses frame order|
| Invert          | switches each consecutive frame witch each other|
| Bloom           | duplicates c times p-frame number n (c=Glitch Size; n=Frame Frequency)|
| Pulse           | duplicates groups of c p-frames every n frames|
| Overlap         | copy group of c frames taken from every nth position|
| Jiggle          | take frame from around current position. n parameter is spread size|
| Void            | gives a clean output but with distortion|
## More effects including these ones are all available in the paid version.
### How to use Advanced Options (Python version)?
The advanced tab is very useful if you want accurate results. The options are:
<br>• `Glitch Size` - tells how long/often to glitch per part (depends on the mode)
<br>• `Frame Frequency` - tells how many frames to apply/repeat in the glitch
<br>• `Ignore Frame` - tells whether to keep the first video frame
<br>• `Kill Frames` - tells max framesize to kill while cleaning (For shuffle/rise mode the kill frame is number of frames that will be deleted)
<br>• `First Frame` - tells the starting frame for the glitch
<br>• `Last Frame` - tells the ending frame for the glitch
<br>• `Start(sec)` - tells the starting time (in seconds) for the glitch
<br>• `End(sec)` - tells the ending time (in seconds) for the glitch
<br>• `Mid Point (Echo mode only)` - tells the point from where the video to repeat(echo)
<br>
<br>NOTE:
<br>- Some modes may not support all the 4 advanced options.
<br>- You can try experimenting with the options but don't put huge values.
<br>- Audio glitching is only available in few modes like classic and repeat.
# UI (BASIC PYTHON VERSION)
| Windows  | Linux   | MacOS   |
| ---------| ------- | ------- |
| ![Windows UI](https://user-images.githubusercontent.com/89206401/142208408-6970448d-fe9d-4e60-aac6-21809aefcfca.png) | ![Linux UI](https://user-images.githubusercontent.com/89206401/168416728-fc9bc8e5-ce34-40c8-9222-bf9986dbb280.png) | ![Mac UI](https://user-images.githubusercontent.com/89206401/168416751-73658dcf-506f-4166-933b-e3f3cb43194c.png) |
# UI (PAID VERSION ONLY WINDOWS)
### This modern UI is available in the paid version only.
![newthemes](https://user-images.githubusercontent.com/89206401/174493211-febc4193-1090-4dbb-8eea-23d7d10e3741.png)
## How It Works?
The main issue with datamoshing is conversion of corrupted files but with Datamosher Pro you can use any video file and it will export an usable datamoshed file. But I still recomend everyone to use MP4 videos. The video is first converted to the required file format using ffmpeg (distributed **externally** with Imageio module) and then the effect is applied and the corrupted file is converted back to stable version using the same process so that the output video can directly be used in other editing softwares. All the unnecessary temp files are removed automatically.
### Read these guides for more details about the python version:
<br> [![Read](https://img.shields.io/badge/Guide-1-orange)](https://akascape.gumroad.com/p/datamosher-pro-guide) [![Read](https://img.shields.io/badge/Guide-2-green)](https://akascape.gumroad.com/p/datamosher-pro-guide-2)
## Conclusion
You will not find this type of software anywhere with so many effects only for datamoshing. This program can be your companion while editing cool glitchy videos :)
<br> As it is a new piece of software some users may find some errors and bugs (specially in the python version), but updates will be on their way.
<br>The effects are all inspired from ItsKaspar's [tomato.py](https://github.com/itsKaspar/tomato), Joe Friedl's [pymosh](https://github.com/grampajoe/pymosh) and [FFglitch](https://ffglitch.org/). 
All the logos and designs are created by me. <br>-Akash Bora
<br>
## License
[<img src="https://user-images.githubusercontent.com/89206401/168461242-884f25ce-eb67-406a-9d98-cf8d0f28cb43.png" width=100>](https://github.com/Akascape/Datamosher-Pro/blob/Datamosher-Pro-v1.7/LICENSE)

Only the python version is licensed under MIT. The executable windows version is different and closed source.
Note that the **FFglitch** part provided in the *releases* is not placed under this license. It is itself an independent program provided without any **modification**. When distributing an application with this package, it must be taken into account that multiple licenses are involved. See the [FFglitch's github page](https://github.com/ramiropolla/ffglitch-core/tree/master) for further details. (That source code is freely available there)
<br>
## Follow me
[<img src="https://img.shields.io/badge/-Github-informational?style=flat&logo=github&logoColor=black&color=grey">](https://github.com/Akascape)
[<img src="https://img.shields.io/badge/-Reddit-informational?style=flat&logo=reddit&logoColor=black&color=orange">](https://www.reddit.com/user/Akascape)
[<img src="https://img.shields.io/badge/-YouTube-informational?style=flat&logo=youtube&logoColor=black&color=red">](https://www.youtube.com/channel/UC7naboenYq9FAo80aPUkqSw)
[<img src="https://img.shields.io/badge/-Twitter-informational?style=flat&logo=twitter&logoColor=black&color=blue">](https://twitter.com/Akascape)
<br> DATAMOSHING MADE EASY!
### Current Version-1.7
<br> [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/Akascape/Datamosher-Pro) [![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://github.com/Akascape/Datamosher-Pro) [![forthebadge](https://forthebadge.com/images/badges/not-a-bug-a-feature.svg)](https://github.com/Akascape/Datamosher-Pro)
[![footer](https://capsule-render.vercel.app/api?type=rect&color=timeGradient&height=2)](https://opensourcelibs.com/lib/capsule-render)
