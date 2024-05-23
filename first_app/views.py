from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    return render(request, 'first_app/home.html')

def geeksforgeeks(request):
    data = { 'author': 'Karim',
            'txt' : "I'm karim",
            'emptyTxt': '',
            'age': 20, 
            'num': ['one', 'two', 'three', 'four'],
            'lower': 'My NAME is HOOMAN',
            'pub_date': datetime.datetime(2023, 12, 25, 10, 0, 0),
            'birthday': datetime.datetime.now(),
            'books': ['Book 1', 'Book 2', 'Book 3'], 
            'list': ['Python', 'is', 'best'],
            'list_2': ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],
            'desc': 'orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
            'courses': [
                {
                    'id': 1,
                    'name': 'Python',
                    'fee': 5000
                },
                {
                    'id': 2,
                    'name': 'Django',
                    'fee': 2000
                },
                {
                    'id': 3,
                    'name': 'C',
                    'fee': 6000
                },
                {
                    'id': 4,
                    'name': 'C++',
                    'fee': 6500
                },
            ] 
        }
    return render(request, 'first_app/geeksforgeeks.html', data)

def earthlydev(request):
    data = { 'author': 'Karim',
            'txt' : "I'm karim a student",
            'framework': 'django',
            'emptyTxt': '',
            'age': 20, 
            'num': ['one', 'two', 'three', 'four'],
            'lower': 'My NAME is HOOMAN',
            'pub_date': datetime.datetime(2023, 12, 25, 10, 0, 0),
            'birthday': datetime.datetime.now(),
            'books': ['Book 1', 'Book 2', 'Book 3'], 
            'list': ['Python', 'is', 'best'],
            'list_2': ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],
            'desc': 'orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
            'str': '0123456789',
            'courses': [
                {
                    'id': 1,
                    'name': 'Python',
                    'fee': 5000
                },
                {
                    'id': 2,
                    'name': 'Django',
                    'fee': 2000
                },
                {
                    'id': 3,
                    'name': 'C',
                    'fee': 6000
                },
                {
                    'id': 4,
                    'name': 'C++',
                    'fee': 6500
                },
            ] 
        }
    return render(request, 'first_app/earthlydev.html', data)