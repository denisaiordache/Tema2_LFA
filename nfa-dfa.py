from collections import OrderedDict
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

def transformare():
    global legaturi,nr_caractere,nr_stari,stare_initiala,alfabet
    dfa_transitions={}
    stari=[]
    coada=[[stare_initiala]]
    for i in range(nr_stari):
        stari.append(i)
    for stare in coada:
        for litera in alfabet:
            if len(str(stare))==1:
                if miscare_litera([stare],litera) not in coada and len(miscare_litera([stare],litera))>0:
                    coada.append(miscare_litera([stare],litera))
            else:
                if miscare_litera(stare,litera) not in coada and len(miscare_litera(stare,litera))>0:
                    coada.append(miscare_litera(stare,litera))
    for stare in coada:
        for litera in alfabet:
            if len(str(stare))==1:
                dfa_transitions[(str(stare),litera)]=miscare_litera([stare],litera)
            else:
                dfa_transitions[str(stare),litera]=miscare_litera(stare,litera)
    print(dfa_transitions)
    dfa_finals=[]
    trans=0
    dfa_alfabet=[]
    for x in dfa_transitions.keys():
        if len(x[0])>1:
            lista=[]
            for a in x[0]:
                if a!='['and a!=']'and a!=',' and a!=' ':
                    if int(a) in stari_finale and x[0] not in dfa_finals:
                        dfa_finals.append(x[0])
        if dfa_transitions[x]!=[]:
            trans+=1
            if x[1] not in dfa_alfabet:
                dfa_alfabet.append(x[1])

    print(dfa_finals)
    print(trans)
    print(len(dfa_finals))
    print(coada)
    print(len(coada))
    g.write("Numar stari: ")
    g.write(str(len(coada)))
    g.write("\nStari DFA: ")
    g.write(str(coada))
    g.write("\nAlfabet DFA: ")
    g.write(str(dfa_alfabet))
    g.write("\nStare initiala: ")
    g.write(str(stare_initiala))
    g.write("\nNumar stari finale: ")
    g.write(str(len(dfa_finals)))
    g.write("\nStari finale DFA: ")
    g.write(str(dfa_finals))
    g.write("\nNumar translatari: ")
    g.write(str(trans))

    for x in dfa_transitions.keys():
        if dfa_transitions[x] != []:
            g.write("\n")
            g.write(x[0])
            g.write(x[1])
            g.write(str(dfa_transitions[x]))


f = open("nfa.in")
g=open("dfa.out","w")
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
print(legaturi)
transformare()