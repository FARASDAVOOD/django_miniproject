from django.shortcuts import render

# Create your views here.

def create(request):
    if request.POST:
        print(request.POST.get("name"))
        print(request.POST.get("place"))
    return render(request,"create.html")

def list(request):
     movie_data={
      "movies":[{
      "name":"john1",
      "age":301,
    #   "place":"calicut1  ",
      "sucess":False,
      "img":"img1.jpg"
    },
    {
      "name":"john2",
      "age":302,
      "place":"calicut2  ",
      "sucess":True,
      "img":"img2.png"
    },{
      "name":"john3",
      "age":303,
      "place":"calicut3 ",
      "sucess":True,
      "img":"img3.jpg"
    },{
      "name":"john4",
      "age":304,
      "place":"calicut4  ",
      "sucess":False,
      "img":"img4.jpg"
    }]}
     return render(request,"list.html",movie_data)

def edit(request):
    return render(request,"edit.html")