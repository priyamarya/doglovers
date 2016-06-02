from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from .models import Cards
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.users.models import UserProfile
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from app.comments.models import Comment
from app.likes.models import CardLikes
from .forms import CardsForm

# Create your views here.


# @login_required(login_url="/users/login")
def all_cards(request):
    """This, function show all cards."""
    # import ipdb; ipdb.set_trace()

    context = {}
    cards = Cards.objects.all()

    paginator = Paginator(cards, 30)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        cards = paginator.page(page)
    except(EmptyPage, InvalidPage):
        cards = paginator.page(paginator.num_pages)
    context = {
        'cards': cards
    }
    context.update(csrf(request))

    return render(request, "allcards.html", context)


@login_required(login_url="/users/login")
def view_card(request, card_id):
    """For displaying single card."""
    # import ipdb; ipdb.set_trace()

    context = {}
    user = request.user
    user = UserProfile.objects.get(name=user)
    card = Cards.objects.get(id=card_id)
    comment = card.name
    comment = Comment.objects.filter(comment_on_card=card)
    
    if (card.card_likes.filter(user=user).exists()):
        like_button = 'unlike'
    else:
        like_button = 'like'
    if card.v_type == "public":
        likers = []
        for item in CardLikes.objects.filter(like_on_card=card):
            likers.append(str(item.user))
        context = {
            'card': card,
            'like_button': like_button,
            'message': "public",
            "likers": likers,
            'comments': comment

        }
        context.update(csrf(request))
        return render(request, 'viewcard.html', context)
    else:
        if str(card.user) == str(request.user):
            context = {'message': "private", 'card': card}
            context.update(csrf(request))
            return render(request, 'viewcard.html', context)
        else:
            context = {'message': "Sorry. You are not authorised to see this card page."}
            context.update(csrf(request))
            return render(request, 'viewcard.html', context)


@login_required(login_url="/users/login")
def new_card(request):
    context = {}
    # import ipdb; ipdb.set_trace()
    form = CardsForm(request.POST, request.FILES or None)
    context = {
        "form": form,
        'message': "Please enter card information."

    }
    user = request.user
    user = UserProfile.objects.get(user=user)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = user
        instance.save()
        context = {
            'message': "Card is Saved"
        }



    # if request.method == "POST":
    #     try:
    #         name = request.POST.get('name')
    #         image = request.FILES.get('image')
    #         desc = request.POST.get('desc')
    #         v_type = request.POST.get('v_type')
    #         created_by = request.user
    #         created_by = UserProfile.objects.get(user=created_by)
    #         new_card = Cards(name=name, image=image, desc=desc, user=created_by, v_type=v_type)
    #         new_card.save()
    #         context = {'success': True, 'message': "card saved"}
    #         context.update(csrf(request))

        # except:
        #     context = {'success': False, 'message': "card not saved"}
    context.update(csrf(request))
    return render(request, "newcard.html", context)





def search(request):
   
    context = {}
    # import ipdb; ipdb.set_trace()

    if request.method == "POST":
        find = request.POST.get('find')
        cards = Cards.objects.filter(name__icontains=find)
        
        context = {
            'list': cards
        }
        context.update(csrf(request))

    return render(request, "show.html", context)

