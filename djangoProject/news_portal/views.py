from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'news_portal/home.html')

def scienceNews(request):
    news_head='Science News'
    new_msg1='The Moon is drifting away from the Earth.'
    new_msg2='Earth has a squishy interior.'
    new_msg3='Nearly all large galaxies are thought to contain supermassive black holes at their centers'
    my_dict={'news_head':news_head, 'new_msg1':new_msg1, 'new_msg2':new_msg2, 'new_msg3':new_msg3}
    return render(request, 'news_portal/news.html', context=my_dict)


def politicsNews(request):
    news_head='Politics News'
    new_msg1='Senate Passes Historic Infrastructure Bill to Revamp National Transportation Network'
    new_msg2='Government Announces New Climate Policy Aimed at Reducing Carbon Emissions by 50 percent by 2030.'
    new_msg3='International Summit Focuses on Global Health Equity and Vaccine Distribution'
    my_dict={'news_head':news_head, 'new_msg1':new_msg1, 'new_msg2':new_msg2, 'new_msg3':new_msg3}
    return render(request, 'news_portal/news.html', context=my_dict)

def sportsNews(request):
    news_head='Sports News'
    new_msg1='Serena Williams Announces Retirement After US Open'
    new_msg2='Lionel Messi Scores Stunning Goal in PSG\'s Victory Over Marseille.'
    new_msg3='LeBron James Leads Lakers to Preseason Win Against Golden State Warriors.'
    my_dict={'news_head':news_head, 'new_msg1':new_msg1, 'new_msg2':new_msg2, 'new_msg3':new_msg3}
    return render(request, 'news_portal/news.html', context=my_dict)