from django.http import JsonResponse
from random import sample
from .models import (
    Patient,
    Inferma,
    Evidence,
    Specialist
)
from .infermedica import (
    init_inf,
    diagnosis_req_to_if,
    get_specialist
)

from .utils import (
    all_tests,
    specialists
)

# Create your views here.
def init(request):
    if request.method != "GET":
        return JsonResponse({
            "data": "Sorry not found"
        }, status=400)
    

    name = request.GET.get("name")
    age = int(request.GET.get("age"))
    sex = request.GET.get("sex")
    text = request.GET.get("text")

    patient = Patient.objects.create(name=name, age=age, sex=sex)
    response = init_inf(age=age, sex=sex, text=text)
    inferma = Inferma.objects.create(patient=patient)

    for evidence in response['evidence']:
        Evidence.objects.create(
            inferma = inferma, 
            evidence_id = evidence['id'], 
            choice_id = evidence['choice_id'],
            initial = False
        )
    
    response = diagnosis_req_to_if(response)
    key = inferma.key


    if not response['should_stop']:
        Evidence.objects.create(
            inferma = inferma,
            evidence_id = response['question']['items'][0]['id'],
            choice_id = None,
            initial = False
        )
        return JsonResponse({
            "key": key,
            "complete": False,
            "question": response["question"]["text"],
            "choices": response['question']['items'][0]['choices']
        })

def continue_query(request):
    key = request.GET.get('key')
    inferma = Inferma.objects.get(key=key)

    patient = inferma.patient

    choice = request.GET.get('choice')
    last_ev = inferma.evidences.get(choice_id=None)
    last_ev.choice_id = choice
    last_ev.save()

    evidences = inferma.evidences.all()

    data = {
        "sex": patient.sex,
        "age": {
            "value": patient.age
        },
        "evidence": [i.serialize() for i in evidences]
    }

    response = diagnosis_req_to_if(data)
    
    if not (response.get('should_stop') or response.get("has_emergency_evidence") or evidences.count() > 10):
        try:
            Evidence.objects.create(
                inferma = inferma,
                evidence_id = response['question']['items'][0]['id'],
                choice_id = None,
                initial = False
            )
        except:
            response = get_specialist(data)
            specialist = response['recommended_specialist']['name']
            try:
                spec = Specialist.objects.get(name=specialist)
            except:
                spec = Specialist.objects.create(name=specialist)
            patient.specialist = spec
            patient.save()
            return JsonResponse({
                'key': key,
                'complete': True,
                'specialization': specialist
            })
        return JsonResponse({
            "key": key,
            "complete": False,
            "question": response["question"]["text"],
            "choices": response['question']['items'][0]['choices']
        })
    else:
        response = get_specialist(data)
        specialist = response['recommended_specialist']['name']
        try:
            spec = Specialist.objects.get(name=specialist)
        except:
            spec = Specialist.objects.create(name=specialist)
        patient.specialist = spec
        patient.save()
        return JsonResponse({
            'key': key,
            'complete': True,
            'specialization': specialist
        })

def get_tests(request):
    specialization = request.GET.get('specialist')
    address = request.GET.get('address')
    lst = specialists.get(address.lower()).get(specialization.lower())
    return JsonResponse({
        'tests': all_tests.get(specialization.lower()),
        'specialists': sample(lst, min(len(lst), 5))
    })