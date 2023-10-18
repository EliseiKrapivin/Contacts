from django.views.generic import ListView
from .models import Contact
from django.views.generic.edit import CreateView

class ContactAdd(CreateView):
    model = Contact
    template_name = 'contacts/post_list.html'
    context_object_name = 'contacts'
    
    """def form_valid(self, form):
        feilds = form.save(commit=False)
        feilds.name = self.request.user
        feilds.second_name = self.request.user
        feilds.surname = self.request.user
        feilds.phone_number = self.request.user
        feilds.email = self.request.user
        feilds.photo = self.request.user
        feilds.birthday = self.request.user
        feilds.save()
        return super().form_valid(form)"""

class ContactList(ListView):
    model = Contact
    template_name = 'contacts/post_list.html'
    context_object_name = 'contacts'

class ContactView(ListView):
    model = Contact
    template_name = 'contacts/post_list.html'
    context_object_name = 'contacts'