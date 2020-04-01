from django.db import models
from datetime import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField('Category',max_length=100,blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

class ResourceTag(models.Model):
    name = models.CharField('Resource Name',max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Resource Tags'
        verbose_name_plural = 'Resource Tags'

class LanguageCategory(models.Model):
    name = models.CharField('Language',max_length=20,blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Languages'
        verbose_name_plural = 'Languages'

class Problem(models.Model):
    name = models.CharField('Name',max_length=300,blank=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(ResourceTag)
    problem_statement = models.TextField('Problem Statement',blank=False)
    approach = models.TextField('Approach',blank=False)
    tip = models.TextField('Tips and Tricks',blank=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    important = models.BooleanField(default=True)
    short_note = models.CharField('Short Note',max_length=50,blank=False)

    def __str__(self):
        return 'Problem - '+str(self.id)

class SolutionCode(models.Model):
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
    language = models.ForeignKey(LanguageCategory,on_delete=models.CASCADE)
    code = models.TextField('Code',blank=False)

    def __str__(self):
        return 'Code '+str(self.id)
    
    class Meta:
        verbose_name = 'Solutions'
        verbose_name_plural = 'Solutions'

class ForeignResource(models.Model):
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
    name = models.CharField('Website',max_length=50,blank=False)
    link = models.URLField('URL',max_length=5000)

class CommentData(models.Model):
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
    comment = models.TextField('Comment',blank=False)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.comment)[:15]
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comment'

class Dates(models.Model):
    name = models.CharField('Name',max_length=50,blank=False)
    date = models.DateField(auto_now=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Dates'
        verbose_name_plural = 'Dates'