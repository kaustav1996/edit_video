from moviepy.editor import *
import sys
import os

args=sys.argv[1:]
input_video_file=args[0]
from_time=int(args[1])
to_time=int(args[2])
caption=args[3]
output_video_file=args[4]
file_url=args[5]

#importing the module 
from pytube import YouTube 
  
#where to save 
SAVE_PATH =  output_video_file.replace(input_video_file,'') #to_do 
  
#link of the video to be downloaded 
link=file_url
  
try: 
    #object creation using YouTube which was imported in the beginning 
    yt = YouTube(link) 
except: 
    print("Connection Error") #to handle exception 
  
#filters out all the files with "mp4" extension 
#mp4files = yt.filter('mp4') 
  
#yt.set_filename(input_video_file) #to set the name of the file 
  
#get the video with the extension and resolution passed in the get() function 
stream = yt.streams.first()
stream.download(SAVE_PATH)
os.rename(SAVE_PATH+"'"+yt.title+".mp4'",SAVE_PATH+input_video_file)

print('Task Completed!')


with VideoFileClip(output_video_file) as video_full:
	with video_full.subclip(from_time,to_time) as video:
	# Make the text. Many more options are available.
		txt_clip = ( TextClip(caption,fontsize=50,color='yellow', font="Amiri-Bold",)
			     .set_position('bottom')
			     .set_duration(to_time-from_time) )

		result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
		result.write_videofile(output_video_file,fps=25)
