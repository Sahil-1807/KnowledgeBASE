from django.shortcuts import render
from .models import Category,Problem,SolutionCode,CommentData,Dates,ResourceTag,ForeignResource
from datetime import date
# Create your views here.


def index(request):
    filter = Category.objects.all()
    placement_date = Dates.objects.get(name='Placements')
    today_date = date.today()

    context = {
        'filters' : filter,
        'total': len(Problem.objects.all()),
        'old_problems': Problem.objects.all().order_by('date'),
        'new_problems': Problem.objects.all().order_by('-date'),
        'days' : (placement_date.date-today_date).days,
        'tags' : ResourceTag.objects.all()
    }
    return render(request,'Code/index.html',context)

def category(request,id):
    category = Category.objects.get(id=id)
    problems = Problem.objects.all().filter(category=category)

    context = {
        'filters': Category.objects.all(),
        'total': len(problems),
        'problems': problems,
        'tags' : ResourceTag.objects.all()
    }
    return render(request,'Code/category.html',context)


def tags(request,id):
    tag = ResourceTag.objects.get(id=id)
    problems = Problem.objects.all().filter(tags=tag)

    context = {
        'filters': Category.objects.all(),
        'total': len(problems),
        'problems': problems,
        'tags' : ResourceTag.objects.all()
    }
    return render(request,'Code/category.html',context)


def detail(request,id):
    if request.method=='POST':
        problem = Problem.objects.get(id=id)
        comment = CommentData(problem=problem,comment=request.POST.get('comment'))
        comment.save()
    comments = CommentData.objects.all().filter(problem=Problem.objects.get(id=id))
    problem = Problem.objects.get(id=id)
    solution = SolutionCode.objects.all().filter(problem=problem)[0]
    return render(request,'Code/detail.html',{
        'problem':problem,
        'solution':solution,
        'comments':comments,
        'foreign_resource':ForeignResource.objects.all().filter(problem=problem)
        })