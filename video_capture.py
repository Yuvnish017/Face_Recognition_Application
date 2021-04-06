import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
fourcc = cv2.VideoWriter_fourcc(*"XVID")
writer = cv2.VideoWriter('video.avi', fourcc, 30, (frame.shape[1], frame.shape[0]), True)

while True:
    ret, frame = cap.read()
    if not ret:
        cap.release()
        break
    writer.write(frame)
    k = cv2.waitKey(1)
    if k == 27:
        cap.release()
        break

cv2.destroyAllWindows()
