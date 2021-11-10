import os
import io

from google.cloud import vision

list_of_objects=[]

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'careful-rock-306004-28c6024b49ee.json'

client = vision.ImageAnnotatorClient()

for x in range(1,8):
    num = str(x)
    file_name = os.path.abspath('./static/'+num+'.png')

    # Loads the image to memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations

    for object_ in objects:
        list_of_objects.append(object_.name)
