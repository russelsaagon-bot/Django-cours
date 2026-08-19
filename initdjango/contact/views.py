from django.shortcuts import render, redirect

# Stockage en mémoire (simulé sans base de données)
CARNET_ADRESSES = [
    {'id': 1, 'nom': 'Dupont', 'prenom': 'Jean', 'telephone': '0612345678', 'email': 'jean.dupont@example.com'},
    {'id': 2, 'nom': 'Martin', 'prenom': 'Alice', 'telephone': '0698765432', 'email': 'alice.martin@example.com'},
    {'id': 3, 'nom': 'Bernard', 'prenom': 'Luc', 'telephone': '0655443322', 'email': 'luc.bernard@example.com'},
]

def contact_list(request):
    """READ : Afficher la liste des contacts et gérer l'ajout ou la modification"""
    edit_id = request.GET.get('edit')
    contact_to_edit = None
    if edit_id:
        try:
            edit_id = int(edit_id)
            contact_to_edit = next((c for c in CARNET_ADRESSES if c['id'] == edit_id), None)
        except ValueError:
            pass

    context = {
        'contacts': CARNET_ADRESSES,
        'contact_to_edit': contact_to_edit,
    }
    return render(request, 'contact/contact.html', context)

def contact_add(request):
    """CREATE : Ajouter un nouveau contact"""
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')

        if nom and prenom:
            new_id = max([c['id'] for c in CARNET_ADRESSES], default=0) + 1
            CARNET_ADRESSES.append({
                'id': new_id,
                'nom': nom,
                'prenom': prenom,
                'telephone': telephone,
                'email': email
            })
    return redirect('contact')

def contact_update(request, pk):
    """UPDATE : Mettre à jour un contact existant"""
    if request.method == 'POST':
        for contact in CARNET_ADRESSES:
            if contact['id'] == pk:
                contact['nom'] = request.POST.get('nom', contact['nom'])
                contact['prenom'] = request.POST.get('prenom', contact['prenom'])
                contact['telephone'] = request.POST.get('telephone', contact['telephone'])
                contact['email'] = request.POST.get('email', contact['email'])
                break
    return redirect('contact')

def contact_delete(request, pk):
    """DELETE : Supprimer un contact"""
    global CARNET_ADRESSES
    CARNET_ADRESSES = [c for c in CARNET_ADRESSES if c['id'] != pk]
    return redirect('contact')


