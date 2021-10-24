from django.http import JsonResponse
from random import sample, uniform, randint
from .models import (
    Patient,
    Inferma,
    Evidence,
    Doctor,
    Diagnostic,
    Test
)
from .infermedica import (
    init_inf,
    diagnosis_req_to_if,
    get_specialist
)

from .utils import (
    all_tests,
    specialists,
    test_values
)

# Create your views here.
def init(request):
    name = request.GET.get("name")
    age = int(request.GET.get("age"))
    sex = request.GET.get("sex")
    height = float(request.GET.get("height"))
    weight = float(request.GET.get("weight"))
    street = request.GET.get("street")
    city = request.GET.get("city")
    phone = request.GET.get("phone")
    text = request.GET.get("text")

    print(city)

    patient = Patient.objects.create(
        name = name,
        age = age,
        sex = sex,
        height = height,
        weight = weight,
        street = street,
        city = city,
        phone = phone
    )
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
        return JsonResponse({
            'key': key,
            'complete': True,
            'specialization': specialist
        })

def get_tests(request):
    key = request.GET.get('key')
    specialization = request.GET.get('specialist')
    address = Inferma.objects.get(key=key).patient.city.title()
    lst = specialists.get(address.title()).get(specialization.lower())
    return JsonResponse({
        'key': key,
        'tests': all_tests.get(specialization.lower()),
        'specialists': sample(lst, min(len(lst), 5))
    })

def set_specialist(request):
    key = request.GET.get('key')
    patient = Inferma.objects.get(key=key).patient
    doctor_key = request.GET.get('doctor')
    doctor = Doctor.objects.get(key=doctor_key)
    Diagnostic.objects.create(
        patient = patient,
        doctor = doctor
    )

    return JsonResponse({
        'success': True
    })

def get_patient_data(request):
    key = request.GET.get('key')
    doctor = Doctor.objects.get(key=key)
    diagnostics = doctor.diagnostics.all()
    lst = []
    for diagnostic in diagnostics:
        patient = diagnostic.patient.serialize()
        patient['emergency'] = diagnostic.emergency
        tests = diagnostic.tests.all().order_by('-time')
        patient['tests'] = dict()
        for test in tests:
            if patient['tests'].get(test.name):
                patient['tests'][test.name].append(test.serialize())
            else:
                patient['tests'][test.name] = []
                patient['tests'][test.name].append(test.serialize())
        lst.append(patient)
    return JsonResponse(lst, safe=False)

def randomize(request):
    lst = []
    for patient in Patient.objects.all():
        diagnostic = patient.diagnostics.first()
        specialization = diagnostic.doctor.department
        tests = all_tests[specialization]
        for test in tests:
            values = test_values[test]
            if isinstance(values['pot_max'], int):
                value = randint(values['pot_min'], values['pot_max'])
            else:
                value = round(uniform(values['pot_min'], values['pot_max']), 1)
            Test.objects.create(
                name = test,
                value = value,
                unit = values['unit'],
                diagnostic = diagnostic
            )

    
    return JsonResponse({
        'success': True
    })