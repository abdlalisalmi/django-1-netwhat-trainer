from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect
from django.db.models import Sum
from django.views import generic

from django.shortcuts import render_to_response

from .models import (
        EnQuestion,
        EnChoice,
        FrQuestion,
        FrChoice
    )

# Create your views here.



def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response

def question_view(request, language, id):

    try:
        if language == 'en':
            question = EnQuestion.objects.get(pk=id)
            choice_list = question.enchoice_set.all()
        elif language == 'fr':
            question = FrQuestion.objects.get(pk=id)
            choice_list = question.frchoice_set.all()
    except(KeyError, EnChoice.DoesNotExist, FrChoice.DoesNotExist, EnQuestion.DoesNotExist, FrQuestion.DoesNotExist):
        return HttpResponseRedirect(reverse('question:result', args=(language,)))

    context = {
        'language': language,
        'question': question,
        'choice_list': choice_list
    }
    template_name = "question.html"
    return render(request, template_name, context)


def repons_handle(request, language, id):
    try:
        if language == 'en':
            question = EnQuestion.objects.get(pk=id)
            choice_list = question.enchoice_set.all()
        elif language == 'fr':
            question = FrQuestion.objects.get(pk=id)
            choice_list = question.frchoice_set.all()
    except(KeyError, EnChoice.DoesNotExist, FrChoice.DoesNotExist, EnQuestion.DoesNotExist, FrQuestion.DoesNotExist):
        return HttpResponseRedirect(reverse('question:result', args=(language,)))

    try:
        if language == 'en':
            choice = question.enchoice_set.get(pk=request.POST['choice'])
        elif language == 'fr':
            choice = question.frchoice_set.get(pk=request.POST['choice'])
    except (KeyError, EnChoice.DoesNotExist, FrChoice.DoesNotExist):
        template_name = 'question.html'
        if language == 'en':
            error_message = "You didn't select a choice."
        elif language == 'fr':
            error_message = "Vous n'avez pas sélectionné de choix."
        context = {
            'language': language,
            'question': question,
            'choice_list': choice_list,
            'error_message': error_message
        }
        return render(request, template_name, context)
    else:
        question.selected_choice = choice.choice
        question.is_correct = 0
        if question.correct_choice == question.selected_choice:
            question.is_correct = 1
        print(question.is_correct)
        question.save()

        return HttpResponseRedirect(reverse('question:question_view', args=(language, question.next_url())))

def result_view(request, language):
    if language == 'en':
        question = EnQuestion.objects.all()
        number_correct = EnQuestion.objects.aggregate(Sum('is_correct'))
        correct = number_correct["is_correct__sum"]
        number_objects = EnQuestion.objects.all().count()

    elif language == 'fr':
        question = FrQuestion.objects.all()
        number_correct = FrQuestion.objects.aggregate(Sum('is_correct'))
        correct = number_correct["is_correct__sum"]
        number_objects = FrQuestion.objects.all().count()

    worng = number_objects - correct
    context = {
        'number_correct': correct,
        'number_worng': worng,
        'language': language,
        'question': question
    }
    template_name = 'result.html'
    return render(request, template_name, context)