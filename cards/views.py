from django.views.generic.base import View, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Set, Card
from .forms import LoginForm, SetForm

class IndexView(generic.ListView):
    template_name = 'cards/index.html'
    context_object_name = 'cards_set_list'

    def get_queryset(self):
        return Set.objects.order_by('-set_name')

class SetIndexView(generic.DetailView):
    model = Set
    template_name = 'cards/set_index.html'

class CardView(View):
    template_name = 'cards/card.html'

    def get(self, request, set_id, card_id):
        selected_set = get_object_or_404(Set, pk=set_id)
        try:
            selected_card = selected_set.card_set.get(id=card_id)
        except (KeyError, Card.DoesNotExist):
            return render(request, 'cards/set.html', {
                'set': selected_set,
                'error_message': "That's all folks!.",
            })
        else:
            context = {
                'set': selected_set,
                'card': selected_card,
            }
            try:
                prev_card = selected_set.card_set.filter(
                    id__lt=card_id).order_by("id")
                prev_card = prev_card[len(prev_card)-1]
            except (KeyError, Card.DoesNotExist, AssertionError):
                pass
            else:
                context['prev_card'] = prev_card
            try:
                next_card = selected_set.card_set.filter(
                    id__gt=card_id).order_by("id")[0:1].get()
            except (KeyError, Card.DoesNotExist):
                pass
            else:
                context['next_card'] = next_card

                print(context)
            return render(request, self.template_name, context)

class NewSetView(View):
    template_name = 'cards/set_form.html'

    def get(self, request):
        form = SetForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SetForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            new_set = Set(
                set_name = form.cleaned_data['set_name'],
                description = form.cleaned_data['description'],
                private = form.cleaned_data['private']
            )
            new_set.save()
            return HttpResponseRedirect(reverse('cards:setIndex', args=(new_set.id,)))

        # TODO have an error page
        return HttpResponseRedirect(reverse('cards:setIndex', args=(new_set.id,)))
