from django.shortcuts import render


def home(request):
  return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        # Here you can handle form submission
        # For example, capture form data, validate, and send an email
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # You can add logic here to send the email or process the form data

        # Redirect or show success message
        return render(request, 'contact.html', {'success': True})

    # GET request: just render the contact page
    return render(request, 'contact.html')


        