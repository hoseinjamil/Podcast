from django.shortcuts import render, get_object_or_404, redirect
from .models import Podcast
from .forms import AddPodcastForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def podcast_detail(request, title):
    podcast = get_object_or_404(Podcast, title=title)
    podcast_show = Podcast.objects.all().order_by('-created_at')[:2]
    return render(request, 'podcast_detail/podcast_detail.html', context={'podcast': podcast, 'podcast_show':podcast_show})


def add_podcast(request):
    if request.method == 'POST':
        form = AddPodcastForm(request.POST, request.FILES)
        if form.is_valid():
            podcast = form.save(commit=False)
            podcast.author = request.user
            podcast.save()
            messages.success(request, "You have added a podcast Now")

            return redirect('add_podcast')
    else:
        form = AddPodcastForm()
        # Retrieve all podcasts belonging to the current user
    podcasts = Podcast.objects.filter(author=request.user)
    return render(request, 'podcast_detail/add_podcast.html', {'form': form, 'podcasts':podcasts})


@login_required
def delete_podcast(request, title):
    podcasts = get_object_or_404(Podcast, title=title, author=request.user)
    if request.method == 'POST':
        podcasts.delete()
        messages.success(request, "You have removed a podcast Now")
        return redirect('add_podcast')
    return render(request, 'podcast_detail/add_podcast.html', {'podcasts': podcasts})
