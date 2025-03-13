from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, "firstpage.html")

def play(request):
    return render(request, "gamepage.html")

def open_level1(request, level):
    return render(request, f'level{level}.html')

def question_page(request, level, question):
    total = 3

    qlinks = [{"number":i, 'url':f'level/{level}/question/{i}'} for i in range(1, total+1)]

    return render(request, f'level_{level}/question{question}.html', {
        'level': level,
        'question': question,
        'qlinks': qlinks,
    })

@csrf_exempt
def track_tab_switch(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        print(f"Tab switched {data['count']} times.")
        return JsonResponse({"status": "success"})
    return JsonResponse({"error": "Invalid request"}, status=400)