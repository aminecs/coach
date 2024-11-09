import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2

from IPython.display import display, Image, Audio
import base64
from openai import OpenAI
import os
import cv2
import numpy as np
import json
import voice

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def draw_landmarks_on_image(rgb_image, detection_result):
  face_landmarks_list = detection_result.face_landmarks
  annotated_image = np.copy(rgb_image)

  # Loop through the detected faces to visualize.
  for idx in range(len(face_landmarks_list)):
    face_landmarks = face_landmarks_list[idx]

    # Draw the face landmarks.
    face_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    face_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in face_landmarks
    ])

    solutions.drawing_utils.draw_landmarks(
        image=annotated_image,
        landmark_list=face_landmarks_proto,
        connections=mp.solutions.face_mesh.FACEMESH_TESSELATION,
        landmark_drawing_spec=None,
        connection_drawing_spec=mp.solutions.drawing_styles
        .get_default_face_mesh_tesselation_style())
    solutions.drawing_utils.draw_landmarks(
        image=annotated_image,
        landmark_list=face_landmarks_proto,
        connections=mp.solutions.face_mesh.FACEMESH_CONTOURS,
        landmark_drawing_spec=None,
        connection_drawing_spec=mp.solutions.drawing_styles
        .get_default_face_mesh_contours_style())
    solutions.drawing_utils.draw_landmarks(
        image=annotated_image,
        landmark_list=face_landmarks_proto,
        connections=mp.solutions.face_mesh.FACEMESH_IRISES,
          landmark_drawing_spec=None,
          connection_drawing_spec=mp.solutions.drawing_styles
          .get_default_face_mesh_iris_connections_style())

  return annotated_image

def get_feed():

    base_options = python.BaseOptions(model_asset_path='face_landmarker.task') # This file needs to be downloaded from mediapipe

    options = vision.FaceLandmarkerOptions(base_options=base_options,
                                        output_face_blendshapes=True,
                                        output_facial_transformation_matrixes=True,
                                        num_faces=1)
    detector = vision.FaceLandmarker.create_from_options(options)
    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()

        if not ret:
            print("Error: failed to capture image")
            break
        
        #image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        detection_result = detector.detect(image)
        annotated_image = draw_landmarks_on_image(image.numpy_view(), detection_result)
        cv2.imshow('annotated_image', annotated_image)

        if cv2.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Open AI solution

def get_llm_emotions_classification():
    print("Getting LLM emotions classification")
    cap = cv2.VideoCapture(0)
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    frame_count = 3
    while(True):
        ret, frame = cap.read()

        if not ret:
            print("Error: failed to capture image")
            break
        else:
            frame_count += 1

            if frame_count % (fps * 5) == 0:
                # Call LLM
                print("Calling LLM")
                #pause_event.clear()
                response = llm_call(frame)
                #pause_event.set()
                print(response)
                # optional 
                frame_count = 0

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def llm_call(frame):
    _, buffer = cv2.imencode(".jpg", frame)
    base64_img = base64.b64encode(buffer).decode("utf-8")

    PROMPT_MESSAGES = [
    {
        "role": "user",
        "content": [
            """
            You are an AI coach for runners. You motivate them David Goggins style. Look at the image for the current state of the runner. 
            If they are happy or neutral, return a sentence that approves their attitude in the tone of David Goggins. 
            If they are any other emotion, return a sentence that motivates them to be push themselves in the tone of David Goggins.
            If their tongue is out, this indicates that their pace is too slow, get them to speed up in the tone of David Goggins.
            """,
            {"image": base64_img, "resize": 768},
        ],
    },
    ]
    params = {
        "model": "gpt-4-turbo",
        "messages": PROMPT_MESSAGES,
        "max_tokens": 200
        #"response_format":{ "type": "json_object"}
    }


    result = client.chat.completions.create(**params)
    voice.speak(result.choices[0].message.content)
    # emotion = json.loads(result.choices[0].message.content)["emotion"]
    # return emotion