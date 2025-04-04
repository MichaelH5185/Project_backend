from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import zipcode, Alert
from .loc import get_code
import requests
import re
import json

def home(request):
    if request.method == 'POST':
        code = request.POST.get('zipcode')
        try:
            zipcode.objects.get(znum=code)
            return redirect('alert', pk=code)
        except:
            zipn = zipcode.objects.create(
                znum = code,
                wcode = get_code(int(code))
            )
            return redirect('alert', pk=code)
    return render(request, 'alerts/home.html')
# Create your views here.
def fetch_data(url):
    header = {"User-Agent" : "(DEWapp, mjhf89@umsystem.edu)"}
    try:
        res = requests.get(url, headers=header)
        res.raise_for_status()
        return res
    except:
        return 0
def check_val(val):
    if val == None:
        return "None Provided"
    return val
def alert(request, pk):
    zipc = get_object_or_404(zipcode, znum=int(pk))
    zipc.wcode = get_code(int(pk))
    components = list(zipc.wcode)
    alt_code = str(components[0])+str(components[1])+"C"+str(components[3])+str(components[4])+str(components[5])
    #print(alt_code)
    alerts_page = fetch_data("https://api.weather.gov/alerts/active?area="+str(components[0])+str(components[1]))
    alerts = None
    if alerts_page != 0:
        page = alerts_page.text
        n_urls = re.findall(r"\"\@id\"\: \"[a-z,A-Z,0-9,.,:,\/]+\"", page)
        for u in n_urls:
            u_json = '{'+u+'}'
            x = json.loads(u_json)
            #print(x)
            info = fetch_data(x["@id"])
            if info != 0:
                info = str(info.text)
                affected = re.findall(r"[A-Z]{3}[0-9]{3}", info)
                if str(zipc.wcode) in affected or str(alt_code) in affected:
                    #print("hello")
                    y = json.loads(info)
                    props = y["properties"]
                    try:
                        instructs = check_val(props["instruction"])
                        head = check_val(props["headline"])
                        desc = check_val(props["description"])
                        end = check_val(props["expires"])
                        sev = check_val(props["severity"])
                        event = check_val(props["event"])
                        n_a = Alert.objects.create(
                            headline = head,
                            description = desc,
                            ref_url = zipc,
                            ends = end,
                            instruct = instructs,
                            severity = sev,
                            event = event,
                        )
                        #print("success")
                    except:
                        print("failure")
        alerts = zipc.alert_set.all()
    print(len(alerts))
    context = {'zcode':zipc, 'alerts':alerts}
    return render(request, 'alerts/alerts.html',context)

def delete_alerts(request, pk):
    zipc = get_object_or_404(zipcode, znum=int(pk))
    alerts = zipc.alert_set.all()
    for alert in alerts:
        alert.delete()
    return redirect('home')