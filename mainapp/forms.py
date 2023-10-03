from django import forms

from mainapp.models import Product, Version

forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product

        fields = ('name', 'description', 'image_preview', 'category', 'price',)

    # def clean_field(self, field_name):
    #     cleaned_data = self.cleaned_data[field_name]
    #
    #     words = [word for word in forbidden_words if word.lower() in cleaned_data]
    #
    #     if words:
    #         raise forms.ValidationError(f'Запрещенные слова: {", ".join(words)}')
    #
    # def clean_name(self):
    #     return self.clean_field('name')
    #
    # def clean_description(self):
    #     return self.clean_field('description')


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version

        fields = '__all__'
