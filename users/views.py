from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.db.models import Q
from authentication.models import User
from .forms import UserCreate, UserLogin
from .models import Profile, Relationship, Notification
import datetime
# Create your views here.


def profile(request, username):

    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(Profile, user=user)

    friends = Relationship.objects.filter(Q(user=user), Q(status=1) | Q(status=2))

    template_name = 'users/user_profile.html'

    # TODO: Check privacy settings

    return render(request, template_name, {'user_profile': user_profile, 'friends': friends})


def add_friend(request, pk):

    # Make sure that the friend requested to be friends actually exists
    try:
        requested_friend = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404("User does not exist!")

    # Make sure the user does not try and friend himself
    if requested_friend.id is request.user.id:
        return HttpResponse("You cannot friend yourself!")

    user = User.objects.get(pk=request.user.id)

    # Make sure that the user and the requested friend are not already friends
    try:
        request = Relationship.objects.get(Q(user=user, corrUser=requested_friend) | Q(user=requested_friend,
                                                                                       corrUser=user))

        if request is not None:
            return HttpResponse("You are already friends with this user or you have already requested to be friends!")

    except Relationship.DoesNotExist:

        # First update database with the request
        request = Relationship(user=user, corrUser=requested_friend, status=0)
        request.save()

        # Grab the profile picture of the user requesting the friend request
        user_profile = Profile.objects.get(user=user)

        description = "User " + user.username + " has requested to be your friend"

        # Notify the requested_friend about the friend request
        notification = Notification(user=requested_friend, image=user_profile.profilePic.image, description=description,
                                    datetime=datetime.datetime.now(), type=2)
        notification.save()

        return HttpResponse("Friend request sent")


class UserCreateView(View):

    form_class = UserCreate

    template_name = 'users/user_create.html'

    # Requested the form
    def get(self, request):

        # Show a blank form
        # TODO: Use JavaScript to fill the form out with previous data (reattempting)

        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        # User has submitted the form to create an account
        # TODO: Use JavaScript to validate the data

        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)

            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)

        return render(request, self.template_name, {'form': form})


# TODO: User login needs to be re-written possibly using customer authentication


class UserLoginView(View):

    form_class = UserLogin

    template_name = 'users/user_login.html'

    def get(self, request):

        # Show a blank form
        # TODO: Use JavaScript to fill the form out with previous data (reattempting)

        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():

            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)

        return render(request, self.template_name, {'form': form})
