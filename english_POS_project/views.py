from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth import password_validation
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from parsimonious.grammar import Grammar

import english_POS_project
import logging
import nltk

username_validator = UnicodeUsernameValidator()


# Create your views here.
def dashboard(request):
    return render(request, "english_POS_project/dashboard.html")


# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: First Name \n',
#                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
#     last_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: Last Name',
#                                widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})))
#     email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.',
#                              widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})))
#     password1 = forms.CharField(label=('Password'),
#                                 widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})),
#                                 help_text=password_validation.password_validators_help_text_html())
#     password2 = forms.CharField(label=('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
#                                 help_text=('Just Enter the same password, for confirmation'))
#     username = forms.CharField(
#         label=('Username'),
#         max_length=150,
#         help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.\n'),
#         validators=[username_validator],
#         error_messages={'unique': ("A user with that username already exists.")},
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
#     )

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

# class SignUp(CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"


# def password_reset_request(request):
# 	if request.method == "POST":
# 		password_reset_form = PasswordResetForm(request.POST)
# 		if password_reset_form.is_valid():
# 			data = password_reset_form.cleaned_data['email']
# 			associated_users = User.objects.filter(Q(email=data))
# 			if associated_users.exists():
# 				for user in associated_users:
# 					subject = "Password Reset Requested"
# 					email_template_name = "registration/password_reset_email.txt"
# 					c = {
# 					"email": user.email,
# 					'domain':'127.0.0.1:8000',
# 					'site_name': 'Website',
# 					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
# 					"user": user,
# 					'token': default_token_generator.make_token(user),
# 					'protocol': 'http',
# 					}
# 					email = render_to_string(email_template_name, c)
# 					try:
# 						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
# 					except BadHeaderError:
# 						return HttpResponse('Invalid header found.')
# 					return redirect ("/password_reset/done/")
# 	password_reset_form = PasswordResetForm()
# 	return render(request=request, template_name="registration/password_reset.html", context={"password_reset_form":password_reset_form})

# Perform parts of speech tagging
def pos_tagging(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(tokens)
    tags = [tag for _, tag in tagged_words]
    return tags


def POS_grammar(english):

    tags = pos_tagging(english)
    logging.info(print(tags))

    grammar = Grammar(r"""
    sentence = (word / space / punctuation)+ additional_tags?
    words = word+
    word = noun / verb / pronoun / adverb / adjective / preposition / determinant / conjunction / interjection / symbol / number / particle / modal / possessive_ending / to /  existential / foreign / other
    space = ~" +"
    
    noun = proper_plural_n / proper_singular_n / plural_n / singular_n
    singular_n = "NN"
    plural_n = "NNS"
    proper_singular_n = "NNP"
    proper_plural_n = "NNPS"
    
    pronoun = possessive_wh_pn / wh_pn / possessive_pn / base_pn
    base_pn = "PRP"
    possessive_pn = "PRP$"
    wh_pn = "WP"
    possessive_wh_pn = "WP$"
    
    verb = third_person_v / non_third_person_v / past_participle_v / present_v / past_v / base_v
    base_v = "VB"
    past_v = "VBD"
    present_v = "VBG"
    past_participle_v = "VBN"
    non_third_person_v = "VBP"
    third_person_v = "VBZ"
    
    adverb = wh_av / superlative_av / comparative_av / base_av
    base_av = "RB"
    comparative_av = "RBR"
    superlative_av = "RBS"
    wh_av = "WRB"
    
    adjective = superlative_adj / comparative_adj / base_adj
    base_adj = "JJ"
    comparative_adj = "JJR"
    superlative_adj = "JJS"
    
    preposition = "IN"
    
    determinant = wh_deter / pre_deter / base_deter
    base_deter = "DT"
    pre_deter = "PDT"
    wh_deter = "WDT"
    
    conjunction = "CC"
    interjection = "UH"
    to = "to"
    symbol = "SYM"                 
    number = "CD"
    particle = "RP"
    modal = "MD"   
    possessive_ending = "POS"
    existential = "EX" 
    foreign = "FW"          
    other = "X"
    punctuation = "." / "," / ":" / "'" / "?" / "!" 
    additional_tags = (~r".+")
""")


    my_grammar = grammar.parse(" ".join(tags))
    logging.info(print(my_grammar))
    context = { "parse_grammar": str(my_grammar),
        "num_of_sentences": str(my_grammar).count("sentence"),
        "num_of_words": str(my_grammar).count("word"),
        "num_of_spaces": str(my_grammar).count("space"),
        "num_of_pronouns": str(my_grammar).count("pronoun"),
        "num_of_nouns": str(my_grammar).count("noun"),
        "num_of_verbs": str(my_grammar).count("verb"),
        "num_of_adverbs": str(my_grammar).count("adverb"),
        "num_of_adjectives": str(my_grammar).count("adjective"),
        "num_of_prepositions": str(my_grammar).count("preposition"),
        "num_of_punctuation": str(my_grammar).count("punctuation")
    }
    return(context)

class UploadFileForm(forms.Form):
    file = forms.FileField()


class EnterInputForm(forms.Form):
    user_input = forms.CharField()

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            contents = f.read().decode("utf-8")
            print('valid')
            context = POS_grammar(contents)
            return render(request, 'english_POS_project/dashboard.html', {'user_input': contents, **context})
        else:
            print('invalid')
    return render(request, 'english_POS_project/dashboard.html', {'file': form})

def submit_sentence(request):
    if request.method == 'POST':
        form = EnterInputForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['user_input']
            context = POS_grammar(text)
            return render(request, 'english_POS_project/dashboard.html', {'user_input': text, **context})

    return render(request, 'english_POS_project/dashboard.html', {'text': form})