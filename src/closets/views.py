from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView, ListView, FormView, CreateView
from django.db.models import Count
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.datetime_safe import datetime
from django.utils import timezone
from django.contrib import messages






from .models import Item
from .forms import ItemForm, ItemImageForm


class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

class ItemImageView(DetailView):
	model = Item
	template_name = 'show_item.html'
	form_class = ItemImageForm
	context_object_name = "items"
	slug_field = 'item_id'
	queryset = Item.objects.all().filter()


	def form_valid(self, form):
		item_image = Item(photo=self.get_form_kwargs().get('files')['photo'])
		item_image.save()
		self.id = item_image.id

		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return reverse('item_image', kwargs={'pk': self.id})

class ItemDetailView(DetailView):
	model = Item
	context_object_name = 'items'
	template_name = 'show_item.html'

	def get_object(self, queryset=None):
		return Item.objects.filter(user=self.request.user)


class ItemCreate(LoginRequiredMixin, CreateView):
	model = Item
	fields = ['photo', 'name', 'brand', 'category','condition', 'size', 'price']

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.posted_at = timezone.now()
		messages.add_message(self.request, messages.SUCCESS,
			"Item Added")


		return super().form_valid(form)


class AddItemView(LoginRequiredMixin, View):
	
	def get(self, request):
		form = ItemForm()
		return render(request, "/add.html", {'form': form})

	def post(self, request):
		form = ItemForm(request.POST)
		if form.is_valid():
			item = form.save(commit=False)
			item.user = request.user
			item.posted_at = datetime.now()
			update.save()
			messages.add_message(request, messages.SUCCESS,
				"You added this item")
			return redirect("mycloset")
		else:
			return render(request, '/add.html', {'form': form})

class ClosetView(LoginRequiredMixin, ListView):
	model = Item
	context_object_name = 'items'
	template_name = 'home.html'
	queryset = Item.objects.order_by('-posted_at').annotate(
		Count('favorite')).select_related()
	paginate_by = 20
	header = "All Items"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['header'] = self.header
		if self.request.user.is_authenticated():
			favorites = self.request.user.favorited_items.all()
		else:
			favorites = []
		context["favorites"] = favorites
		return context


class UserClosetView(DetailView):
	model = Item
	context_object_name = 'items'
	template_name = 'mycloset.html'

	def get_object(self, queryset=None):
		items = Item.objects.filter(user=self.request.user)
		if items == None:
			return HttpResponse("You have no items in your closet, get some.")
		else:
			return Item.objects.filter(user=self.request.user)


	
	





