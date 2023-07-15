import cv2

#Initialize the video capture object

video = cv2.VideoCapture(0)
#Read the first frame

ret ,frame =video.read(1)

#Or insert the image
#img=cv2.imread('img2.png')


#Creating a tracker object
tracker = cv2.TrackerKCF_create()

#Select the region of interest (ROI) for tracking
bbox =cv2.selectROI("Object Tracking ",frame,False)


#bbox =cv2.selectROI("Object Tracking ",img,False)

#Initialize the tracker with the first frame and ROI
tracker.init(frame,bbox)
#tracker.init(img,bbox)

while True:
    #Read a new frame
    ret , frame =video.read()

    #Update the tracker
    success, bbox =tracker.update(frame)
    #If tracking is successful ,draw the bounding box around the object
    if success:
        x ,y,w,h =[int(v) for v in bbox]
        cv2.rectangle(frame , (x,y), (x+w , y+h),(0,255,0),2)
        cv2.putText(frame, "Tracking", (75, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)

        #gt_bbox=(x,y,x+w,y+h)
    else:
        cv2.putText(frame, "Lost", (75, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)

    #Display the Frame
    cv2.imshow("Object Tracking",frame)

    #Exit Loop  if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Release the video capture object
video.release()

#Close all windows
cv2.destroyAllWindows()