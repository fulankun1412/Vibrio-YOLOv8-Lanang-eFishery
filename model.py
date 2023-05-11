from ultralytics import YOLO
import cv2
from collections import OrderedDict
import numpy as np
import yaml
import os

os.environ['CLEARML_CONFIG_FILE'] = "clearml.conf"

from clearml import Task, InputModel

with open('config.yaml','r') as f:
    configModel = yaml.safe_load(f)

task = Task.init(project_name='OCR Model-eFishery', task_name='OCR Detection and Text Extraction', task_type="inference")
inputModel = InputModel(project="OCR Model-eFishery", name=configModel["model-config"]["YOLO-model"])
task.connect(inputModel)
pathToModel = inputModel.get_local_copy()

model = YOLO(pathToModel)
imgDelimiter = cv2.imread(configModel["model-config"]["delimiter"])
gcv_api_key_path = configModel["model-config"]["vision-key"]
imgSize = configModel["model-config"]["image-size"]

def extractValue(img):
    scalingH, scalingW = img.shape[0]/imgSize, img.shape[1]/imgSize
    data = cv2.resize(img, (imgSize, imgSize))

    results = model.predict(data, imgsz = imgSize,
                            conf = configModel["model-config"]["conf"], iou = configModel["model-config"]["iou"],
                            save = configModel["model-config"]["save-mode"], save_conf = configModel["model-config"]["save-mode"],
                            save_crop = configModel["model-config"]["save-mode"], save_txt = configModel["model-config"]["save-mode"],
                            device = configModel["model-config"]["device-mode"])
    
    classes = results[0].names

    totalFound = {}
    for boxes in results[0].boxes:
        for box in boxes:
            if int(box.cls) in totalFound.keys():
                totalFound[int(box.cls)] = totalFound[int(box.cls)] + 1
            else:
                totalFound[int(box.cls)] = 1

    finalDict = {}
    orderedDict = OrderedDict(sorted(totalFound.items()))
    for key, value in orderedDict.items():
        for classKey, classValue in classes.items(): 
            if key == classKey:
                finalDict[classValue] = value
    
    for label in classes.values():
        if label not in finalDict.keys():
            finalDict[label] = "0"
    
    return results[0].plot(), finalDict