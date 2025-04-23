# mysite/blog/views.py
from django.http import HttpResponse
from django.shortcuts import render

def post_list(request):
    return HttpResponse("Blog Posts List")

def post_detail(request, post_id):
    return HttpResponse(f"Post {post_id} Detail")