#include <stdio.h>
#include <stdlib.h>



void le_texto (char texto[ ], int size_texto){ // string: ponteiro implícito
     char dummy[size_texto + 1]; // cabe um caractere a mais do que no texto:

     fflush(stdin);
     fgets(dummy, sizeof(dummy), stdin); // lê caracteres
     // O último caractere tem que ser '\n' para estar correto:
     while(dummy[strlen(dummy) -1] != '\n'){
         printf("\nNumero de caracteres digitados excedeu tamanho do campo.\n" );
         printf("Numero maximo de caracteres eh %d.\n", size_texto - 1);
         printf("Digite o conteudo novamente.\n");
         fflush(stdin);
         fgets(dummy, sizeof(dummy), stdin); // lê caracteres novamente
     }
     dummy[strlen(dummy)-1]= '\0'; // sempre precisa substituir o '\n'
     strcpy(texto, dummy); // transfere conteúdo digitado e sem o '\n' para texto
}
