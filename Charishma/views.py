from django.shortcuts import render
from Charishma.models import *
# Create your views here.
def Table(request):
    LOT=Department.objects.all()
    d={'departments':LOT}
    return render(request,'Table.html',context=d)
def Table2(request):
    LOT2=Employee.objects.all()
    d={'employees':LOT2}
    return render(request,'Table2.html',context=d)
