from django.conf.urls import url

from .views import *

urlpatterns = [
    # api
    url(r'^api/v1/users/$', TeamDataList.as_view(), name="team_details"),
    url(r'^api/v1/user/(?P<pk>\d+)$', TeamMemberDetails.as_view(), name="get_team_member_details"),

]