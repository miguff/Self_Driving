import cv2

cam = cv2.VideoCapture(0)

while True:
    ignore, frame = cam.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(frame, (5,5), 0)
    edges = cv2.Canny(blur, 100, 200)
    ret, thresh = cv2.threshold(edges, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        M = cv2.moments(c)
        try:
            cX = int(M["m10"] / M["m00"])
            cY = int(M['m01'] / M["m00"])
            cv2.circle(frame, (cX, cY), 1, (255, 255, 255), -1)
        except:
            continue

    cv2.imshow("Teszt", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()