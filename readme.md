# Pitt-Challenge Backend Repository

**Team UofT_Phoenix**'s backend repository for [Pitt Challenge 2021](https://pittchallenge.com/).

### Database Schema

| Patient | Table to keep patient information ||
| --- | --- | --- |
| name | string | Name of the patient |
| age | integer | Age of the patient |
| sex | string | Sex of the patient (male/female/others) |
| height | float | Height of the patient (in meter) |
| weight | float | Weight of the patient (in kg) |
| street | string | The street where patient lives in |
| city | string | Specific boroughs and neighborhoods of New York |
| phone | string | Contact No. of the patient |




| Inferma | Table to manage chat history with patient ||
| --- | --- | --- |
| patient | one-to-one with a row in 'Patient' | To track the user |
| key | string (uuid4) | Used by chatbot to call API |




| Evidence | Table to store symptoms ||
| --- | --- | --- |
| inferma | foreignkey to a row in 'Inferma' | To track user chats |
| evidence id | string | ID provided by infermedica api |
| choice_id | string | Present/Absent/Unknown |
| initial | bool | Whether the symptom was mentioned by user themselves or not |




| Doctor | Table to keep doctor information ||
| --- | --- | --- |
| key | string | ID to track a doctor |
| name | string | Name of the doctor |
| department | string | Specialization of the doctor |
| city | string | Specific boroughs and neighborhoods of New York |
| email | string | Generated email address of the doctor |




| Diagnostic | Table to establish patient-doctor relation ||
| --- | --- | --- |
| patient | foreignkey to a row in 'Patient' | To track the patient |
| doctor | foreignkey to a row in 'Doctor' | To track the doctor |
| emergency | bool | Whether the patient has emergency situation or not |




| Test | Table to track tests done by patient ||
| --- | --- | --- |
| name | string | Name of the test |
| value | float | Test value |
| unit | string | Test unit |
| diagnostic | foreignkey to a row in 'Diagnostic' | To track patient |
| time | datetime | Time of the test |



### Api Calls

`/init`: Initialize chat
**Method**: GET
**Params**:

* name
* age
* sex
* height
* weight
* street
* city: Bronx, Brooklyn, Cedarhurst, Flushing, Jackson Heights, Manhattan, New York, Queens, Staten Island
* phone

**Response**:

```json
{
    "key": "string",
    "complete": "bool",
    "question": "string",
    "choices": [
        {
            "id": "string",
            "label": "string"
        }
    ]
}
```



`/continue`: Continue initialized chat

**Method**: GET

**Params**:

* key: Key received via `init` API
* choice: present/absent/unknown

**Response**

```json
{
    "key": "string",
    "complete": false,
    "question": "string",
    "choices": [
        {
            "id": "string",
            "label": "string"
        }
    ]
}
```



```json
{
    "key": "string",
    "complete": true,
    "specialization": "string"
}
```



`/get-tests`: Get test and doctor suggestion

**Method**: GET

**Params**:

* key: Key received via `init` API
* specialist: Specialization name received via `continue` API

**Response**:

```json
{
    "key": "string",
    "tests": [
   		"string"
    ],
    "specialists": [
        {
        "id": "string",
        "name": "string",
        "address": "string",
        "email": "string"
        }
    ]
}
```



`/appoint`: Confirm doctor selection

**Method**: GET

**Params**:

* key: Key received via `init` API
* doctor: Doctor's ID received via `get-tests` API

**Response**:

```json
{
	"success": "bool"
}
```



`/get-patient-data`: Called from doctor's view

**Method**: GET

**Params**: 

* key: Doctor's ID

**Response**:

```json
[
    {
        "name": "string",
        "age": "int",
        "sex": "string",
        "height": "float",
        "weight": "int",
        "phone": "string",
        "key": "string", //patient key from init api
        "emergency": "bool",
        "tests": {
        "Test Name": [
                {
                    "value": "int",
                    "unit": "string",
                    "date": "string", // "01 Jan, 1968"
                    "time": "string" // "14:20"
                }
            ]
        }
	}
]
```



`/toggle-emergency`: To mark/unmark a patient as emergency

**Method**: GET

**Params**:

* key: Patient key received via `init` API

**Response**:

```json
{
	"success": "bool"
}
```

