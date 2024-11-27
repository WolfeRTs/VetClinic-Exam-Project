from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from rest_framework.reverse import reverse_lazy

from VetClinic.images.choices import ImageCategoryChoices
from VetClinic.images.forms import ImageAddForm, ImageEditForm
from VetClinic.images.models import Image

UserModel = get_user_model()


class ImageAddView(CreateView):
    model = Image
    template_name = 'images/image-add.html'
    form_class = ImageAddForm
    success_url = reverse_lazy('gallery')


class ImageEditView(UpdateView):
    model = Image
    template_name = 'images/image-edit.html'
    form_class = ImageEditForm
    success_url = reverse_lazy('gallery')


class ImageDeleteView(DeleteView):
    model = Image
    template_name = 'images/image-delete.html'
    success_url = reverse_lazy('gallery')

    def get_object(self, queryset=None):
        return Image.objects.get(id=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        image = self.get_object()
        image.delete()
        return redirect(self.get_success_url())


class ImageDetailsView(DetailView):
    model = Image
    template_name = 'images/image-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['previous_image'] = self.object.get_next_by_date_uploaded()
        except Image.DoesNotExist:
            context['previous_image'] = None

        try:
            context['next_image'] = self.object.get_previous_by_date_uploaded()
        except Image.DoesNotExist:
            context['next_image'] = None
        return context


class GalleryView(ListView):
    model = Image
    context_object_name = 'images'
    paginate_by = 12

    def get_queryset(self):
        if self.request.user.groups.filter(name='Veterinarian').exists():
            category = self.request.GET.get('category', 'all')
            if category == 'all':
                return Image.objects.all().order_by('-date_uploaded')
            return Image.objects.filter(category=category).order_by('-date_uploaded')
        else:
            return Image.objects.filter(category=ImageCategoryChoices.GALLERY).order_by('-date_uploaded')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.groups.filter(name='Veterinarian').exists():
            context['categories'] = ImageCategoryChoices.choices
            context['selected_category'] = self.request.GET.get('category', 'all')
        return context

    def get_template_names(self):
        if self.request.user.groups.filter(name='Veterinarian').exists():
            return ['images/gallery/vet-gallery.html']
        return ['images/gallery/regular-gallery.html']