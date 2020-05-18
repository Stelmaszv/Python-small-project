from core.baseview import baseListView,baseShowView
from .models import list_Model
class List(baseListView):
    template_name = 'mian.html'
    def setContext(self, request):
        self.context = {
            'list': list_Model.objects.all()
        }
class Get(baseShowView):
    template_name = 'get.html'
    getObject = list_Model




