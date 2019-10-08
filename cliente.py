from socket import  *

s = socket ()


servidor="127.0.0.1"
porta=8792
s.connect((servidor, porta))

def enviar(s, msg):
    byte = str.encode(msg, "UTF-8")
    s.send(byte)

a= ""
f= True
while a!= "" or f==True:
    f=False
    a = input("Digite a sequencia de DNA: ")
    if a == "":
        break
    enviar(s, a)
    status = s.recv(8192) # Resposta do server se a sequencia for válida (0)
    # Retorna 1 caso inválido
   # print(status.decode("utf-8"))
    
    if status.decode("utf-8") == "1":
        print("Sequencia de DNA inválida")
        continue

    b = input("Digite o par da sequencia: ")
    enviar(s, b)
    status = s.recv(8192) # Resposta do server se o par for válido(0)
   # print(status.decode("utf-8"))
    
        # Retorna 1 caso inválido
        # Retorna 2 caso par não complementar
    if status.decode("utf-8") == "1" :
        print("Par inválido\n")
        continue
    elif status.decode("utf-8") == "2":
        print("Par não complementar\n")
        continue
    elif status.decode("utf-8") == "0":
        print("Par válido e complementar\n")

enviar(s, "FIM")
resultado = s.recv(8192) # Resultado com o tamanho da maior sequencia
print("\nO tamanho do maior dna é : %s"%(resultado.decode("utf-8")))
s.close ()
