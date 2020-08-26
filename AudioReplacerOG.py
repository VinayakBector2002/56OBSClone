#Replacing Audio
source = vedit.Video( "./examples/i010.mp4" )
output_file = "./example_output/example04.mp4"
# Get a clip, but override any Window settings for its audio.
clip = vedit.Clip( video=source, display=vedit.Display( include_audio=False ) )
# Give this window it's own audio track, and set the duration to
# 10 seconds (otherwise it will go on as long as the audio track).
#
# Note - if the window audio track is longer than the video
# content, it fades out starting 5 seconds from the end.
window = vedit.Window( audio_file="./examples/a2.mp4", duration=10,
                       output_file=output_file )
window.clips = [ clip ]
window.render()
log.info( "Replaced audio in output: %s" % ( output_file ) )

# Let's make a version where we attribute the audio with some text.
song_attribution = '''This video features the song:
Chuckie Vs Hardwell Vs Sandro Silva Vs Cedric & Quintino
EPIC CLARITY JUMP- (NC MASHUP) LIVE
By: NICOLE CHEN
Available under under a Creative Commons License:
http://creativecommons.org/licenses/by/3.0/ license'''

output_file = "./example_output/example04-attributed.mp4"
window = vedit.Window( audio_file="./examples/a2.mp4",
                       audio_desc=song_attribution,
                       duration=10,
                       output_file=output_file )
window.clips = [ clip ]
window.render()
log.info( "Replaced audio in output: %s" % ( output_file ) )
