from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from account_module.models import Stylist, User
from django.shortcuts import render
from django.core.paginator import Paginator
from stylist.models import Services, TimeSlot
from appointment.models import Appointment


def get_stylists(request):
    if not request.user.is_authenticated:
        return redirect('login_page')

    user = request.user
    services = Services.objects.all()
    # if request.method == 'POST':
    #     province = request.POST.get('province')
    #     city = request.POST.get('city')
    #     if province and city:
    #         stylists = Stylist.objects.filter(province = province, city = city).order_by('rating')
    #         paginator = Paginator(stylists, 10)
    #         page_number = request.GET.get('page')
    #         page_obj = paginator.get_page(page_number)
    #         return render(request, 'stylist/customerIndex.html', {'page_obj': page_obj})
    #     elif province:
    #         stylists = Stylist.objects.filter(province = province).order_by('rating')
    #         paginator = Paginator(stylists, 10)
    #         page_number = request.GET.get('page')
    #         page_obj = paginator.get_page(page_number)
    #         return render(request, 'stylist/customerIndex.html', {'page_obj': page_obj})
    stylists = Stylist.objects.all().order_by('rating')
    return render(request, 'stylist/customerIndex.html', {'stylists': stylists, 'user' : user, 'services': services})

def get_stylist(request, stylist_id):
    if not request.user.is_authenticated:
        return redirect('login_page')
    stylist = get_object_or_404(Stylist, id=stylist_id)
    services = stylist.services.all()
    time_slots = stylist.time_slots.all()
    stylists = Stylist.objects.all()

    context = {
        'stylist': stylist,
        'services': services,
        'time_slots': time_slots,
        'stylists': stylists,
    }
    return render(request, 'stylist/detail.html', context)

def stylist_view(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    stylist = User.objects.filter(id=request.user.id).first()
    context = {
        'stylist': stylist
    }
    return render(request, 'stylist/stylistIndex.html', context)

