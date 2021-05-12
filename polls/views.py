from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.views import generic

from polls.models import Poll, Choice
from polls.forms import PollModelForm, ChoiceInlineFormSet


def home(request):
    return HttpResponseRedirect(reverse('create_polls',))


def create_polls(request):
    poll = Poll()
    poll_form = PollModelForm(instance=poll)

    if request.method == "POST":
        poll_form = PollModelForm(request.POST)

        formset = ChoiceInlineFormSet(request.POST, request.FILES)

        if poll_form.is_valid():
            created_poll = poll_form.save(commit=False)
            formset = ChoiceInlineFormSet(request.POST, request.FILES, instance=created_poll)

            if formset.is_valid():
                created_poll.save()
                formset.save()

                return HttpResponseRedirect(reverse('vote', args=(created_poll.uuid,)))
    else:
        formset = ChoiceInlineFormSet(instance=poll)
    return render(request, 'polls/manage_polls.html', {'poll_form': poll_form,'formset': formset, 'poll': poll})


def vote(request, poll_id):
    poll = get_object_or_404(Poll, uuid=poll_id)

    if request.COOKIES.get('{}'.format(poll_id)) or poll.is_expired():
        return HttpResponseRedirect(reverse('results', args=(poll.uuid,)))
    else:
        if request.POST:
            try:
                selected_choice = poll.choice_set.get(pk=request.POST['choice'])
            except (KeyError, Choice.DoesNotExist):
                return render(request, 'polls/vote.html', {
                    'poll': poll,
                    'error_message': "You didn't select a choice.",
                })
            else:
                selected_choice.votes += 1
                selected_choice.save()
                response = HttpResponseRedirect(reverse('results', args=(poll_id,)))
                response.set_cookie('{}'.format(poll_id), selected_choice.choice_text, max_age=poll.get_total_seconds())
                return response
        else:
            return render(request, 'polls/vote.html', {'poll': poll,})


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'
    slug_field = 'uuid'

    def get_context_data(self, *args, **kwargs):
        context = super(ResultsView, self).get_context_data(*args, **kwargs)
        poll = get_object_or_404(Poll, uuid=self.kwargs.get('slug'))
        context['cookie'] = self.request.COOKIES.get('{}'.format(poll.uuid))
        return context
