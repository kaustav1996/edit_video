from moviepy.editor import *
import sys

args=sys.argv[1:]
input_video_file=args[0]
from_time=int(args[1])
to_time=int(args[2])
caption=args[3]
output_video_file=args[4]
with VideoFileClip(input_video_file) as video_full:
	with video_full.subclip(from_time,to_time) as video:
	# Make the text. Many more options are available.
		txt_clip = ( TextClip(caption,fontsize=50,color='yellow', font="Amiri-Bold",)
			     .set_position('bottom')
			     .set_duration(to_time-from_time) )

		result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
		result.write_videofile(output_video_file,fps=25)
