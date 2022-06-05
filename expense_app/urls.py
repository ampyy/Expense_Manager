from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("", views.home_view, name='home'),
    path("about", views.about_view, name='about'),
    path("expenses", views.index, name='expenses'),
    path("expenses/add-expense", views.add_expense, name="add-expense"),
    path("expenses/edit-expense/<int:id>", views.expense_edit, name="edit-expense"),
    path("expenses/delete-expense/<int:id>", views.delete_expense, name="delete-expense"),
    path("authentication/register", views.RegistrationView.as_view(), name='register'),
    path("authentication/login", views.LoginView.as_view(), name='login'),
    path('authentication/logout', views.LogoutView.as_view(), name="logout"),
    path("authentication/validate-username", csrf_exempt(views.UsernameValidateView.as_view()), name='validate-username'),
    path("authentication/validate-email", csrf_exempt(views.EmailValidateView.as_view()), name='validate-email'),
     path("search-expense", csrf_exempt(views.search_expenses), name='search-expense'),
    path("preferences", views.preferences, name='preferences'),
    path("income", views.income, name='income'),
    path("income/add-income", views.add_income, name="add-income"),
    path("income/edit-income/<int:id>", views.income_edit, name="edit-income"),
    path("income/delete-income/<int:id>", views.delete_income, name="delete-income"),
    path("search-income", csrf_exempt(views.search_income), name='search-income'),
    path('expense_category_summary', views.expense_category_summary, name="expense_category_summary"),
    path("stats", views.stats_view, name="stats"),
     path('income_category_summary', views.income_category_summary, name="income_category_summary"),
    path("stats-income", views.stats_view_income, name="stats-income"),
    path("export", views.export_view, name='export'),
    path("export-csv", views.export_csv, name='export-csv'),
    path("export-excel", views.export_excel, name='export-excel'),
    path("export-csv-income", views.export_csv_income, name='export-csv-income'),
    path("export-excel-income", views.export_excel_income, name='export-excel-income'),


]
