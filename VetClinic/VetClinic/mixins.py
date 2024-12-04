from django import forms


class FormFieldsUpdateMixin(forms.Form):

    custom_keyword = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'name': field + '_' + self.custom_keyword,
                'id': field + '_' + self.custom_keyword,
            })