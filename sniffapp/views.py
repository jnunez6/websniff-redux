from django.shortcuts import render
from .models import GWCandidate, GWevent, GWfield
from django.http import JsonResponse


def index(request):
    gwevent_list = GWevent.objects.order_by('gwevent')
    list_of_snrcandidates = GWCandidate.objects.all()
    likelycandidates = []
    for cand in list_of_snrcandidates:
        if cand.likelyvote >= 2 and cand.unlikelyvote == 0:
            likelycandidates.append(cand)
    context = {'gwevent_list': gwevent_list,
               'likelycandidates': likelycandidates[:5]}
    return render(request, 'sniffapp/index.html', context)


def results(request):
    candidates = GWCandidate.objects.all()
    for candidate in candidates:
        votesum = candidate.likelyvote + candidate.unlikelyvote + candidate.possiblevote
        if votesum > 0:
            percentlikely = round((float(candidate.likelyvote) / float(votesum))*100, 2)
            percentpossible = round((float(candidate.possiblevote) / float(votesum))*100, 2)
            candidate.percentlikely = percentlikely
            candidate.percentpossible = percentpossible
            candidate.save()

    candidate_likely_list = GWCandidate.objects.order_by('-percentlikely')[:100]
    candidate_possible_list = GWCandidate.objects.order_by('-percentpossible')[:100]
    context = {'likelylist': candidate_likely_list,
               'possiblelist': candidate_possible_list,
               }
    return render(request,'sniffapp/results.html', context)


def fields(request, gwevent):
    givenevent_list = GWfield.objects.filter(gwevent__gwevent=gwevent).order_by('field')
    fieldvotes = []
    for fieldobject in givenevent_list:
        fieldname = fieldobject.field
        first_candidate_in_field = GWCandidate.objects.filter(field__field=fieldname).first()
        if first_candidate_in_field == None:
            nocand = "No Candidates"
            fieldvotes.append(nocand)
        else:
            votesum = first_candidate_in_field.likelyvote + first_candidate_in_field.unlikelyvote + first_candidate_in_field.possiblevote
            if votesum == 0:
                novotes = "Hasn't been sniffed yet"
                fieldvotes.append(novotes)
            if votesum >= 1:
                hasvotes = 'Has been sniffed ' + str(votesum) + ' times'
                fieldvotes.append(hasvotes)
    zipped_data = zip(givenevent_list, fieldvotes)
    context = {'fieldlist': givenevent_list,
               'gwevent': gwevent,
               'zipped_data': zipped_data
               }
    return render(request, 'sniffapp/fields.html', context)


def candidates(request, gwevent, field_name):
    list_of_candidates = GWCandidate.objects.filter(field__field=field_name).order_by('-snr')
    context = {'list_of_candidates': list_of_candidates,
               'field': field_name,
               'gwevent': gwevent,
               }
    return render(request, 'sniffapp/candidates.html', context)


def firstpush(request):
    list_of_snrcandidates = GWCandidate.objects.all().order_by('-snr')
    novotecandidates = []
    for cand in list_of_snrcandidates:
        votesum = cand.likelyvote + cand.unlikelyvote
        if votesum <= 0:
            novotecandidates.append(cand)
    context = {'list_of_snrcandidates': novotecandidates[:50]}
    return render(request, 'sniffapp/firstpush.html', context)


def secondpush(request):
    list_of_snrcandidates = GWCandidate.objects.all().order_by('-snr')
    likelycandidates = []
    for cand in list_of_snrcandidates:
        if cand.likelyvote == 1 and cand.unlikelyvote == 0:
            likelycandidates.append(cand)

    context = {'list_of_snrcandidates': likelycandidates}
    return render(request, 'sniffapp/secondpush.html', context)


def likelycandidates(request):
    list_of_snrcandidates = GWCandidate.objects.all().order_by('-snr')
    likelycandidates = []
    for cand in list_of_snrcandidates:
        if cand.likelyvote >= 2 and cand.unlikelyvote == 0:
            likelycandidates.append(cand)
    context = {'list_of_snrcandidates': likelycandidates}
    return render(request, 'sniffapp/likelycandidates.html', context)


def likelyvote(request, gwevent, field_name, candidate_id):
    candidate = GWCandidate.objects.get(field__field=field_name, gwevent__gwevent=gwevent,
                                        candidate_id=candidate_id)
    candidate.likelyvote += 1
    candidate.save()
    data = {
        'message': "Successfully submitted push vote.", }
    return JsonResponse(data)


def possiblevote(request, gwevent, field_name, candidate_id):
    candidate = GWCandidate.objects.get(field__field=field_name, gwevent__gwevent=gwevent,
                                        candidate_id=candidate_id)
    candidate.possiblevote += 1
    candidate.save()
    data = {
        'message': "Successfully submitted form data.", }
    return JsonResponse(data)


def unlikelyvote(request, gwevent, field_name, candidate_id):
    candidate = GWCandidate.objects.get(field__field=field_name, gwevent__gwevent=gwevent,
                                        candidate_id=candidate_id)
    candidate.unlikelyvote += 1
    candidate.save()
    data = {
        'message': "Successfully submitted veto vote.", }
    return JsonResponse(data)
