from django.forms import ModelForm
from myapp.models import Expense


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

