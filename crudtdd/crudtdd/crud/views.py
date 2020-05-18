from core.baseview import baseListView
from .models import list_Model
class List(baseListView):
    template_name = 'mian.html'
    model = list_Model


