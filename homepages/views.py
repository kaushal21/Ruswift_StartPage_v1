from django.shortcuts import render
import pyrebase

config = {
    'apiKey': "AIzaSyCfc51zLIQfopAQj3msQgB3frwK7iglrYw",
    'authDomain': "learning-part-1.firebaseapp.com",
    'databaseURL': "https://learning-part-1.firebaseio.com",
    'projectId': "learning-part-1",
    'storageBucket': "learning-part-1.appspot.com",
    'messagingSenderId': "10891597566"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def login(request):
    template = 'homepage/login.html'
    context = {}
    return render(request, template, context)


def postlogin(request):
    email = request.POST.get('your-email')
    password = request.POST.get('password')

    user = auth.sign_in_with_email_and_password(email, password)

    return render(request, 'homepages/welcome.html', {"email": email})


def postsignup(request):
    fname = request.POST.get('your-email')
    lname = request.POST.get('password')
    month = request.POST.get('month')
    date = request.POST.get('date')
    year = request.POST.get('year')
    gender = request.POST.get('gender')
    email = request.POST.get('your_email')
    password = request.POST.get('your_password')
    repassword = request.POST.get('your_password1')
    code = request.POST.get('code')
    phone = request.POST.get('phone')
    employment = request.POST.get('employment')
    marital = request.POST.get('marital')

    street = request.POST.get('street')
    additional_info = request.POST.get('additional')
    zip_code = request.POST.get('zip')
    place = request.POST.get('place')
    country = request.POST.get('country')

    return render(request, 'homepages/student-data-survey.html')


def poststudentsurvey(request):
    college_fee = request.POST.get('college_fee')
    hostel = request.POST.get('hostel')
    hostel_fee = request.POST.get('hostel_fee')
    mess = request.POST.get('mess')
    canteen = request.POST.get('canteen')
    stationary = request.POST.get('stationary')
    pocket_money = request.POST.get('pocket_money')

    data_charges = request.POST.get('data_charges')
    movies_month = request.POST.get('movies_month')
    movies_charges = request.POST.get('movies_charges')
    club_charges = request.POST.get('club_charges');
    dinning_month = request.POST.get('dinning_month')
    dinning_charges = request.POST.get('dinning_charges')
    transport = request.POST.get('transport')

    financial_goal = request.POST.get('financial_goal')

    return render(request, 'homepages/')


def postemployedsurvey(request):
    income = request.POST.get('college_fee')
    investments = request.POST.get('investments')
    emi_no = request.POST.get('emi_no')
    emi_amt = request.POST.get('emi_amt')
    dependents_no = request.POST.get('dependents_no')
    dependents_cost = request.POST.get('dependents_cost')

    rent = request.POST.get('rent')
    electricity = request.POST.get('electricity')
    water = request.POST.get('water')
    grocery = request.POST.get('grocery')
    medication = request.POST.get('medication')

    data_charges = request.POST.get('data_charges')
    tv = request.POST.get('tv')
    movies_month = request.POST.get('movies_month')
    movies_charges = request.POST.get('movies_charges')
    club_charges = request.POST.get('club_charges');
    dinning_month = request.POST.get('dinning_month')
    dinning_charges = request.POST.get('dinning_charges')
    transport = request.POST.get('transport')

    financial_goal = request.POST.get('financial_goal')

    return render(request, 'homepages/')


def postselfemployedsurvey(request):
    income = request.POST.get('college_fee')
    investments = request.POST.get('investments')
    emi_no = request.POST.get('emi_no')
    emi_amt = request.POST.get('emi_amt')
    dependents_no = request.POST.get('dependents_no')
    dependents_cost = request.POST.get('dependents_cost')

    rent = request.POST.get('rent')
    electricity = request.POST.get('electricity')
    water = request.POST.get('water')
    grocery = request.POST.get('grocery')
    medication = request.POST.get('medication')

    data_charges = request.POST.get('data_charges')
    tv = request.POST.get('tv')
    movies_month = request.POST.get('movies_month')
    movies_charges = request.POST.get('movies_charges')
    club_charges = request.POST.get('club_charges');
    dinning_month = request.POST.get('dinning_month')
    dinning_charges = request.POST.get('dinning_charges')
    transport = request.POST.get('transport')

    business_capital = request.POST.get('business_capital')
    labour = request.POST.get('labour')
    labour_cost = request.POST.get('labour_cost')
    office = request.POST.get('office')
    office_rent = request.POST.get('office_rent')

    financial_goal = request.POST.get('financial_goal')

    return render(request, 'homepages/')


def index(request):
    return render(request, 'homepages/index.html')


def aboutus(request):
    return render(request, 'homepages/about-us.html')


def services(request):
    return render(request, 'homepages/service.html')


def login(request):
    return render(request, 'homepages/login.html')


def signup(request):
    return render(request, 'homepages/signup.html')


def help(request):
    return render(request, 'homepages/help.html')

