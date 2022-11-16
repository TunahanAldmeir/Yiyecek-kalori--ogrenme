from django.shortcuts import render
import requests
import json
# Create your views here.
def Food(request):
    
    if request.method == 'POST':
        query=request.POST.get('query')
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        response = requests.get(api_url, headers={'X-Api-Key': 'your api key'})
        try:
            api=json.loads(response.content)
        except Exception as e:
            api="There was an error"
        return render(request,'Home.html',{'api':api})  
    else:                
        return render(request,'Home.html',{'query': 'Enter a valid search word'})
        

    
    