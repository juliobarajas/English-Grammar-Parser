from parsimonious.grammar import Grammar

grammar = Grammar ( r""" 
    sentence = (word / space / punctuation)+
    word = (pronoun / noun / verb / adverb / adjective / preposition)+
    space = ~" +" 
    pronoun = "I"/"another"/"anybody"/"anyone"/"anything"/"both"/"but"/"certain"/"either"/"enough"/"everybody"/"everyone"/"everything"/"extra"/"few"/"he "/"her "/"hers "/"herself"/"him"/"himself"/"his"/"hon"/"idem"/"it "/"itself"/"me"/"mine"/"my"/"myself"/"next"/"nobody"/"none"/"nothing"/"one"/"oneself"/"other"/"others"/"ours"/"ourselves"/"own"/"plenty"/"same"/"self"/"she"/"some"/"somebody"/"someone"/"something"/"somewhat"/"such"/"that"/"thee"/"theirs"/"them"/"themselves"/"these"/"they"/"thine"/"this"/"those"/"thou"/"thy"/"thyself"/"us"/"we"/"what"/"whatever"/"whatsoever"/"when"/"which"/"whichever"/"who"/"whoever"/"whom"/"whomever"/"whomsoever"/"whose"/"whoso"/"whosoever"/"ya"/"ye"/"you"/"your"/"yours"/"yourself"/"yourselves"
    noun = "Python"/"a "/"act"/"active"/"activity"/"age"/"air"/"amount"/"answer"/"anything"/"apple"/"area"/"arm"/"army"/"art"/"ask"/"attack"/"baby"/"back"/"bad"/"bag"/"ball"/"bank"/"base"/"basket"/"bath"/"bear"/"beautiful"/"bed"/"bedroom"/"beer"/"bell"/"big"/"bird"/"birth"/"birthday"/"bit"/"bite"/"black"/"block"/"blood"/"blow"/"blue"/"board"/"boat"/"body"/"bone"/"book"/"border"/"bottle"/"bottom"/"bowl"/"box"/"boy"/"branch"/"brave"/"bread"/"break"/"breakfast"/"bridge"/"brother"/"brown"/"brush"/"burn"/"business"/"bus"/"buy"/"cake"/"call"/"can"/"candle"/"cap"/"car"/"card"/"care"/"carry"/"case"/"cat"/"catch"/"chair"/"chance"/"change"/"chicken"/"child"/"chocolate"/"choice"/"city"/"class"/"clock"/"clothes"/"cloud"/"coffee"/"coat"/"cold"/"comfortable"/"common"/"computer"/"condition"/"control"/"cook"/"corner"/"cost"/"count"/"country"/"course"/"cover"/"crash"/"cross"/"cry"/"cup"/"cut"/"dance"/"dark"/"daughter"/"day"/"dead"/"deep"/"desk"/"dinner"/"direction"/"dish"/"dog"/"door"/"double"/"draw"/"dream"/"dress"/"drink"/"drive"/"drop"/"dust"/"duty"/"ear"/"earth"/"east"/"eat"/"education"/"effect"/"egg"/"end"/"equal"/"entrance"/"escape"/"evening"/"event"/"examination"/"example"/"exercise"/"eye"/"face"/"fact"/"fail"/"fall"/"family"/"farm"/"father"/"fat"/"fault"/"fear"/"feed"/"feel"/"female"/"few"/"fight"/"fill"/"film"/"finger"/"finish"/"fire"/"fish"/"fix"/"floor"/"flower"/"fly"/"fold"/"food"/"foot"/"football"/"force"/"form"/"freedom"/"friend"/"front"/"fruit"/"fun"/"funny"/"future"/"game"/"garden"/"gate"/"general"/"gift"/"give"/"glad"/"glass"/"go"/"god"/"gold"/"good"/"grandfather"/"grandmother"/"grass"/"great"/"green"/"ground"/"group"/"hair"/"half"/"hall"/"hand"/"hat"/"hate"/"head"/"heavy"/"heart"/"height"/"hello"/"help"/"hide"/"high"/"hit"/"hold"/"hole"/"holiday"/"home"/"hope"/"horse"/"hospital"/"hotel"/"house"/"hour"/"hurry"/"husband"/"hurt"/"ice"/"idea"/"if"/"increase"/"inside"/"iron"/"invite"/"island"/"it"/"job"/"join"/"juice"/"jump"/"keep"/"key"/"kill"/"kind"/"king"/"kitchen"/"knee"/"knife"/"ladder"/"lady"/"land"/"laugh"/"lead"/"leave"/"leg"/"length"/"lesson"/"let"/"letter"/"library"/"lie"/"life"/"light"/"lip"/"list"/"listen"/"lock"/"long"/"look"/"love"/"low"/"luck"/"machine"/"main"/"make"/"male"/"man"/"many"/"map"/"mark"/"market"/"matter"/"meal"/"meat"/"medicine"/"meet"/"member"/"mention"/"method"/"middle"/"milk"/"mind"/"minute"/"miss"/"mistake"/"mix"/"model"/"moment"/"money"/"month"/"morning"/"most"/"mother"/"mountain"/"mouth"/"move"/"music"/"name"/"nation"/"nature"/"neck"/"net"/"news"/"newspaper"/"night"/"noise"/"north"/"nose"/"nothing"/"notice"/"number"/"object"/"offer"/"office"/"oil"/"one"/"opposite"/"orange"/"order"/"other"/"outside"/"page"/"pain"/"paint"/"pair"/"paper"/"parent"/"park"/"part"/"partner"/"party"/"pass"/"past"/"path"/"pay"/"peace"/"pen"/"people"/"period"/"person"/"piano"/"pick"/"picture"/"piece"/"pin"/"place"/"plane"/"plant"/"plastic"/"plate"/"play"/"plenty"/"point"/"police"/"pool"/"position"/"possible"/"potato"/"power"/"present"/"press"/"price"/"private"/"prize"/"problem"/"produce"/"promise"/"public"/"pull"/"push"/"put"/"queen"/"question"/"quiet"/"radio"/"rain"/"raise"/"reach"/"read"/"record"/"red"/"remove"/"rent"/"repair"/"repeat"/"reply"/"report"/"rest"/"restaurant"/"result"/"return"/"rice"/"rich"/"ride"/"ring"/"rise"/"road"/"rock"/"room"/"round"/"rule"/"run"/"rush"/"sad"/"safe"/"sail"/"salt"/"sand"/"save"/"school"/"science"/"search"/"seat"/"second"/"sell"/"sentence"/"serve"/"sex"/"shake"/"shape"/"share"/"she"/"shine"/"ship"/"shirt"/"shoe"/"shoot"/"shop"/"shoulder"/"show"/"sick"/"side"/"signal"/"silly"/"silver"/"simple"/"single"/"sing"/"sink"/"sister"/"size"/"skill"/"skin"/"skirt"/"sky"/"sleep"/"slip"/"smell"/"smile"/"smoke"/"snow"/"sock"/"soft"/"son"/"sound"/"soup"/"south"/"space"/"special"/"speed"/"spell"/"spend"/"sport"/"spread"/"spring"/"square"/"stand"/"star"/"start"/"station"/"stay"/"steal"/"step"/"still"/"stomach"/"stop"/"store"/"storm"/"story"/"street"/"structure"/"student"/"study"/"stupid"/"subject"/"substance"/"sugar"/"summer"/"sun"/"support"/"surprise"/"sweet"/"swim"/"table"/"talk"/"taste"/"tea"/"teach"/"team"/"tear"/"telephone"/"television"/"tell"/"tennis"/"test"/"thing"/"tie"/"title"/"today"/"toe"/"tomorrow"/"tonight"/"tool"/"tooth"/"top"/"total"/"touch"/"town"/"train"/"travel"/"tree"/"trouble"/"trust"/"try"/"turn"/"type"/"uncle"/"unit"/"use"/"usual"/"vegetable"/"village"/"voice"/"visit"/"wait"/"wake"/"walk"/"wash"/"watch"/"water"/"way"/"wear"/"weather"/"wedding"/"week"/"weight"/"welcome"/"west"/"wheel"/"while"/"white"/"wife"/"will"/"win"/"wind"/"window"/"wine"/"winter"/"wish"/"woman"/"wonder"/"word"/"work"/"world"/"worry"/"yard"/"yesterday"/"you"/"young"/"two"  
    verb = "punch"/"love"/"be"/"have"/"know"/"see"/"want"/"do "/"take"/"use"/"provide"/"make"/"go"/"get"/"find"/"say"/"tell"/"support"/"need"/"give"/"help"/"include"/"come"/"work"/"ensure"/"improve"/"put"/"talk"/"increase"/"ask"/"keep"/"allow"/"reduce"/"call"/"receive"/"become"/"like"/"create"/"play"/"believe"/"promote"/"protect"/"change"/"live"/"leave"/"prevent"/"determine"/"let"/"meet"/"set"/"understand"/"develop"/"show"/"stop"/"try"/"look"/"consider"/"open"/"read"/"remain"/"offer"/"stay"/"pay"/"strengthen "/" form"/"start"/"establish"/"send"/"kill"/"achieve"/"bring"/"hear"/"wait"/"avoid"/"encourage"/"hope"/"add"/"think"/"follow"/"control"/"contribute"/"produce"/"maintain"/"speak"/"complete"/"choose"/"thank"/"obtain"/"buy"/"implement"/"listen"/"participate"/"address"/"require"/"share"/"enhance"/"save"/"wish"/"assist"/"note"/"enable"/"accept"/"contain"/"check"/"enjoy"/"serve"/"learn"/"indicate"/"die"/"move"/"build"/"represent"/"eat"/"hold"/"cover"/"forget"/"submit"/"prepare"/"select"/"discuss"/"apply"/"decide"/"access"/"research"/"finance"/"adopt"/"return "/" reach"/"explain"/"visit"/"remove"/"assess"/"feel"/"recognize"/"monitor"/"act"/"appear"/"generate"/"define"/"begin"/"inform"/"run"/"cut"/"lose"/"seek"/"write"/"respond"/"review"/"discover"/"watch"/"seem"/"respect"/"contact"/"guarantee"/"manage"/"benefit"/"reflect"/"comprise"/"enter"/"sell"/"spend"/"cause"/"win"/"perform"/"answer"/"express"/"replace"/"sleep"/"download"/"end"/"concern"/"operate"/"affect"/"eliminate"/"lead"/"examine"/"happen"/"turn"/"limit"/"view"/"communicate"/"report"/"vote"/"agree"/"raise"/"study"/"confirm"/"introduce"/"request"/"cooperate "/" imagine"/"collect"/"claim"/"conduct"/"prove"/"join"/"extend"/"explore"/"propose"/"describe"/"invite"/"treat"/"fight"/"hate"/"measure"/"detect"/"permit"/"close"/"recommend"/"demonstrate"/"deliver"/"equal"/"resolve"/"evaluate"/"fill"/"result"/"exceed"/"grow"/"carry"/"draw"/"solve"/"consult"/"wear"/"destroy"/"sign"/"target"/"suggest"/"expand"/"miss"/"fear"/"specify"/"defend"/"overcome"/"mean"/"appreciate"/"depend"/"exercise"/"welcome"/"vary"/"teach"/"walk"/"dry"/"transmit"/"remind"/"fix"/"focus"/"deal"/"preserve"/"break"/"realize"/"finish"
    adverb = "abnormally"/"absentmindedly"/"accidentally"/"actually"/"adventurously"/"afterwards"/"almost"/"always"/"annually"/"anxiously"/"arrogantly"/"awkwardly"/"bashfully"/"beautifully"/"bitterly"/"bleakly"/"blindly"/"blissfully"/"boastfully"/"boldly"/"bravely"/"briefly"/"brightly"/"briskly"/"broadly"/"busily"/"calmly"/"carefully"/"carelessly"/"cautiously"/"certainly"/"cheerfully"/"clearly"/"cleverly"/"closely"/"coaxingly"/"colorfully"/"commonly"/"continually"/"coolly"/"correctly"/"courageously"/"crossly"/"cruelly"/"curiously"/"daily"/"daintily"/"dearly"/"deceivingly"/"deeply"/"defiantly"/"deliberately"/"delightfully"/"diligently"/"dimly"/"doubtfully"/"dreamily"/"easily"/"elegantly"/"energetically"/"enormously"/"enthusiastically"/"equally"/"especially"/"even"/"evenly"/"eventually"/"exactly"/"excitedly"/"extremely"/"fairly"/"faithfully"/"famously"/"far"/"fast"/"fatally"/"ferociously"/"fervently"/"fiercely"/"fondly"/"foolishly"/"fortunately"/"frankly"/"frantically"/"freely"/"frenetically"/"frightfully"/"fully"/"furiously"/"generally"/"generously"/"gently"/"gladly"/"gleefully"/"gracefully"/"gratefully"/"greatly"/"greedily"/"happily"/"hastily"/"healthily"/"heavily"/"helpfully"/"helplessly"/"highly"/"honestly"/"hopelessly"/"hourly"/"hungrily"/"immediately"/"innocently"/"inquisitively"/"instantly"/"intensely"/"intently"/"interestingly"/"inwardly"/"irritably"/"jaggedly"/"jealously"/"jovially"/"joyfully"/"joyously"/"jubilantly"/"judgmentally"/"justly"/"keenly"/"kiddingly"/"kindheartedly"/"kindly"/"knavishly"/"knowingly"/"knowledgeably"/"kookily"/"lazily"/"less"/"lightly"/"likely"/"limply"/"lively"/"loftily"/"longingly"/"loosely"/"loudly"/"lovingly"/"loyally"/"madly"/"majestically"/"meaningfully"/"mechanically"/"merrily"/"miserably"/"mockingly"/"monthly"/"more"/"mortally"/"mostly"/"mysteriously"/"naturally"/"nearly"/"neatly"/"nervously"/"never"/"nicely"/"noisily"/"not"/"obediently"/"obnoxiously"/"oddly"/"offensively"/"officially"/"often"/"only"/"openly"/"optimistically"/"overconfidently"/"painfully"/"partially"/"patiently"/"perfectly"/"physically"/"playfully"/"politely"/"poorly"/"positively"/"potentially"/"powerfully"/"promptly"/"properly"/"punctually"/"quaintly"/"queasily"/"queerly"/"questionably"/"quicker"/"quickly"/"quietly"/"quirkily"/"quizzically"/"rightfully"/"randomly"/"rapidly"/"rarely"/"readily"/"really"/"reassuringly"/"recklessly"/"regularly"/"reluctantly"/"repeatedly"/"reproachfully"/"restfully"/"righteously"/"rigidly"/"roughly"/"rudely"/"safely"/"scarcely"/"scarily"/"searchingly"/"sedately"/"seemingly"/"seldom"/"selfishly"/"separately"/"seriously"/"shakily"/"sharply"/"sheepishly"/"shrilly"/"shyly"/"silently"/"sleepily"/"slowly"/"smoothly"/"softly"/"solemnly"/"solidly"/"sometimes"/"soon"/"speedily"/"stealthily"/"sternly"/"strictly"/"successfully"/"suddenly"/"supposedly"/"surprisingly"/"suspiciously"/"sweetly"/"swiftly"/"sympathetically"/"tenderly"/"tensely"/"terribly"/"thankfully"/"thoroughly"/"thoughtfully"/"tightly"/"tomorrow"/"too"/"tremendously"/"triumphantly"/"truly"/"truthfully"/"ultimately"/"unabashedly"/"unaccountably"/"unbearably"/"unethically"/"unexpectedly"/"unfortunately"/"unimpressively"/"unnaturally"/"unnecessarily"/"upbeat"/"upright"/"upside-down"/"upward"/"urgently"/"usefully"/"uselessly"/"usually"/"utterly"/"vacantly"/"vaguely"/"vainly"/"valiantly"/"vastly"/"verbally"/"very"/"viciously"/"victoriously"/"violently"/"vivaciously"/"voluntarily"/"warmly"/"weakly"/"wearily"/"well"/"wetly"/"wholly"/"wildly"/"willfully"/"wisely"/"woefully"/"wonderfully"/"worriedly"/"wrongly"/"yawningly"/"yearly"/"yearningly"/"yesterday"/"yieldingly"/"youthfully"/"zealously"/"zestfully"/"zestily"
    adjective = "able"/"bad"/"best"/"better"/"big"/"black"/"certain"/"clear"/"different"/"early"/"easy"/"economic"/"federal"/"free"/"full"/"good"/"great"/"hard"/"high"/"human"/"important"/"international"/"large"/"late"/"little"/"local"/"long"/"low"/"major"/"military"/"national"/"new"/"old"/"only"/"other"/"political"/"possible"/"public"/"real"/"recent"/"right"/"small"/"social"/"special"/"strong"/"sure"/"true"/"white"/"whole"/"young"
    preposition = "about"/"above"/"according to"/"across"/"after"/"against"/"ago"/"ahead of"/"along"/"amidst"/"among"/"amongst"/"apart"/"around"/"as"/"as far as"/"as well as"/"aside"/"at"/"away"/"because of"/"before"/"behind"/"below"/"beneath"/"beside"/"besides"/"between"/"beyond"/"by"/"by means of"/"by way of"/"Close to"/"Despite"/"Down"/"Due to"/"During"/"Except"/"For"/"From"/"Hence"/"In"/"In accordance with"/"In addition to"/"In case of"/"In front of"/"In lieu of"/"In place of"/"In regard to"/"In spite of"/"In to"/"Inside"/"Instead of"/"Into"/"Like"/"Near"/"Next"/"Next to"/"Notwithstanding"/"Of"/"Off"/"On"/"On account of"/"On behalf of"/"On to"/"On top of"/"Onto"/"Opposite"/"Out"/"Out from"/"Out of"/"Outside"/"Over"/"Owing to"/"Past"/"Per"/"Prior to"/"Round"/"Since"/"Than"/"Through"/"Throughout"/"Till"/"To"/"Toward"/"Towards"/"Under"/"Underneath"/"Unlike"/"Until"/"Unto"/"Up"/"Upon"/"Via"/"With"/"With a view to"/"Within"/"Without"/"Worth"
    punctuation = "." / "," / ":" / "'" / "?" / "!" 
""")

print (grammar.parse("I hope after today I will love python."))
    
