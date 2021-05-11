from django.views.generic.base import View, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Set, Card

class IndexView(generic.ListView):
    template_name = 'cards/index.html'
    context_object_name = 'cards_set_list'

    def get_queryset(self):
        return Set.objects.order_by('-set_name')

class SetView(generic.DetailView):
    model = Set
    template_name = 'cards/set.html'

class CardView(View):
    template_name = 'cards/card.html'

    def get(self, request, set_id, card_id):
        selected_set = get_object_or_404(Set, pk=set_id)
        try:
            selected_card = selected_set.card_set.get(id=card_id)
            print(selected_card)
            context = { 'set': selected_set, 'card': selected_card }
        except (KeyError, Card.DoesNotExist):
            return render(request, 'cards/set.html', {
                'set': selected_set,
                'error_message': "card not in range.",
            })
        else:
            return render(request, self.template_name, context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'cards/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('cards:results', args=(question.id,)))
