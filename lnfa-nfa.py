def miscari_lambda(stari_curente):
    am_lambda = 1
    global legaturi
    while (am_lambda):
        am_lambda = 0
        rez = []
        for stare in stari_curente:
            for leg in legaturi:
                if int(leg[0]) == stare and leg[1] == '$' and (
                        int(leg[2]) not in rez and int(leg[2]) not in stari_curente):
                    rez.append(int(leg[2]))
                    am_lambda = 1
        stari_curente.extend(rez)

    return sorted(stari_curente)


def miscare_litera(stari_curente, caracter):
    stari_totale = []
    for stare in stari_curente:
        stari = []
        for leg in legaturi:
            if int(leg[0]) == stare and leg[1] == caracter and int(leg[2]) not in stari:
                stari.append(int(leg[2]))
        stari_totale.extend(stari)
    rez = []
    for x in stari_totale:
        if x not in rez:
            rez.append(x)
    return rez


def pozitie_alfabet(litera):
    global alfabet
    for i in range(nr_caractere):
        if litera == alfabet[i]:
            return i
    return -1


def transformare():
    global stare_initiala, stari_finale
    L = []
    mat = [[[] for i in range(nr_caractere - 1)] for j in range(nr_stari)]
    for i in range(nr_stari):
        lista = [i]
        lista = miscari_lambda(lista)
        if i not in lista:
            lista.append(i)
        for element in stari_finale:
            if element in lista and i not in stari_finale:
                stari_finale.append(i)


        new = []
        for litera in alfabet:
            if litera != '$':
                new = miscare_litera(lista, litera)
                new = miscari_lambda(new)
                mat[i][pozitie_alfabet(litera)].extend(new)


    print(mat)
    l=len(mat)
    stari=[]
    nfa_finals=[]

    for i in range(nr_stari):
        stari.append(i)

    for i in stari:
        for x in miscari_lambda([i]):
            if x in stari_finale and i not in nfa_finals:
                nfa_finals.append(i)


    for i in stari:
        for j in range(i+1,len(stari)):
            if mat[i]==mat[j] and ((i in nfa_finals and j in nfa_finals) or (i not in nfa_finals and j not in nfa_finals)) :
                poz=stari.index(j)
                stari.pop(poz)
                for a in range(nr_caractere-1):
                    mat[j][a]=[]
                for x in range(l):
                    for y in range(nr_caractere-1):
                        if j in mat[x][y]:
                            poz1=mat[x][y].index(j)
                            if i not in mat[x][y]:
                                mat[x][y][poz1]=i
                            else:
                                mat[x][y].pop(poz1)

    print(mat)

    for i in nfa_finals:
        if i not in stari:
            poz=nfa_finals.index(i)
            nfa_finals.pop(poz)
    print(sorted(nfa_finals))

    nfa_translatari=0
    nfa_alfabet=[]
    nfa_stari=[]
    print(nfa_finals)


    for i in range(len(mat)):
        for j in range(nr_caractere-1):
            if mat[i][j]!=[]:
                if i not in nfa_stari:
                    nfa_stari.append(i)
                if alfabet[j] not in nfa_alfabet:
                    nfa_alfabet.append(alfabet[j])
                for k in range(len(mat[i][j])):
                    nfa_translatari+=1

    nfa_nr_stari=len(nfa_stari)
    g.write("Numar stari NFA: ")
    g.write(str(nfa_nr_stari))
    g.write("\nStari NFA: ")
    g.write(str(nfa_stari))
    g.write("\nAlfabet NFA: ")
    g.write(str(nfa_alfabet))
    g.write("\nStare initiala: ")
    g.write(str(stare_initiala))
    g.write("\nNumar stari finale: ")
    g.write(str(len(nfa_finals)))
    g.write("\nStari finale NFA: ")
    g.write(str(nfa_finals))
    g.write("\nNumar translatari: ")
    g.write(str(nfa_translatari))
    for i in range(len(mat)):
        for j in range(nr_caractere-1):
            if mat[i][j]!=[]:
                for k in range(len(mat[i][j])):
                    g.write('\n')
                    g.write(str(i))
                    g.write(alfabet[j])
                    g.write(str(mat[i][j][k]))







f = open("lnfa.in")
g=open("nfa.out","w")
nr_stari = int(f.readline())
nr_caractere = int(f.readline())
alfabet = [x for x in f.readline().split()]
stare_initiala = int(f.readline())
nr_stari_finale = int(f.readline())
stari_finale = [int(x) for x in f.readline().split()]
nr_translatari = int(f.readline())
legaturi = []
for i in range(nr_translatari):
    legaturi.append(f.readline())
for i in range(len(legaturi) - 1):
    legaturi[i] = legaturi[i][:len(legaturi[i]) - 1]

transformare()