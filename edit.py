from moviepy.editor import *
import sys
import os
from pytube import YouTube 

def download_and_edit(from_time,to_time,caption,link):
	#where to save 
	SAVE_PATH =  os.path.abspath(__file__).replace('edit.py','')+'downloads/' #to_do 
	FINAL_PATH= os.path.abspath(__file__).replace('edit.py','')+'fb_post_queue/'
	#link of the video to be downloaded 
	print(from_time,to_time,caption,link)
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
	stream.download(output_path=SAVE_PATH)

	print('Download Completed!')


	with VideoFileClip(SAVE_PATH+stream.default_filename) as video_full:
		with video_full.subclip(from_time,to_time) as video:
		# Make the text. Many more options are available.
			txt_clip = ( TextClip(caption,fontsize=45,color='yellow', font="Amiri-Bold",)
				     .set_position('bottom')
				     .set_duration(to_time-from_time) )

			result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
			result.write_videofile(FINAL_PATH+stream.default_filename.replace('.mp3','.mp4'),
						threads=4,
						write_logfile=True,
						codec='libx264', 
						audio_codec='aac', 
						temp_audiofile='temp-audio.m4a', 
						remove_temp=True,
						fps=25)
			print('Task COmpleted!!')
