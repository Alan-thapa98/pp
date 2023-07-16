from django.urls import path
from .views import (
    my_profile_view,
     ProfileDetailView,
        my_profile_view_edit
)

app_name = 'profiles'

urlpatterns = [
    # these is for the search reasut
    path('myprofile/', my_profile_view, name='my-profile-view'),
    path('myprofile/profile_edite', my_profile_view_edit,
         name='my-profile-view-edit'),
]
