import webbrowser
import time

t_breaks=5
breaks_taken=0

while(breaks_taken < t_breaks):
    print("Current time:" + time.ctime())
    time.sleep(5)
    webbrowser.open_new("https://facebook.com")
    breaks_taken=breaks_taken+1