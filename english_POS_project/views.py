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

def POS_grammar(english):

    grammar = Grammar ( r""" 
        sentence = (word / space / punctuation)+
        word = (pronoun / noun / verb / adverb / adjective / preposition)+
        space = ~" +" 
        pronoun = "I"/"another"/"anybody"/"anyone"/"anything"/"both"/"but"/"certain"/"either"/"enough"/"everybody"/"everyone"/"everything"/"extra"/"few"/"he "/"her "/"hers "/"herself"/"him"/"himself"/"his"/"hon"/"idem"/"it "/"itself"/"me"/"mine"/"my"/"myself"/"next"/"nobody"/"none"/"nothing"/"one"/"oneself"/"other"/"others"/"ours"/"ourselves"/"own"/"plenty"/"same"/"self"/"she"/"some"/"somebody"/"someone"/"something"/"somewhat"/"such"/"that"/"thee"/"theirs"/"them"/"themselves"/"these"/"they"/"thine"/"this"/"those"/"thou"/"thy"/"thyself"/"us"/"we"/"what"/"whatever"/"whatsoever"/"when"/"which"/"whichever"/"who"/"whoever"/"whom"/"whomever"/"whomsoever"/"whose"/"whoso"/"whosoever"/"ya"/"ye"/"you"/"your"/"yours"/"yourself"/"yourselves"
        noun = "python"/"a "/"act"/"active"/"activity"/"age"/"air"/"amount"/"answer"/"anything"/"apple"/"area"/"arm"/"army"/"art"/"ask"/"attack"/"baby"/"back"/"bad"/"bag"/"ball"/"bank"/"base"/"basket"/"bath"/"bear"/"beautiful"/"bed"/"bedroom"/"beer"/"bell"/"big"/"bird"/"birth"/"birthday"/"bit"/"bite"/"black"/"block"/"blood"/"blow"/"blue"/"board"/"boat"/"body"/"bone"/"book"/"border"/"bottle"/"bottom"/"bowl"/"box"/"boy"/"branch"/"brave"/"bread"/"break"/"breakfast"/"bridge"/"brother"/"brown"/"brush"/"burn"/"business"/"bus"/"buy"/"cake"/"call"/"can"/"candle"/"cap"/"car"/"card"/"care"/"carry"/"case"/"cat"/"catch"/"chair"/"chance"/"change"/"chicken"/"child"/"chocolate"/"choice"/"city"/"class"/"clock"/"clothes"/"cloud"/"coffee"/"coat"/"cold"/"comfortable"/"common"/"computer"/"condition"/"control"/"cook"/"corner"/"cost"/"count"/"country"/"course"/"cover"/"crash"/"cross"/"cry"/"cup"/"cut"/"dance"/"dark"/"daughter"/"day"/"dead"/"deep"/"desk"/"dinner"/"direction"/"dish"/"dog"/"door"/"double"/"draw"/"dream"/"dress"/"drink"/"drive"/"drop"/"dust"/"duty"/"ear"/"earth"/"east"/"eat"/"education"/"effect"/"egg"/"end"/"equal"/"entrance"/"escape"/"evening"/"event"/"examination"/"example"/"exercise"/"eye"/"face"/"fact"/"fail"/"fall"/"family"/"farm"/"father"/"fat"/"fault"/"fear"/"feed"/"feel"/"female"/"few"/"fight"/"fill"/"film"/"finger"/"finish"/"fire"/"fish"/"fix"/"floor"/"flower"/"fly"/"fold"/"food"/"foot"/"football"/"force"/"form"/"freedom"/"friend"/"front"/"fruit"/"fun"/"funny"/"future"/"game"/"garden"/"gate"/"general"/"gift"/"give"/"glad"/"glass"/"go"/"god"/"gold"/"good"/"grandfather"/"grandmother"/"grass"/"great"/"green"/"ground"/"group"/"hair"/"half"/"hall"/"hand"/"hat"/"hate"/"head"/"heavy"/"heart"/"height"/"hello"/"help"/"hide"/"high"/"hit"/"hold"/"hole"/"holiday"/"home"/"hope"/"horse"/"hospital"/"hotel"/"house"/"hour"/"hurry"/"husband"/"hurt"/"ice"/"idea"/"if"/"increase"/"inside"/"iron"/"invite"/"island"/"it"/"job"/"join"/"juice"/"jump"/"keep"/"key"/"kill"/"kind"/"king"/"kitchen"/"knee"/"knife"/"ladder"/"lady"/"land"/"laugh"/"lead"/"leave"/"leg"/"length"/"lesson"/"let"/"letter"/"library"/"lie"/"life"/"light"/"lip"/"list"/"listen"/"lock"/"long"/"look"/"love"/"low"/"luck"/"machine"/"main"/"make"/"male"/"man"/"many"/"map"/"mark"/"market"/"matter"/"meal"/"meat"/"medicine"/"meet"/"member"/"mention"/"method"/"middle"/"milk"/"mind"/"minute"/"miss"/"mistake"/"mix"/"model"/"moment"/"money"/"month"/"morning"/"most"/"mother"/"mountain"/"mouth"/"move"/"music"/"name"/"nation"/"nature"/"neck"/"net"/"news"/"newspaper"/"night"/"noise"/"north"/"nose"/"nothing"/"notice"/"number"/"object"/"offer"/"office"/"oil"/"one"/"opposite"/"orange"/"order"/"other"/"outside"/"page"/"pain"/"paint"/"pair"/"paper"/"parent"/"park"/"part"/"partner"/"party"/"pass"/"past"/"path"/"pay"/"peace"/"pen"/"people"/"period"/"person"/"piano"/"pick"/"picture"/"piece"/"pin"/"place"/"plane"/"plant"/"plastic"/"plate"/"play"/"plenty"/"point"/"police"/"pool"/"position"/"possible"/"potato"/"power"/"present"/"press"/"price"/"private"/"prize"/"problem"/"produce"/"promise"/"public"/"pull"/"push"/"put"/"queen"/"question"/"quiet"/"radio"/"rain"/"raise"/"reach"/"read"/"record"/"red"/"remove"/"rent"/"repair"/"repeat"/"reply"/"report"/"rest"/"restaurant"/"result"/"return"/"rice"/"rich"/"ride"/"ring"/"rise"/"road"/"rock"/"room"/"round"/"rule"/"run"/"rush"/"sad"/"safe"/"sail"/"salt"/"sand"/"save"/"school"/"science"/"search"/"seat"/"second"/"sell"/"sentence"/"serve"/"sex"/"shake"/"shape"/"share"/"she"/"shine"/"ship"/"shirt"/"shoe"/"shoot"/"shop"/"shoulder"/"show"/"sick"/"side"/"signal"/"silly"/"silver"/"simple"/"single"/"sing"/"sink"/"sister"/"size"/"skill"/"skin"/"skirt"/"sky"/"sleep"/"slip"/"smell"/"smile"/"smoke"/"snow"/"sock"/"soft"/"son"/"sound"/"soup"/"south"/"space"/"special"/"speed"/"spell"/"spend"/"sport"/"spread"/"spring"/"square"/"stand"/"star"/"start"/"station"/"stay"/"steal"/"step"/"still"/"stomach"/"stop"/"store"/"storm"/"story"/"street"/"structure"/"student"/"study"/"stupid"/"subject"/"substance"/"sugar"/"summer"/"sun"/"support"/"surprise"/"sweet"/"swim"/"table"/"talk"/"taste"/"tea"/"teach"/"team"/"tear"/"telephone"/"television"/"tell"/"tennis"/"test"/"thing"/"tie"/"title"/"today"/"toe"/"tomorrow"/"tonight"/"tool"/"tooth"/"top"/"total"/"touch"/"town"/"train"/"travel"/"tree"/"trouble"/"trust"/"try"/"turn"/"type"/"uncle"/"unit"/"use"/"usual"/"vegetable"/"village"/"voice"/"visit"/"wait"/"wake"/"walk"/"wash"/"watch"/"water"/"way"/"wear"/"weather"/"wedding"/"week"/"weight"/"welcome"/"west"/"wheel"/"while"/"white"/"wife"/"will"/"win"/"wind"/"window"/"wine"/"winter"/"wish"/"woman"/"wonder"/"word"/"work"/"world"/"worry"/"yard"/"yesterday"/"you"/"young"/"two"  
        verb = "punch"/"love"/"be"/"have"/"know"/"see"/"want"/"do "/"take"/"use"/"provide"/"make"/"go"/"get"/"find"/"say"/"tell"/"support"/"need"/"give"/"help"/"include"/"come"/"work"/"ensure"/"improve"/"put"/"talk"/"increase"/"ask"/"keep"/"allow"/"reduce"/"call"/"receive"/"become"/"like"/"create"/"play"/"believe"/"promote"/"protect"/"change"/"live"/"leave"/"prevent"/"determine"/"let"/"meet"/"set"/"understand"/"develop"/"show"/"stop"/"try"/"look"/"consider"/"open"/"read"/"remain"/"offer"/"stay"/"pay"/"strengthen "/" form"/"start"/"establish"/"send"/"kill"/"achieve"/"bring"/"hear"/"wait"/"avoid"/"encourage"/"hope"/"add"/"think"/"follow"/"control"/"contribute"/"produce"/"maintain"/"speak"/"complete"/"choose"/"thank"/"obtain"/"buy"/"implement"/"listen"/"participate"/"address"/"require"/"share"/"enhance"/"save"/"wish"/"assist"/"note"/"enable"/"accept"/"contain"/"check"/"enjoy"/"serve"/"learn"/"indicate"/"die"/"move"/"build"/"represent"/"eat"/"hold"/"cover"/"forget"/"submit"/"prepare"/"select"/"discuss"/"apply"/"decide"/"access"/"research"/"finance"/"adopt"/"return "/" reach"/"explain"/"visit"/"remove"/"assess"/"feel"/"recognize"/"monitor"/"act"/"appear"/"generate"/"define"/"begin"/"inform"/"run"/"cut"/"lose"/"seek"/"write"/"respond"/"review"/"discover"/"watch"/"seem"/"respect"/"contact"/"guarantee"/"manage"/"benefit"/"reflect"/"comprise"/"enter"/"sell"/"spend"/"cause"/"win"/"perform"/"answer"/"express"/"replace"/"sleep"/"download"/"end"/"concern"/"operate"/"affect"/"eliminate"/"lead"/"examine"/"happen"/"turn"/"limit"/"view"/"communicate"/"report"/"vote"/"agree"/"raise"/"study"/"confirm"/"introduce"/"request"/"cooperate "/" imagine"/"collect"/"claim"/"conduct"/"prove"/"join"/"extend"/"explore"/"propose"/"describe"/"invite"/"treat"/"fight"/"hate"/"measure"/"detect"/"permit"/"close"/"recommend"/"demonstrate"/"deliver"/"equal"/"resolve"/"evaluate"/"fill"/"result"/"exceed"/"grow"/"carry"/"draw"/"solve"/"consult"/"wear"/"destroy"/"sign"/"target"/"suggest"/"expand"/"miss"/"fear"/"specify"/"defend"/"overcome"/"mean"/"appreciate"/"depend"/"exercise"/"welcome"/"vary"/"teach"/"walk"/"dry"/"transmit"/"remind"/"fix"/"focus"/"deal"/"preserve"/"break"/"realize"/"finish"
        adverb = "abnormally"/"absentmindedly"/"accidentally"/"actually"/"adventurously"/"afterwards"/"almost"/"always"/"annually"/"anxiously"/"arrogantly"/"awkwardly"/"bashfully"/"beautifully"/"bitterly"/"bleakly"/"blindly"/"blissfully"/"boastfully"/"boldly"/"bravely"/"briefly"/"brightly"/"briskly"/"broadly"/"busily"/"calmly"/"carefully"/"carelessly"/"cautiously"/"certainly"/"cheerfully"/"clearly"/"cleverly"/"closely"/"coaxingly"/"colorfully"/"commonly"/"continually"/"coolly"/"correctly"/"courageously"/"crossly"/"cruelly"/"curiously"/"daily"/"daintily"/"dearly"/"deceivingly"/"deeply"/"defiantly"/"deliberately"/"delightfully"/"diligently"/"dimly"/"doubtfully"/"dreamily"/"easily"/"elegantly"/"energetically"/"enormously"/"enthusiastically"/"equally"/"especially"/"even"/"evenly"/"eventually"/"exactly"/"excitedly"/"extremely"/"fairly"/"faithfully"/"famously"/"far"/"fast"/"fatally"/"ferociously"/"fervently"/"fiercely"/"fondly"/"foolishly"/"fortunately"/"frankly"/"frantically"/"freely"/"frenetically"/"frightfully"/"fully"/"furiously"/"generally"/"generously"/"gently"/"gladly"/"gleefully"/"gracefully"/"gratefully"/"greatly"/"greedily"/"happily"/"hastily"/"healthily"/"heavily"/"helpfully"/"helplessly"/"highly"/"honestly"/"hopelessly"/"hourly"/"hungrily"/"immediately"/"innocently"/"inquisitively"/"instantly"/"intensely"/"intently"/"interestingly"/"inwardly"/"irritably"/"jaggedly"/"jealously"/"jovially"/"joyfully"/"joyously"/"jubilantly"/"judgmentally"/"justly"/"keenly"/"kiddingly"/"kindheartedly"/"kindly"/"knavishly"/"knowingly"/"knowledgeably"/"kookily"/"lazily"/"less"/"lightly"/"likely"/"limply"/"lively"/"loftily"/"longingly"/"loosely"/"loudly"/"lovingly"/"loyally"/"madly"/"majestically"/"meaningfully"/"mechanically"/"merrily"/"miserably"/"mockingly"/"monthly"/"more"/"mortally"/"mostly"/"mysteriously"/"naturally"/"nearly"/"neatly"/"nervously"/"never"/"nicely"/"noisily"/"not"/"obediently"/"obnoxiously"/"oddly"/"offensively"/"officially"/"often"/"only"/"openly"/"optimistically"/"overconfidently"/"painfully"/"partially"/"patiently"/"perfectly"/"physically"/"playfully"/"politely"/"poorly"/"positively"/"potentially"/"powerfully"/"promptly"/"properly"/"punctually"/"quaintly"/"queasily"/"queerly"/"questionably"/"quicker"/"quickly"/"quietly"/"quirkily"/"quizzically"/"rightfully"/"randomly"/"rapidly"/"rarely"/"readily"/"really"/"reassuringly"/"recklessly"/"regularly"/"reluctantly"/"repeatedly"/"reproachfully"/"restfully"/"righteously"/"rigidly"/"roughly"/"rudely"/"safely"/"scarcely"/"scarily"/"searchingly"/"sedately"/"seemingly"/"seldom"/"selfishly"/"separately"/"seriously"/"shakily"/"sharply"/"sheepishly"/"shrilly"/"shyly"/"silently"/"sleepily"/"slowly"/"smoothly"/"softly"/"solemnly"/"solidly"/"sometimes"/"soon"/"speedily"/"stealthily"/"sternly"/"strictly"/"successfully"/"suddenly"/"supposedly"/"surprisingly"/"suspiciously"/"sweetly"/"swiftly"/"sympathetically"/"tenderly"/"tensely"/"terribly"/"thankfully"/"thoroughly"/"thoughtfully"/"tightly"/"tomorrow"/"too"/"tremendously"/"triumphantly"/"truly"/"truthfully"/"ultimately"/"unabashedly"/"unaccountably"/"unbearably"/"unethically"/"unexpectedly"/"unfortunately"/"unimpressively"/"unnaturally"/"unnecessarily"/"upbeat"/"upright"/"upside-down"/"upward"/"urgently"/"usefully"/"uselessly"/"usually"/"utterly"/"vacantly"/"vaguely"/"vainly"/"valiantly"/"vastly"/"verbally"/"very"/"viciously"/"victoriously"/"violently"/"vivaciously"/"voluntarily"/"warmly"/"weakly"/"wearily"/"well"/"wetly"/"wholly"/"wildly"/"willfully"/"wisely"/"woefully"/"wonderfully"/"worriedly"/"wrongly"/"yawningly"/"yearly"/"yearningly"/"yesterday"/"yieldingly"/"youthfully"/"zealously"/"zestfully"/"zestily"
        adjective = "able"/"bad"/"best"/"better"/"big"/"black"/"certain"/"clear"/"different"/"early"/"easy"/"economic"/"federal"/"free"/"full"/"good"/"great"/"hard"/"high"/"human"/"important"/"international"/"large"/"late"/"little"/"local"/"long"/"low"/"major"/"military"/"national"/"new"/"old"/"only"/"other"/"political"/"possible"/"public"/"real"/"recent"/"right"/"small"/"social"/"special"/"strong"/"sure"/"true"/"white"/"whole"/"young"
        preposition = "about"/"above"/"according to"/"across"/"after"/"against"/"ago"/"ahead of"/"along"/"amidst"/"among"/"amongst"/"apart"/"around"/"as"/"as far as"/"as well as"/"aside"/"at"/"away"/"because of"/"before"/"behind"/"below"/"beneath"/"beside"/"besides"/"between"/"beyond"/"by"/"by means of"/"by way of"/"Close to"/"Despite"/"Down"/"Due to"/"During"/"Except"/"For"/"From"/"Hence"/"In"/"In accordance with"/"In addition to"/"In case of"/"In front of"/"In lieu of"/"In place of"/"In regard to"/"In spite of"/"In to"/"Inside"/"Instead of"/"Into"/"Like"/"Near"/"Next"/"Next to"/"Notwithstanding"/"Of"/"Off"/"On"/"On account of"/"On behalf of"/"On to"/"On top of"/"Onto"/"Opposite"/"Out"/"Out from"/"Out of"/"Outside"/"Over"/"Owing to"/"Past"/"Per"/"Prior to"/"Round"/"Since"/"Than"/"Through"/"Throughout"/"Till"/"To"/"Toward"/"Towards"/"Under"/"Underneath"/"Unlike"/"Until"/"Unto"/"Up"/"Upon"/"Via"/"With"/"With a view to"/"Within"/"Without"/"Worth"
        punctuation = "." / "," / ":" / "'" / "?" / "!" 
    """)

    my_grammar = str(grammar.parse(english))
    context = { "parse_grammar" : my_grammar,
                "num_of_sentences" : my_grammar.count("sentence"),
                "num_of_words" : my_grammar.count("word"),
                "num_of_spaces" : my_grammar.count("space"),
                "num_of_pronouns" : my_grammar.count("pronoun"),
                "num_of_nouns" : my_grammar.count("noun"),
                "num_of_verbs" : my_grammar.count("verb"),
                "num_of_adverbs" : my_grammar.count("adverb"),
                "num_of_adjectives" : my_grammar.count("adjective"),
                "num_of_prepositions" : my_grammar.count("preposition"),
                "num_of_puntation" : my_grammar.count("puntuation")
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
            return render(request, 'english_POS_project/dashboard.html', context)
        else:
            print('invalid')
    return render(request, 'english_POS_project/dashboard.html', {'file': form})

def submit_sentence(request):
    if request.method == 'POST':
        form = EnterInputForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['user_input']
            context = POS_grammar(text)
            return render(request, 'english_POS_project/dashboard.html', context)

    return render(request, 'english_POS_project/dashboard.html', {'text': form})