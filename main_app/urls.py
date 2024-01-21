from django.urls import path

from .views import ListFile, ListFile2, ListData21, ListData22, ListMark, ListModel1, ListData21Statistics, \
    ListData22Statistics, ListMarks22, ListMarks21, ListModel22, ListModel21, DailyModel21CountView, \
    DailyModel22CountView

urlpatterns = [
    path('file_2021/', ListFile.as_view()),
    path('file_2022/', ListFile2.as_view()),
    path('data21/', ListData21.as_view()),
    path('data22/', ListData22.as_view()),
    path('data_marks/', ListMark.as_view()),
    path('data_models/', ListModel1.as_view()),

    path('statis21_when_get_models_by_id/', ListData21Statistics.as_view()),
    path('statis22_when_get_models_by_id/', ListData22Statistics.as_view()),
    path('only_marks22/', ListMarks22.as_view()),
    path('only_marks21/', ListMarks21.as_view()),
    path('only_models22/', ListModel22.as_view()),
    path('only_models21/', ListModel21.as_view()),
    path('new_statistics21/', DailyModel21CountView.as_view()),
    path('new_statistics22/', DailyModel22CountView.as_view()),
]