def question(annonce, essais =4, please ='oui ou non'):
    while essais >0:
        reponse = input(annonce)
        if reponse in ('o', 'oui', 'O', 'Oui', 'OUI'):
            return 1
        if reponse in ('n', 'non', 'N', 'Non', 'NON'):
            return 0
        print(please)
        essais = essais-1
