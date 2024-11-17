# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .compiler import lexical_analysis # Importa tu lexer

def editor(request):
    return render(request, 'editor.html')

def analyze_code(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        # Llama al análisis léxico con el código directamente
        result = lexical_analysis(code)
        return JsonResponse({'tokens': result})

    return JsonResponse({'error': 'Invalid request'}, status=400)
