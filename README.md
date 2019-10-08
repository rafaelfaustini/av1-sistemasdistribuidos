# Avaliação

## Introdução
O DNA humano é uma estrutura em dupla hélice, cada uma composta por bases nitrogenadas. Essas bases podem ser de quatro tipos: Citosina (C), Guanina (G), Adenina (A) e Timina (T). Separando a hélice em duas fitas, cada uma pode ser lida como uma sequência de bases. Para cada base na fita, há uma outra complementar na outra fita. As bases complementares são: Adenina com Timina e Citosina com Guanina. Dessa forma, se uma sequência é **AATGCTCC**, a outra só pode ser **TTACGAGG**.

## Objetivo
O seu objetivo nessa avaliação é criar um sistema distribuído, seguindo o modelo cliente-servidor, para verificar se sequências de DNA são complementares. O seu sistema deverá ser composto por duas partes (uma para o cliente e outra para o servidor) que devem possuir as características e funcionalidades descritas abaixo.

## Cliente
O Cliente deverá solicitar ao usuário diversos pares de sequências, uma de cada vez, até que a primeira sequência seja vazia. A cada vez que uma sequência é lida, ela deve ser enviada ao servidor para verificar se é uma sequência de DNA, ou seja, uma sequência que só contém as bases nitrogenadas. Após enviar o par de sequências, o cliente deve perguntar ao servidor se o par enviado é formado por duas sequências complementares.
Ao final de todos os pares, o cliente deve enviar ao servidor uma string contendo FIM, a qual o servidor retornará o tamanho da maior sequência pertencente a um par complementar.
Servidor

## Servidor
O servidor deverá ser implementado prevendo a possibilidade de diversas conexões simultâneas. Para tal, deve utilizar uma thread para cada conexão. A porta a ser utilizada pelo servidor será 8792.
Para cada conexão, o servidor deverá receber a primeira sequência e informar ao cliente se ela é válida; receber a segunda sequência e informar ao cliente se ela é válida; receber a requisição do cliente e informar se o par é complementar.
Caso receba uma string FIM, o servidor deve saber que o envio dos pares terminou e deverá retornar ao cliente, o tamanho da maior sequência pertencente a um par complementar.

