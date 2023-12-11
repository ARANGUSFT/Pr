from django.shortcuts import render
import cv2
import face_recognition

def reconocimiento_facial(request):
    # Capturar imagen desde la cámara
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    # Guardar la imagen capturada
    cv2.imwrite('imagen_capturada.jpg', frame)
    cap.release()

    # Cargar la imagen para el reconocimiento facial
    imagen_usuario = face_recognition.load_image_file('imagen_capturada.jpg')

    # Realizar el reconocimiento facial
    # (Agrega aquí la lógica de comparación con tus usuarios registrados)

    # Muestra el resultado en la plantilla
    return render(request, 'reconocimiento/reconocimiento_facial.html')
