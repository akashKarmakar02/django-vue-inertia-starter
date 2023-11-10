import json
from inertia import inertia

from demo.form import TestForm
from demo.models import Test


@inertia('index')
def index(request):
    if request.method == "POST":
        data: dict = json.load(request)
        test = TestForm(data)
        if test.is_valid():
            test.save()

    return {
        'name': 'Akash'
    }
