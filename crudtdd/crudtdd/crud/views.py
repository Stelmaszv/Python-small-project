from core.baseview import baseListView,baseShowView,baseCreate
from .models import list_Model
from .forms import list_Form
class List(baseListView):
    template_name = 'mian.html'
    def setContext(self, request):
        self.context = {
            'list': list_Model.objects.all()
        }
class Get(baseShowView):
    template_name = 'get.html'
    getObject = list_Model
class Create(baseCreate):
    template_name = 'create.html'
    form = list_Form
    success_url = '/'



