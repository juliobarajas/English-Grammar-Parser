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
from nltk.tokenize import word_tokenize
from nltk import pos_tag

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
# Gathers only the needed tags and removes the words in the array.  
def pos_tagging_tags(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(tokens)
    tags = [tag for _, tag in tagged_words]
    return tags

# Parses the grammar with parsimonious and NLTK 
def POS_grammar(english):

    tags = pos_tagging_tags(english)
    logging.info(print(tags))

    grammar = Grammar(r"""
    grammar = (word / space / punctuation / ending_punctuation)+ additional_tags?
    word = noun / verb / pronoun / adverb / adjective / preposition / determinant / conjunction / interjection / symbol / number / particle / modal / possessive_ending / to /  existential / foreign / other
    space = ~" +"
    ending_punctuation = "." / "?" / "!"
    punctuation = "," / ":" / "'" 
                      
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
    to = "TO"
    symbol = "SYM"                 
    number = "CD"
    particle = "RP"
    modal = "MD"   
    possessive_ending = "POS"
    existential = "EX" 
    foreign = "FW"          
    other = "X"
     
    additional_tags = (~r".+")
""")

    # Prepares data for the Chart.js bar graph
    my_grammar = grammar.parse(" ".join(tags))
    logging.info(print(my_grammar))
    context = { "parse_grammar": str(my_grammar),
        "num_of_sentences": str(my_grammar).count("ending_punctuation"),
        "num_of_words": str(my_grammar).count("word"),
        "num_of_spaces": str(my_grammar).count("space") - str(my_grammar).count("punctuation") - str(my_grammar).count("'nt") - str(my_grammar).count("'ve"),
        "num_of_pronouns": str(my_grammar).count("pronoun"),
        "num_of_nouns": str(my_grammar).count("noun"),
        "num_of_verbs": str(my_grammar).count("verb"),
        "num_of_adverbs": str(my_grammar).count("adverb"),
        "num_of_adjectives": str(my_grammar).count("adjective"),
        "num_of_prepositions": str(my_grammar).count("preposition"),
        "num_of_determiners": str(my_grammar).count("determinant"),
        "num_of_punctuation": str(my_grammar).count("punctuation")
    }
    return(context)

# Form that user uploads .txt file into 
class UploadFileForm(forms.Form):
    file = forms.FileField(
        required=True,
        error_messages={'required': 'Only accepts .txt (text document) files'},    
        label="Upload a .txt file"
    )

# Form user manually enters grammar into
class EnterInputForm(forms.Form):
    user_input = forms.CharField(
        required= True, 
        label="Your Grammar",
    )

 # Handles request from upload file button    
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            contents = f.read().decode("utf-8")
            print('valid')
            context = POS_grammar(contents)
            return render(request, 'english_POS_project/submit_sentence.html', {'user_input': contents, **context})
        else:
            print('invalid')
    
        return render(request, 'english_POS_project/dashboard.html', {'file': form})
    else:
        return render(request, 'english_POS_project/dashboard.html')

# Handles both uploaded files, and manually entered grammar after pressing either button
def submit_sentence(request):
    nltk.download('help_tagsets')
    if request.method == 'POST':
        form = EnterInputForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['user_input']
            tagged_words = pos_tag(word_tokenize(text))
            
            # Prepare a list of tuples with (word, pos_tag, full_name)
            words_with_pos = []
            # Match up tags with respective full part of speech
            for word, pos in tagged_words:
                if pos == 'NN':
                 full_name = "Noun, common, singular or mass" 
                elif pos == 'NNP':
                    full_name = "Noun, proper, singular"
                elif pos == 'NNS':
                    full_name = "Noun, common, plural"
                elif pos == 'VB':
                    full_name = "Verb, base form" 
                elif pos == 'VBD':
                    full_name = "Verb, past tense"
                elif pos == 'VBG':
                    full_name = "Verb, present participle or gerund"
                elif pos == 'VBN':
                    full_name = "Verb, past participle"
                elif pos == 'VBP':
                    full_name = "Verb, present tense, not 3rd person singular"
                elif pos == 'VBZ':
                    full_name = "Verb, present tense, 3rd person singular"
                elif pos == 'JJ':
                    full_name = "Adjective or numeral, ordinal"
                elif pos == 'JJR':
                    full_name = "Adjective, comparative"
                elif pos == 'JJS':
                    full_name = "Adjective, superlative"
                elif pos == 'CC':
                    full_name = "Conjunction, coordinating" 
                elif pos == 'CD':
                    full_name = "Numeral, cardinal" 
                elif pos == 'DT':
                    full_name = "Determiner" 
                elif pos == 'EX':
                    full_name = "Existential there" 
                elif pos == 'IN':
                    full_name = "Preposition or conjunction, subordinating"   
                elif pos == 'LS':
                    full_name = "List item marker" 
                elif pos == 'MD':
                    full_name = "Modal auxiliary" 
                elif pos == 'PDT':
                    full_name = "Pre-determiner"  
                elif pos == 'POS':
                    full_name = "Genitive marker"  
                elif pos == 'PRP':
                    full_name = "Pronoun, personal" 
                elif pos == 'PRP$':
                    full_name = "pronoun, possessive" 
                elif pos == 'RB':
                    full_name = "Adverb" 
                elif pos == 'RBR':
                    full_name = "Adverb, comparative" 
                elif pos == 'RBS':
                    full_name = "Adverb, superlative" 
                elif pos == 'RP':
                    full_name = "Particle" 
                elif pos == 'TO':
                    full_name = "to as preposition or infinitive marker" 
                elif pos == 'UH':
                    full_name = "Interjection" 
                elif pos == 'WDT':
                    full_name = "WH-determiner" 
                elif pos == 'WP':
                    full_name = "WH-pronoun"  
                elif pos == 'WRB':
                    full_name = "WH-adverb"   
                elif pos == '.':
                    full_name = "Punctuation"    

                words_with_pos.append((word, pos, full_name))  
                   

            context = POS_grammar(text)
            return render(request, 'english_POS_project/submit_sentence.html', {'user_input': text, 'words_with_pos': words_with_pos, **context})
        return render(request, 'english_POS_project/dashboard.html', {'text': form})
    
    else: 
        # Used when returning to the dashboard from the submit_sentence view
        return render(request, 'english_POS_project/dashboard.html')
