from django.shortcuts import render


import numpy as np
import joblib

model=joblib.load('./Enery_pred_finalmodel.sav')

# Create your views here.
def home(request):
    return render(request,"index.html")
def reg(request):
    if request.method=='POST':
        Lagging_Current_Reactive_Power_kVarh =request.POST.get('Lagging_Current_Reactive_Power_kVarh')
        #print(age)
        Leading_Current_Reactive_Power_kVarh=request.POST.get('Leading_Current_Reactive_Power_kVarh')
        #print(sex)
        Lagging_Current_Power_Factor=request.POST.get('Lagging_Current_Power_Factor')
        #print(bmi)
        Leading_Current_Power_Factor=request.POST.get('Leading_Current_Power_Factor')
        #print(children)
        NSM=request.POST.get('NSM')
    result=model.predict([[Lagging_Current_Reactive_Power_kVarh,Leading_Current_Reactive_Power_kVarh,Lagging_Current_Power_Factor,Leading_Current_Power_Factor,NSM]])
    pred={'predition':int(result)}

    return render(request,"register.html",pred)
