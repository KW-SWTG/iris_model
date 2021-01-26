from django.shortcuts import render
from django.shortcuts import redirect
from .apps import ModelConfig
import numpy as np
import pickle
# Create your views here.

def home(request):
    return render(request, "main.html")


def Prediction(x, y, z, a):
    result=""
    model=ModelConfig.models.predict(np.array([[x, y, z, a]]))

    if model[0]==1:
        result = "setosa"
    elif model[0]==2:
        result = "virginicpa"
    else:
        result = "nothing"
    return result

def model(request):
    x = int(request.GET['x'])
    y = int(request.GET['y'])
    z = int(request.GET['z'])
    a = int(request.GET['a'])

    result = Prediction(x, y, z, a)
    return render(request, 'result.html', {'result': result})




