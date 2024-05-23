from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from .forms import ckdForm
import numpy as np
import pickle

# Initialize classifier
filename = 'final_RF_classification_model.sav'
classifier = pickle.load(open(filename, 'rb'))

class dataUploadView(View):
    form_class = ckdForm
    success_url = reverse_lazy('success')
    template_name = 'create.html'
    failure_url = reverse_lazy('fail')
    filenot_url = reverse_lazy('filenot')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data_al = request.POST.get('Albumin')
            data_bgr = request.POST.get('Blood_Glucose_Random')
            data_bu = request.POST.get('Blood_Urea')
            data_sc = request.POST.get('Serum_Creatine')
            data_pcv = request.POST.get('Packed_cell_volume')
            data_wc = request.POST.get('White_blood_count')

            data = np.array([data_al, data_bgr, data_bu, data_sc, data_pcv, data_wc])
            try:
                out = classifier.predict(data.reshape(1, -1))
                return render(request, "succ_msg.html", {
                    'data_al': data_al,
                    'data_bgr': data_bgr,
                    'data_bu': data_bu,
                    'data_sc': data_sc,
                    'data_pcv': data_pcv,
                    'data_wc': data_wc,
                    'out': out
                })
            except Exception as e:
                print(e)
                return render(request, 'error.html', {'error': str(e)})
        else:
            return redirect(self.failure_url)
