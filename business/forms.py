from django.forms import ModelForm
from .models import sell_goods

class sell_frm(ModelForm):
    class Meta:
        model = sell_goods
        fields = ('itemdesc','price' , 'itemimg')
        widgets = {
            'itemdesc':attr({"name":"Description"})
        }
