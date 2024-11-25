from django.shortcuts import render
from .forms import CementInput
from django.http import JsonResponse
import pickle
import os
import numpy as np
import pandas as pd

# Create your views here.

def home(request):
    if request.method == 'POST':
        form_data = request.POST
        data={}
        for key,val in dict(form_data).items():
            if key!="csrfmiddlewaretoken":
                data[key]=float(val[0])

        # print(data)
        if not data:
            return JsonResponse({'error': 'No data provided'})
        
        app_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the absolute file path to the pickle file
        scaler_file = os.path.join(app_dir, 'scaler.pkl')
        model_file = os.path.join(app_dir, 'prediction.pkl')
        
        # Load the pickled object from the file
       

        try:
            with open(model_file,'rb') as g:
                model=pickle.load(g)
            with open(scaler_file,'rb') as f:
                scaler = pickle.load(f)

        except Exception as e:
            print(e)
            return JsonResponse({'error': 'Error loading model files'})
        
        # Extract values from the POST data
        data_values = [float(val) for val in data.values()]

        # Assuming data_values correspond to the features in the same order
        data_scaled = scaler.transform([np.array(data_values)])
        prediction = model.predict(data_scaled)
    
        return render(request, 'core/result.html', {'pred': prediction[0]})
    else:
        fm = CementInput()
        return render(request, 'core/index.html', {'form': fm})
