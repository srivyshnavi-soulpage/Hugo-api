from django.urls import path

# Create your urls here.
from hugo.api.views import UserListCreate,UserDetail,EmployeeApi,EmployeeDetail,EmploymentApi,EmploymentDetail
from hugo.api.views import EmployDocsApi,EmployDocsDetail,EducationApi,EducationDetail,EducationDocsApi,EducationDocsDetail
from hugo.api.views import InternshipApi,InternshipDetail,SalaryApi,SalaryDetail,ProjectApi,ProjectDetail
from hugo.api.views import EventApi,EventDetail,HolidayApi,HolidayDetail,TicketApi,TicketDetail,RequestTicketApi,RequestTicketDetail
from hugo.api.views import TicketAvailabilityApi,TicketAvailabilityDetail

from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/',UserListCreate.as_view(), name='usercreate'),
    path('users/me/',UserDetail.as_view(),name='userlist'),

    path('employee/', EmployeeApi.as_view(),name='employee_List'),
    path('detail/<int:pk>/',EmployeeDetail.as_view(),name='employee_detail'),

    path('employment/', EmploymentApi.as_view(),name='employment_List'),
    path('detail/<int:pk>/',EmploymentDetail.as_view(),name='employment_detail'),

    path('employee/<int:pk>/employdocs/',EmployDocsApi.as_view(), name='employdocs'),
    path('update/docs/<int:pk>/',EmployDocsDetail.as_view(), name='docs-delete'),


    path('employee/<int:pk>/education/',EducationApi.as_view(), name='education'),
    path('update/edu/<int:pk>/',EducationDetail.as_view(), name='edu-delete'),

    path('education/<int:pk>/educationdocs/',EducationDocsApi.as_view(), name='educationdocs'),
    path('update/edu-docs/<int:pk>/',EducationDocsDetail.as_view(), name='edu_docs-delete'),


    path('internship/', InternshipApi.as_view(),name='interns'),
    path('interndetail/<int:pk>/',InternshipDetail.as_view(),name='internship_detail'),

    path('users/<int:pk>/salary/',SalaryApi.as_view(), name='salary'),
    path('users/me/detail/<int:pk>',SalaryDetail.as_view(),name='salary_detail'),

    path('users/<int:pk>/project/',ProjectApi.as_view(), name='project'),
    path('users/<int:pk>/projectdetail/',ProjectDetail.as_view(),name='project_detail'),

    path('event/', EventApi.as_view(),name='event_list'),
    path('detail/<int:pk>/', EventDetail.as_view(),name='event_details'),

    path('holiday/', HolidayApi.as_view(),name='holiday_list'),
    path('detail/<int:pk>/', HolidayDetail.as_view(),name='holiday_details'),


    path('ticket/', TicketApi.as_view(),name='ticket_list'),
    path('ticketdetail/<int:pk>/', TicketDetail.as_view(),name='ticket_details'),

    
    path('ticket/<int:pk>/request/',RequestTicketApi.as_view(),name="request_ticket"),
    path("requestlist/",RequestTicketDetail.as_view(), name="request_detail"),

    path('ticket/<int:pk>/availability/',TicketAvailabilityApi.as_view(),name="ticket_availability"),
    path("availablelist/",TicketAvailabilityDetail.as_view(), name="available_detail"),


]
