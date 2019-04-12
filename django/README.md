- Django Admin docs generation builtin
```
Add 'django.contrib.admindocs', in INSTALLED_APPS
In urls,                   
    path('admin/doc/', include('django.contrib.admindocs.urls')),

```
- location field (co-ordinates) for map

### Pass request to django form

```
admin.py
class GroupAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        FooForm = super(GroupAdmin, self).get_form(request, obj, **kwargs)

        class RequestFooForm(FooForm):
            def __new__(cls, *args, **kwargs):
                kwargs['request'] = request
                return FooForm(*args, **kwargs)

        return RequestFooForm
    form = GroupAdminForm
    search_fields = ('name',)
    ordering = ('name',)

```

```
forms.py
class GroupAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        self.fields['permissions'].queryset = get_permissions(request)

    permissions = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=widgets.FilteredSelectMultiple(_('permissions'), False))

    def clean(self):
        data = self.cleaned_data
        if not data['name'].isupper():
            data['name'] = data['name'].title()

    class Meta:
        model = Group
        fields = ['name', 'permissions']
```
