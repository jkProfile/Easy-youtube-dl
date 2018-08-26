import subprocess

def media_selection():
    answer = input('Do you want Audio or Video? [A/V]:\n')
    answer = answer.upper()
    if answer == 'A' or answer == 'AUDIO':
        conf_file = 'C:\\python\\youtube-dl\\music.conf'
        return conf_file
    elif answer == 'V' or answer == 'VIDEO':
        conf_file = 'C:\\python\\youtube-dl\\videos.conf'
        return conf_file
    else:
        print(f"Please type A or V:\n")
        return media_selection()

conf_file = media_selection()
# Output dir example:   -o N:/dump-music/%(title)s.%(ext)s
output_dir = input("Where do you want to save the file(s)?:\n")
output_dir = (output_dir.replace('\\', '/') + "/%(title)s.%(ext)s")
url = input("Please paste the url of the video or playlist:\n")
pscp_exec = subprocess.Popen([r"C:\python\youtube-dl\youtube-dl.exe", "--config-location", conf_file, "-o", output_dir, url])
quit()
