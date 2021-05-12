from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = "Compiler"

urlpatterns = [
    #compiler_only
    path('compiler-without-ui/', First_Compiler, name='First_Compiler'),
    path('main-compiler/', Main_Compiler, name='Main_Compiler'),

    #profile
    path('profile/',Profile, name="Profile"),
    path('login/', Login, name="Login"),
    path('logout/', Logout, name="Logout"),

    #contest
    #1.all_contest
    path('all_contest/', All_Contest, name="All_Contest"),
    #2.single_contest
    path('competition/<int:cid>/', Get_Into_Competition, name='Get_Into_Competition'),
    #3.competition_compiler
    path('competition_compiler/<int:cpid>', Solve_Competition_Problem, name="Solve_Competition_Problem"),

    #pratice
    #1. all_questions
    path('pratice/', Pratice, name="Pratice"),

    #3. question_compiler
    path('pratice_compiler/<int:pid>/', Solve_Pratice_Problem, name='SolvePraticeProblem'),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)