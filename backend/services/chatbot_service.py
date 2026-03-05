from sqlalchemy.orm import Session
from backend.schemas.chatbot import ChatMessageRequest
from backend.db.models import User, ChatLog

# Hardcoded translations for mock responses
BOT_RESPONSES = {
    "en": {
        "weather": "Based on current forecasts, there's a 30% chance of rain tomorrow. I recommend delaying pesticide application.",
        "tomato": "For early blight in tomatoes, consider applying a copper-based fungicide and ensure good air circulation.",
        "price": "Market prices for wheat are currently stable. If your storage moisture is below 12%, holding could yield better margins next month.",
        "greeting": "Hello {name}! How can I assist you with your crops today?",
        "fallback": "I'm still learning about that topic. Could you provide more specific details about the crop or condition?"
    },
    "hi": {
        "weather": "वर्तमान पूर्वानुमान के आधार पर, कल बारिश की 30% संभावना है। मेरा सुझाव है कि कीटनाशक के छिड़काव में देरी करें।",
        "tomato": "टमाटर में अगेती अंगमारी के लिए, तांबे-आधारित कवकनाशी लगाने पर विचार करें और अच्छी हवा का संचार सुनिश्चित करें।",
        "price": "गेहूं के बाजार मूल्य वर्तमान में स्थिर हैं। यदि आपके भंडारण की नमी 12% से कम है, तो होल्ड करने से अगले महीने बेहतर मार्जिन मिल सकता है।",
        "greeting": "नमस्ते {name}! आज मैं आपकी फसलों के संबंध में आपकी कैसे सहायता कर सकता हूँ?",
        "fallback": "मैं अभी भी उस विषय के बारे में सीख रहा हूँ। क्या आप फसल या स्थिति के बारे में अधिक विशिष्ट विवरण प्रदान कर सकते हैं?"
    },
    "or": {
        "weather": "ବର୍ତ୍ତମାନର ପୂର୍ବାନୁମାନ ଆଧାରରେ, ଆସନ୍ତାକାଲି ବର୍ଷା ହେବାର 30% ସମ୍ଭାବନା ଅଛି | ମୁଁ କୀଟନାଶକ ପ୍ରୟୋଗକୁ ବିଳମ୍ବ କରିବାକୁ ପରାମର୍ଶ ଦେଉଛି |",
        "tomato": "ଟମାଟୋରେ ପ୍ରାରମ୍ଭିକ ବ୍ଲାଇଟ୍ ପାଇଁ, ତମ୍ବା ଭିତ୍ତିକ ଫଙ୍ଗିସାଇଡ୍ ପ୍ରୟୋଗ କରିବାକୁ ବିଚାର କରନ୍ତୁ ଏବଂ ଭଲ ବାୟୁ ଚଳାଚଳ ନିଶ୍ଚିତ କରନ୍ତୁ |",
        "price": "ଗହମ ପାଇଁ ବଜାର ମୂଲ୍ୟ ବର୍ତ୍ତମାନ ସ୍ଥିର ଅଟେ | ଯଦି ଆପଣଙ୍କର ଷ୍ଟୋରେଜ୍ ଆର୍ଦ୍ରତା 12% ରୁ କମ୍, ଧରି ରଖିବା ଆସନ୍ତା ମାସରେ ଭଲ ଲାଭ ଦେଇପାରେ |",
        "greeting": "ନମସ୍କାର {name}! ଆଜି ମୁଁ ତୁମର ଫସଲ ସହିତ କିପରି ସାହାଯ୍ୟ କରିପାରିବି?",
        "fallback": "ମୁଁ ଏବେ ବି ସେହି ବିଷୟ ବିଷୟରେ ଶିଖୁଛି | ଆପଣ ଫସଲ କିମ୍ବା ଅବସ୍ଥା ବିଷୟରେ ଅଧିକ ନିର୍ଦ୍ଦିଷ୍ଟ ବିବରଣୀ ପ୍ରଦାନ କରିପାରିବେ କି?"
    },
    "te": {
        "weather": "ప్రస్తుత సూచనల ఆధారంగా, రేపు వర్షం పడటానికి 30% అవకాశం ఉంది. పురుగుమందుల దరఖాస్తును ఆలస్యం చేయాలని నేను సిఫార్సు చేస్తున్నాను.",
        "tomato": "టమోటాలలో ప్రారంభ ముడత కోసం, రాగి ఆధారిత శిలీంద్ర సంహారిణిని వర్తింపజేయండి మరియు మంచి గాలి ప్రసరణను నిర్ధారించుకోండి.",
        "price": "గోధుమలకు మార్కెట్ ధరలు ప్రస్తుతం స్థిరంగా ఉన్నాయి. మీ నిల్వ తేమ 12% కంటే తక్కువగా ఉంటే, పట్టుకోవడం వచ్చే నెలలో మంచి లాభాలను ఇస్తుంది.",
        "greeting": "నమస్తే {name}! ఈ రోజు మీ పంటలతో నేను మీకు ఎలా సహాయం చేయగలను?",
        "fallback": "నేను ఇప్పటికీ ఆ విషయం గురించి నేర్చుకుంటున్నాను. మీరు పంట లేదా పరిస్థితి గురించి మరింత నిర్దిష్ట వివరాలను అందించగలరా?"
    },
    "ta": {
        "weather": "தற்போதைய முன்னறிவிப்புகளின் அடிப்படையில், நாளை 30% மழை பெய்ய வாய்ப்புள்ளது. பூச்சிக்கொல்லி பயன்பாட்டை தாமதப்படுத்த நான் பரிந்துரைக்கிறேன்.",
        "tomato": "தக்காளியில் ஆரம்ப நிலையற்ற தன்மைக்கு, தாமிரம் கலந்த பூஞ்சைக் கொல்லியைப் பயன்படுத்துவதைக் கருத்தில் கொள்ளவும், நல்ல காற்று சுழற்சியை உறுதி செய்யவும்.",
        "price": "கோதுமைக்கான சந்தை விலைகள் தற்போது நிலையானவை. உங்கள் சேமிப்பகத்தின் ஈரப்பதம் 12% க்கும் குறைவாக இருந்தால், அடுத்த மாதம் சிறந்த லாபத்தை ஈட்ட முடியும்.",
        "greeting": "வணக்கம் {name}! இன்று உங்கள் பயிர்களுக்கு நான் எவ்வாறு உதவ முடியும்?",
        "fallback": "அந்தத் தலைப்பைப் பற்றி நான் இன்னும் கற்றுக் கொண்டிருக்கிறேன். பயிர் அல்லது நிலைமை பற்றி இன்னும் விரிவான விவரங்களை வழங்க முடியுமா?"
    },
    "bn": {
        "weather": "বর্তমান পূর্বাভাস অনুসারে, আগামীকাল বৃষ্টির ৩০% সম্ভাবনা রয়েছে। আমি কীটনাশক প্রয়োগ বিলম্বিত করার পরামর্শ দিচ্ছি।",
        "tomato": "টমেটোতে আর্লি ব্লাইটের জন্য কপার-ভিত্তিক ছত্রাকনাশক প্রয়োগ করার কথা বিবেচনা করুন এবং ভালো বায়ু চলাচল নিশ্চিত করুন।",
        "price": "গমের বাজার মূল্য বর্তমানে স্থিতিশীল। যদি আপনার সংরক্ষণের আর্দ্রতা ১২% এর কম হয়, তবে ধরে রাখলে আগামী মাসে আরও ভালো লাভ হতে পারে।",
        "greeting": "নমস্কার {name}! আজ আপনার ফসলের বিষয়ে আমি কীভাবে আপনাকে সহায়তা করতে পারি?",
        "fallback": "আমি এখনও এই বিষয়টি সম্পর্কে শিখছি। আপনি কি ফসল বা অবস্থা সম্পর্কে আরও নির্দিষ্ট বিবরণ প্রদান করতে পারেন?"
    }
}


