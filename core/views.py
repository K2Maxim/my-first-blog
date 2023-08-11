from django.shortcuts import render
from .controllers import entities, payments


# Create your views here.
def index(request):
    return render(request, "gto/index.html")

(
    entity_added,
    entity_updated,
    payment_list,
    receipt,
) = (
    entities.entity_added,
    entities.entity_updated,
    payments.payment_list,
    payments.receipt,
)
