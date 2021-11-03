import pyautogui
import cv2
import numpy as np
import time as t


###########################################################################

#         ----------- Screen Recording Program -----------

###########################################################################



def screen_recording(video_name):          # Function contains one paramater

    screen_size = pyautogui.size()    # Size of Screen


    video_write = cv2.VideoWriter(video_name +".avi",cv2.VideoWriter_fourcc(*"MJPG"),18,screen_size)    # We create the object on which we will write the video.


    print("Recording...")
    t.sleep(0.2)
    print("...")
    t.sleep(0.2)
    print("..")
    t.sleep(0.2)
    print(".")


    while True:

        screen_shot_image = pyautogui.screenshot()
        frame = np.array(screen_shot_image)

        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)   # Converting BGR to RGB format

        video_write.write(frame)                  # Every video frame is recorded.


        cv2.imshow("Recording Screen",frame)     # Showing recording screen


        if cv2.waitKey(1) == ord("q"):                 # Press "q" to close recording screen

            break

    cv2.destroyAllWindows()
    video_write.release()





screen_recording("FirstRecording")     # The function takes only the video name as a parameter.



