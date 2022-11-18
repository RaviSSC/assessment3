from django.shortcuts import render, redirect
from .models import Plane
from django.urls import reverse

# Create your views here.
def showPlane(request):
    # each entry of a plane is an object so i can use the .objects.all syntax and 
    # operations
    allPlanes=Plane.objects.all()
    return render(request,"showplane.html", {"allPlanes":allPlanes})

def addPlane(request):
    # create item
    # save
    # redirect
    # as each plane is an object i can update the name of the object 
    # by specifying the Plane(name=request.POST['name'])
    # note the name in the brackers refers to the model i created
    # in the models.py file
    newPlane= Plane(name=request.POST['name'])
    newPlane.save()
    print("post")
    # redirect function was hard to use- didnt realize it needed the "/"
    # to go back to the original page
    return redirect("/")


def deletePlane(request,plane_id):
    # retrieve item with id
    # as we have a number of entries that are all objects in the database
    # we can retrieve them by using the id.this comes from the urls.py page
    # and the html page where we are using the {{plane.id}} to single out 
    # the plane we are manipulating. using this function in the html
    # file gives is a /[number] when we edit it-> not 100% clear on this
    deleteItem = Plane.objects.get(id=plane_id)
    # delete
    deleteItem.delete()
    # redirect
    print("post")
    return redirect("/")

def editPlane(request,plane_id):
    # retrieve item with id
    editPlane = Plane.objects.get(id=plane_id)
    # delete
    editPlane.name=request.POST["name"]
    editPlane.save()
    # redirect
    return redirect("/")