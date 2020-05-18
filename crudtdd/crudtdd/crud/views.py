from core.baseview import baseListView
from .models import list_Model
class List(baseListView):
    template_name = 'mian.html'
    def setContext(self, request):
        self.context = {
            'list': list_Model.objects.all()
        }


