import cv2
cap = cv2.VideoCapture(0)

ret1, frame1 = cap.read()
ret2, frame2 = cap.read()

while True:
    frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    frame1_blur = cv2.GaussianBlur(frame1_gray, (21,21), 0)
    frame2_blur = cv2.GaussianBlur(frame2_gray, (21,21), 0)

    diff = cv2.absdiff(frame1_blur, frame2_blur)

    thresh = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)[1]
    final = cv2.dilate(thresh, None, iterations=2)

    cv2.imshow("Motion", final)
    frame1 = frame2
    ret, frame2 = cap.read()
    if not ret:
        break

    k = cv2.waitKey(10)
    if k == ord('q'):
        break
cv2.destroyAllWindows()


       