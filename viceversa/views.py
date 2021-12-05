from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    original_message = request.GET['message']
    reversed_message = original_message[::-1]
    return render(request,
                  'reverse.html',
                  {'original_message': original_message, 'reversed_message': reversed_message}
                  )
