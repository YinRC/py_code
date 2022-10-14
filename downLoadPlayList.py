import os

# --playlist-items 1-3,7
i = 1
dlp = 'yt-dlp --merge-output-format mp4'
ends = '413'
url = 'https://www.youtube.com/playlist?list=PL5I_Ke1KdJcfc7svkx0PczQoPsB39nslR'
item = ''
# print(os.listdir('./'))
for f in os.listdir('./')[1:]:
    print(f)
    if "{:0>3d}".format(i) in f:
        i+=1
        continue
os.system(' '.join((dlp, '--playlist-items '+str(i)+'-'+'413', url)))