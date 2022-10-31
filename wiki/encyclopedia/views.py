
from pickle import GET
from turtle import title
from urllib import request
from django.shortcuts import render
from markdown2 import Markdown
from django import forms
from . import util
from django.utils.safestring import mark_safe
import random 






def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def html(data):
    markdown=Markdown()
    page=util.get_entry(data)
    htm=markdown.convert(page)
    if page: 
        return htm
    else:
     None





def input(request,title):
    markdown=Markdown()
    page=util.get_entry(title)
    if page is None:
     return render(request,"encyclopedia/notfound.html",{
         "entry":title
     })
    else:
         return render(request,"encyclopedia/found.html",{
          "entry":markdown.convert(page) ,
          "Title":title

         })




def search(request):
   
    if request.method=='GET':
        input=request.GET['q']
       
        entry=util.list_entries()
    
    
   
    if util.get_entry(input) :
         h=html(input)
         return render(request,"encyclopedia/found.html",{
               "entry":h,
               "Title":input,

            })
    else:
        
        search=[]
        for i in entry:
             if input.upper() in i.upper() :
               search.append(i)
        if not search:  
               return render(request,"encyclopedia/notfound.html",{
               "entry":title
              })

        return render(request,"encyclopedia/index.html",{
               "entries":search,
            })




def newpage(request):
    return render(request,"encyclopedia/newpage.html",{
})


def submit(request):
    
    if request.method=='POST':
        title=request.POST['title']
        data=request.POST['data']
        exists='False'
        entry=util.list_entries()
       
        for i in entry:
             if title.upper() in i.upper():
                  if  title == i.upper():
                    exists='True'
               
        if exists=='True':
             return render(request,"encyclopedia/existing.html",{
                "title":title,
            })
        else:
                markdown=Markdown()
                util.save_entry(title,data)
                save=util.get_entry(title)
                s=markdown.convert(save)
                
                return render(request,"encyclopedia/found.html",{
            "entry":s,
            "Title":title,
        })

    
def edit(request): 
	
	if request.method == 'POST':
	
		title = request.POST['title']

		data = util.get_entry(title)
		

		return render(request, "encyclopedia/edit.html",{
			"entry": data,
			"Title": title
		})         

def save(request):
     if request.method=='POST':
        title = request.POST['title']
        data=request.POST['data']
        markdown=Markdown()
        util.save_entry(title,data)
        save=util.get_entry(title)
        s=markdown.convert(save)
                
        return render(request,"encyclopedia/found.html",{
            "entry":s,
            "Title":title
        })

def randompage(request):
    list=util.list_entries()
    entry= random.choice(list)
    data=util.get_entry(entry)
    markdown=Markdown()
    s=markdown.convert(data)
    return render(request,"encyclopedia/found.html",{
            "entry":s,
            "Title":entry
        })

     

