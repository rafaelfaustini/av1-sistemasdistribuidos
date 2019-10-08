from socket import *
from threading import Thread

def envia(s,msg):
    s.send(str.encode(msg, "utf-8"))

def isValido(dna):
    valido = ["C", "G", "A", "T"]
    for letra in dna:
        if(letra not in valido):
            return False
    return True

def isComplementar(dna,par):
    combinacoes = {
    "A" : "T",
    "T" : "A",
    "G" : "C",
    "C" : "G"
            }
    if len(dna) != len(par):
        return False
    for i in range(0,len(par)):
    
        if combinacoes[dna[i]] != par[i]:
            return False
    return True

def resultado(dnas):
    maior = 0
    for dna in dnas:
        tamanho= len(dna)
        if(tamanho > maior):
            maior = tamanho
    return maior



def atende (conn, cliente):
        conn.settimeout(100.00)
        validos = []
        while True:
            a= conn.recv(4096).decode("utf-8")
            if(a == "FIM"):
                break
            if(isValido(a)):
                envia(conn,"0")
            else:
                envia(conn, "1")
            b = conn.recv(4096).decode("utf-8")
            if(b == "FIM"):
                break
            if(isValido(b)):
                if(isComplementar(a,b)):
                    envia(conn, "0")
                else:
                    envia(conn, "2")
            else:
                envia(conn, "1")
                
            if isValido(a) and isValido(b) and isComplementar(a,b):
                validos.append(a)
        
        r = resultado(validos)
        envia(conn, str(r))
        print ("Fim da conexao com "+str(cliente))
        conn.close

s = socket ()
host = "127.0.0.1"
porta = 8792
s.bind ((host, porta))
s.listen (100)
nthr = 0

while True:
        (conn, cliente) = s.accept ()

        print ("Recebi a conexao de "+str(cliente))
        nthr += 1
        print ("Criando thread "+str(nthr))
        t = Thread(target=atende,args=(conn, cliente,))
        t.start()
