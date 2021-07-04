escala_cromatica={
    0:"B",
    1:"C",  2:"C#",    3:"D",    4:"D#",    5:"E",    6:"F",
    7:"F#", 8:"G",     9:"G#",   10:"A",    11:"A#",    12:"B"
}
def num_to_note(num):
    return escala_cromatica[num%12]

def note_to_num(note):
    for k,v in escala_cromatica.items():
        if v==note: return k

def gerar_escala(escala,tonalidade):
    arr={}
    grau=0
    for nota in escala:
        grau+=1
        arr[grau]=num_to_note((nota-1+note_to_num(tonalidade))%12)
    return arr

def esta_na_escala(escala,tonalidade,cifra):
    for grau,nota in gerar_escala(escala,tonalidade).items():
        if nota==cifra: return grau
    return False

def desenhar_escala_no_braco_do_instrumento(afinacao,escala,tonalidade,numero_de_trastes=12):
    print("desenhando escala no braco do violao:")
    for c in afinacao:
        print(c+")|\t",end="")
        for traste in range(1,numero_de_trastes+1):
            nota=num_to_note(note_to_num(c)+traste)
            grau=esta_na_escala(escala,tonalidade,nota)
            if grau:
                print(str(grau)+"-"+nota,end="")
            else:
                print('x',end="")
            print("\t|",end="")
        print("")

afinacao_standard=["E","A","D","G","B","E"]
afinacao_openD=["D","A","D","G","A","D"]
afinacao_openE=["E","B","E","G#","B","E"]
afinacao_openG=["D","G","D","G","B","D"]
afinacao_dropD=["D","A","D","G","B","E"]

afinacao_viola_caipira=["B","E","G#","B","E"]
afinacao_ukulele=["G","C","E","A"]
afinacao_baixo_4cordas=["E","A","D","G"]
afinacao_cavaquinho=["D","G","B","D"]
afinacao_cavaquinho=["D","G","B","D"]
afinacao_banjo=["D","G","D","A"]

escala_diatonica=[1,3,5,6,8,10,12]
escala_pentatonica=[1,3,5,8,10]
escala_pentablues=[1,3,4,5,8,10]

# exemplo: você pode escolher a escala e afinacao do instrumento
desenhar_escala_no_braco_do_instrumento(afinacao_standard,escala_pentatonica,'E')
