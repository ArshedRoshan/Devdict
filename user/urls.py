from django.contrib import admin
from django.urls import path
from.views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('signup',signup,name='signup'),
    path('',getRoutes,name='routes'),
    path('token/',MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    # path('follow/<int:id>/', FollowView.as_view({'post': 'follows'})),
    path('follow',follows,name='follow'),
    path('user_list',user_list,name='user_list'),
    # path('unfollow',unfollow,name='unfollow'),
    path('company_list',company_list,name='company_list'),
    path('my_profile/<int:id>',my_profile,name='my_profile'),
    path('add_dp',add_dp,name='add_dp'),
    path('follow_check',follow_check,name='follow_check'),
    
    path('application',application,name='application'),
    path('applicant_view/<int:id>',applicant_view,name='applicant_view'),
    path('process_list/<int:id>/<int:cid>',process_list,name='process_list'),
    path('process_list1/<int:id>',process_list1,name='process_list1'),
    path('accept/<int:id>/<int:cid>',accept,name='accept'),
    path('accept1/<int:id>',accept1,name='accept1'),
    path('application_status/<int:id>',application_status,name='application_status'),
    path('validate',validate,name='validate'),
    path('chat_users',chat_users,name='chat_users'),
    path('block_user/<int:id>',block_user,name='block_user'),
    path('admin_user',admin_user,name='admin_user'),
    path('admin_comp',admin_comp,name='admin_comp'),
    path('count',count,name='count')
    # path('email-verify',getss,name='email-verify')
    
    
    
]
