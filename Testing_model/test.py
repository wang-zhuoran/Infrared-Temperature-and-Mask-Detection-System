new_model = tf.keras.models.load_model('my_first_model.h5')

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
while 1:
    # get a frame
    ret, frame = cap.read()
    # show a frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.1, 4)

    for x, y, w, h in faces:
      roi_gray = gray[y:y + h, x:x + h]
      roi_color = frame[y:y + h, x:x + h]
      # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
      faces = faceCascade.detectMultiScale(roi_gray)
      for (ex, ey, ew, eh) in faces:
          face_roi = roi_color[ey:ey + eh, ex:ex + eh]
          final_image = cv2.resize(face_roi, (224, 224))
          final_image = final_image.reshape(-1, 224, 224, 3)  # return the image with shaping that TF wants.

          fianl_image = np.expand_dims(final_image, axis=0)  # need forth dimension

          final_image = final_image / 225.0

          Predictions = new_model.predict(final_image)
          print(Predictions)
          if (Predictions > 0.5):
              cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
              cv2.putText(frame, 'Wearing Mask!', (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)
              # cv2.putText(img, str,origin,font,size,color,thickness)
          else:
              cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
              cv2.putText(frame, 'No Mask!', (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

          # if(Predictions<0.45):
          #   print("No mask")
          # elif(Predictions>0.55):
          #   print("With mask")
          # else:
          #   print("Can not determine")

      cv2.imshow("capture", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
