.PHONY: screencast install-deps

screencast:
	ffmpeg -i screencast.mov -s 400x194 -pix_fmt rgb24 -r 20 -f gif - | gifsicle --optimize=3 --delay=3 > screencast.gif

install-deps:
	brew install ffmpeg gifsicle