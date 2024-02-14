from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import  FinancialGoal, Expense, News
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import RegisterForm  
from django.contrib.auth.views import LoginView
from django.urls import reverse
from .models import Analitics 
from .models import Visit
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import FinancialResource
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm




def review_form(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = ReviewForm()
    
    return render(request, 'home.html', {'form': form})


def finance_resources(request):
    resources = FinancialResource.objects.all()
    return render(request, 'finance_resources.html', {'financial_resources': resources})

class MyLoginView(LoginView):
    template_name = 'login.html'


def logout_view(request):
    logout(request)
    return redirect(reverse('default_view'))

def register(request):
    if request.method == 'GET':
        form  = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('default_view')

        else:
            context = {'form': form}
            return render(request, 'register.html', context)

    return render(request, 'register.html', {})


def expense_list(request):
    expenses = Analitics.objects.all()  # Получаем все объекты Analitics
    if request.method != "POST":
        return render(request, 'expense-list.html', {'expenses': expenses})
    else:

        Analitics.objects.create(
            user=request.user, 
            name=request.POST["expenseName"],
            amount=request.POST["expenseAmount"],
            date =request.POST["deadline"],
        )
        
        return redirect("/")

def financial_planning(request):
    finances = FinancialGoal.objects.all()  # Получаем все объекты FinancialGoal
    if request.method != "POST":
        return render(request, 'financial-planning.html', {'finances': finances})
    else:
        FinancialGoal.objects.create(
            name=request.POST["finance_name"],
            amount=request.POST["target_amount"],
            date=request.POST["deadline"],
        )
        
        return redirect("/")

@login_required
def my_default_view(request):
    visit, created = Visit.objects.get_or_create(id=1)
    visit.increment()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(
                user=request.user, 
                rating=int(request.POST.get("rating")),
                comment=request.POST.get("comment"),
            )
            return redirect(reverse("default_view"))  # Redirect to a success page
    else:
        form = ReviewForm()

    return render(request, 'home.html', {'visit_count': visit.count, "form": form, "reviews": Review.objects.all()})



@login_required
def reports_and_analytics(request):
    expenses = Analitics.objects.filter(user=request.user)
    finances = FinancialGoal.objects.all()

    context = {
        'expenses': expenses,
        'finances': finances,
    }

    return render(request, 'reports-and-analytics.html', context)



def account_settings(request):
    return render(request, 'account-settings.html')

def capital(request):
    return render(request, 'capital.html')

def support(request):
    return render(request, 'support.html')

def news1_view(request):
    return render(request, 'news1.html') 

def news2_view(request):
    return render(request, 'news2.html') 

def news3_view(request):
    return render(request, 'news3.html') 

def news4_view(request):
    return render(request, 'news4.html') 

def news5_view(request):
    return render(request, 'news5.html') 

def news6_view(request):
    return render(request, 'news6.html') 

def news7_view(request):
    return render(request, 'news7.html') 

def news8_view(request):
    return render(request, 'news8.html') 

def news9_view(request):
    return render(request, 'news9.html') 

def news10_view(request):
    return render(request, 'news10.html') 

def economy_tips_view(request):
    return render(request, 'economy_tips.html') 

def investment_tips_view(request):
    return render(request, 'investment_tips.html') 

def investment2_tips_view(request):
    return render(request, 'investment2_tips.html') 



def increase_counter(request):
    visit, created = Visit.objects.get_or_create(id=1)
    visit.increment()
    return render(request, 'home.html', {'visit_count': visit.count})

def increase_counter(request):
    visit, created = Visit.objects.get_or_create(id=1)
    visit.increment()
    return HttpResponse(str(visit.count))


def delete_expenses(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('reports-and-analytics.html[]')  # Используйте фактическое имя, используемое в вашем шаблоне
        Expense.objects.filter(id__in=selected_ids).delete()
        # Предполагая, что вы хотите перенаправить после удаления, обновите URL по необходимости
        return redirect('expense-list')  # Обновите с фактическим именем URL
    return HttpResponse('Недопустимый метод запроса', status=400)

def edit_expense(request, expense_id):
    # Обработайте логику редактирования здесь
    # Предполагая, что вы хотите перенаправить после редактирования, обновите URL по необходимости
    return redirect('expense-list')  # Обновите с фактическим именем URL




def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Отправляем электронное письмо
        send_mail(
            f'Сообщение от {name}',
            f'От: {email}\n\n{message}',
            'boris.nicolaec@mail.ru',  # Замените на ваш адрес электронной почты
            ['boris.nicolaec@mail.ru'],  # Замените на ваш адрес электронной почты
            fail_silently=False,
        )

        return JsonResponse({'status': 'success', 'message': 'Сообщение успешно отправлено!'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Недопустимый метод запроса'})
    

def tax_calculator(request):
    if request.method == 'POST':
        income = float(request.POST.get('income'))
        # Здесь вы можете добавить вашу логику расчета налогов
        # Например, простой расчет 20% налога от дохода:
        tax_amount = 0.2 * income
        return render(request, 'tax_calculator.html', {'tax_amount': tax_amount})
    return render(request, 'tax_calculator.html')


