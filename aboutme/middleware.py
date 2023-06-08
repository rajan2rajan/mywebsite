from django.shortcuts import render
class Underconstruction:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        # if site is under construction then 
        # response = render(request,'siteundercons.html')

        # if site is not under construction then 
        response = self.get_response(request)
        return response