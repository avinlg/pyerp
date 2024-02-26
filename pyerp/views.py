from django.http import HttpResponse
from django_nextjs.render import render_nextjs_page

async def nextJSrequests(request):
    return await render_nextjs_page(request)