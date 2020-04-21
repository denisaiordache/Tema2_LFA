def pozitie_alfabet(litera):
    global alfabet
    for i in range(nr_caractere):
        if litera == alfabet[i]:
            return i
    return -1

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

def parcurgere(stari):
    global alfabet
    coada=[stari]
    for element in coada:
        for litera in alfabet:
            list=miscare_litera(element,litera)
            if list not in coada:
                coada.append(list)
    return coada


def transformare():
    global legaturi,nr_stari,nr_caractere,stari_finale,alfabet
    delta=[[[]for i in range(nr_caractere)]for j in range(nr_stari)]
    for leg in legaturi:
        delta[int(leg[0])][pozitie_alfabet(leg[1])].append(int(leg[2]))
    mat=[[[1]for i in range(nr_stari)]for j in range(nr_stari)]
    for i in range(nr_stari):
        for j in range(nr_stari):
            if i>j:
                if (i in stari_finale and j not in stari_finale) or (i not in stari_finale and j in stari_finale) :
                    mat[i][j]=mat[j][i]=[0]
    se_modif=1
    while se_modif==1:
        se_modif=0
        for col in range(nr_caractere):
            for stare in range(nr_stari-1):
                for stare2 in range(stare+1,nr_stari):
                    x=delta[stare2][col][0]
                    y=delta[stare][col][0]
                    #print(x,y)
                #print(mat[x][y])
                    if mat[x][y]==[0] and (mat[stare2][stare]==[1] or mat[stare][stare2]==[1]):
                        se_modif=1
                        print(stare,stare2)
                        mat[stare][stare2]=mat[stare2][stare]=[0]
    for i in range(nr_stari):
        for j in range(nr_stari):
            if i>j:
                print(i,j,mat[i][j])

    stari_echiv=[]
    coada=[]
    for col in range(nr_stari):
        if col not in coada:
            coada.append(col)
            list=[col]
            for linie in range(nr_stari):
                if linie>col:
                    if mat[linie][col]==[1]:
                        list.append(linie)
                        coada.append(linie)
            stari_echiv.append(list)
    print(stari_echiv)

    dfa_transitions={}


    for stare in stari_echiv:
        for caracter in alfabet:
            stari=miscare_litera(stare,caracter)
            for element in stari:
                for x in stari_echiv:
                    if element in x:
                        stari=x
                        dfa_transitions[(str(stare),caracter)]=stari
                        break
    print(dfa_transitions)
    for stare in stari_echiv:
        if stare_initiala in stare:
            stare_initiala_noua=stare
            break
    print("stare initiala noua",stare_initiala_noua)

    stari_finale_noi=[]
    for stare in stari_finale:
        for x in stari_echiv:
            if stare in x and x not in stari_finale_noi:
                stari_finale_noi.append(x)
    print("stari finale noi",stari_finale_noi)

    #eliminare stari dead-end

    print("stari echivalente",stari_echiv)
    copie=stari_echiv
    for stare in copie:
        dead_end=1
        for sf in stari_finale_noi:
            list=parcurgere(stare)
            for element in list:
                for i in range(len(element)):
                    if element[i] in sf:
                        dead_end=0
                        break

        if dead_end==1:
            i=stari_echiv.index(stare)
            stari_echiv.pop(i)
    print("starile automatului dupa eliminarea starilor dead-end",stari_echiv)

    #eliminare stari neaccesibile

    list=parcurgere(stare_initiala_noua)
    copie=stari_echiv
    for stari in copie:
        ok=0
        for element in stari:
            for sf in stari_finale_noi:
                if element in sf:
                    ok=1
                    break
        if ok==0 and stari!=stare_initiala_noua:
            i = stari_echiv.index(stari)
            stari_echiv.pop(i)

    dfa_min_alfabet=[]
    trans=0
    for x in dfa_transitions.keys():
        if dfa_transitions[x]!=[] and x[1] not in dfa_min_alfabet:
            dfa_min_alfabet.append(x[1])


    print(stari_echiv)
    g.write("Numar stari: ")
    g.write(str(len(stari_echiv)))
    g.write("\nStari DFA_min: ")
    g.write(str(stari_echiv))
    g.write("\nAlfabet: ")
    g.write(str(dfa_min_alfabet))
    g.write("\nStare initiala: ")
    g.write(str(stare_initiala_noua))
    g.write("\nNumar stari finale: ")
    g.write(str(len(stari_finale_noi)))
    g.write("\nStari finale DFA min: ")
    g.write(str(stari_finale_noi))

    for a in stari_echiv:
        for x in dfa_transitions.keys():
            if str(a)==x[0] and dfa_transitions[x] in stari_echiv:
                trans+=1
    g.write("\nNumar translatari: ")
    g.write(str(trans))

    for a in stari_echiv:
        for x in dfa_transitions.keys():
            if str(a)==x[0] and dfa_transitions[x] in stari_echiv:
                g.write("\n")
                g.write(x[0])
                g.write(x[1])
                g.write(str(dfa_transitions[x]))

f = open("dfa.in")
g=open("dfa_min.out","w")
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