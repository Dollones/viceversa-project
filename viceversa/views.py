from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    original_message = request.GET['message']
    reversed_message = original_message[::-1]
    words_amount = len(original_message.split())
    return render(request,
                  'reverse.html',
                  {'original_message': original_message, 'reversed_message': reversed_message,
                   'words_amount': words_amount}
                  )
