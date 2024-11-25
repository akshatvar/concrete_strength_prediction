from django import forms

class CementInput(forms.Form):
    Cement = forms.FloatField(min_value=100,max_value=600)
    Blast_Furnace_Slag = forms.FloatField(min_value=0,max_value=380)
    Fly_Ash  = forms.FloatField(min_value=0,max_value=210)
    Water = forms.FloatField(min_value=100,max_value=250)
    Superplasticizer = forms.FloatField(min_value=0,max_value=35)
    Coarse_Aggregate = forms.FloatField(min_value=800,max_value=1150)
    Fine_Aggregate = forms.FloatField(min_value=580,max_value=1000)
    Age_in_Days = forms.IntegerField(min_value=1,max_value=365)