def process_chat_message(db: Session, user: User, request: ChatMessageRequest) -> tuple[ChatLog, ChatLog]:
    """
    Process incoming user message, generate a mock AI response, 
    and save both to the database.
    Returns: a tuple of (user_log, bot_log).
    """
    
    # 1. Save User Message
    user_log = ChatLog(
        user_id=user.id,
        message_text=request.message,
        is_bot=False
    )
    db.add(user_log)
    
    # 2. Generate Mock AI Response based on keywords
    msg_lower = request.message.lower()
    
    # Get user language, fallback to english
    lang = user.language if user.language in BOT_RESPONSES else "en"
    responses = BOT_RESPONSES[lang]
    
    # Basic keyword matching (in reality this would be an LLM call)
    # The matching is done in english mostly for simplicity in this mock, 
    # but could be improved to check keywords in targeted languages.
    if "weather" in msg_lower or "rain" in msg_lower or "मौसम" in msg_lower or "बारीश" in msg_lower:
        bot_reply = responses["weather"]
    elif "tomato" in msg_lower or "blight" in msg_lower or "टमाटर" in msg_lower:
        bot_reply = responses["tomato"]
    elif "price" in msg_lower or "sell" in msg_lower or "कीमत" in msg_lower:
        bot_reply = responses["price"]
    elif "hello" in msg_lower or "hi" in msg_lower or "नमस्ते" in msg_lower or "namaste" in msg_lower:
        name = user.full_name or ('Farmer' if lang == 'en' else 'किसान')
        bot_reply = responses["greeting"].replace("{name}", name)
    else:
        bot_reply = responses["fallback"]
        
    # 3. Save Bot Response
    bot_log = ChatLog(
        user_id=user.id,
        message_text=bot_reply,
        is_bot=True
    )
    db.add(bot_log)
    
    db.commit()
    db.refresh(user_log)
    db.refresh(bot_log)
    
    return user_log, bot_log
