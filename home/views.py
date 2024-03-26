from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from podcast_detail.models import Podcast


def home(request):
    podcast_list = Podcast.objects.all().order_by('-created_at')
    paginator = Paginator(podcast_list, 2)  # Show 3 podcast items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "home/index.html", {'page_obj': page_obj})
