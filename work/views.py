from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import Http404

# View to list all WorkProgress records
def work_progress_list(request):
    work_progresses = WorkProgress.objects.all()  # Retrieve all records from the database
    return render(request, 'work_progress_table.html', {'work_progresses': work_progresses})

# View to create a new WorkProgress record
def work_progress_create(request):
    if request.method == 'POST':
        form = WorkProgressForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form to the database
            return redirect('ok')  # Redirect to the list view after successful creation
    else:
        form = WorkProgressForm()
    
    return render(request, 'site_details_form.html', {'form': form})

# View to edit an existing WorkProgress record
def work_progress_edit(request, ticket_id):
    work_progress = get_object_or_404(WorkProgress, ticket_id=ticket_id)
    
    if request.method == 'POST':
        form = WorkProgressForm(request.POST, instance=work_progress)
        if form.is_valid():
            form.save()  # Save the changes to the record
            return redirect('work_progress_list')  # Redirect to the list view
    else:
        form = WorkProgressForm(instance=work_progress)
    
    return render(request, 'work_progress_form.html', {'form': form, 'work_progress': work_progress})

# View to delete a WorkProgress record (optional)
def work_progress_delete(request, ticket_id):
    work_progress = get_object_or_404(WorkProgress, ticket_id=ticket_id)
    
    if request.method == 'POST':
        work_progress.delete()  # Delete the record
        return redirect('work_progress_list')  # Redirect to the list view
    
    return render(request, 'work_progress_confirm_delete.html', {'work_progress': work_progress})




def ok(request):
    application = get_object_or_404
    return render(request, 'ok.html', {'application': application})
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')




def site_details(request, data_id):
    site = get_object_or_404(WorkProgress, pk=data_id)
    if request.method == 'POST':
        status = request.POST.get('name')
        site.status = status
        site.save()
        return redirect('work_progress_list')
    return render(request, 'view_site_data.html', {'site': site})




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('hii')
        password = request.POST.get('12345')

        # Authenticate the user
        user = authenticate(request, usernam=username, password=password)

        if user is not None:
            # Successful login, redirect to home page or dashboard
            login(request, user)
            return redirect('work_progress_list')  # Change 'home' to your homepage view name
        else:
            # Authentication failed, show error message
            messages.error(request, 'Invalid username or password')
            return redirect('work_progress_list')  # Redirect back to login page

    return render(request, 'login.html')







from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmployeeLoginForm
from .models import Employee

def employee_signin(request):
    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)
        if form.is_valid():
            mobile_number = form.cleaned_data['mobile_number']
            password = form.cleaned_data['password']

            # Check if employee exists and the password is correct
            try:
                employee = Employee.objects.get(mobile_number=mobile_number)
                if employee.password == password:
                    if employee.is_approved:
                        # Redirect to a new page if login is approved
                        return redirect('employe_signin_check.html')  # Replace with your dashboard view
                    else:
                        messages.error(request, 'Your sign-in request has been rejected.')
                else:
                    messages.error(request, 'Invalid password.')
            except Employee.DoesNotExist:
                messages.error(request, 'Employee not found.')
    
    else:
        form = EmployeeLoginForm()

    return render(request, 'signin.html', {'form': form})










# # List all contact deals
# def contact_deal_list(request):
#     dealing = contract_deal.objects.all()
#     return render(request, 'contract_deal_list.html', {'dealing': dealing})




def contact_deal_list(request):
    deals = contract_deal.objects.all()
    return render(request, 'contract_deal_list.html', {'deals': deals})















# Create a new contact deal
def contact_deal_create(request):
    if request.method == 'POST':
        form = ContactDealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_deal_list')  # Redirect to the list page after success
    else:
        form = ContactDealForm()

    return render(request, 'contract_deal_form.html', {'form': form})

# Edit an existing contact deal
def contact_deal_edit(request, pk):
    deal = get_object_or_404(contract_deal, pk=pk)
    if request.method == 'POST':
        form = ContactDealForm(request.POST, instance=deal)
        if form.is_valid():
            form.save()
            return redirect('contract_deal_list')  # Redirect after save
    else:
        form = ContactDealForm(instance=deal)

    return render(request, 'contract_deal_form.html', {'form': form})

# View details of a single contact deal
def contact_deal_detail(request, pk):
    deal = get_object_or_404(contract_deal, pk=pk)
    return render(request, 'contact_deal_detail.html', {'deal': deal})


