#include <stdio.h>
#include <stdlib.h>



void le_texto (char texto[ ], int size_texto){ // string: ponteiro impl�cito
     char dummy[size_texto + 1]; // cabe um caractere a mais do que no texto:

     fflush(stdin);
     fgets(dummy, sizeof(dummy), stdin); // l� caracteres
     // O �ltimo caractere tem que ser '\n' para estar correto:
     while(dummy[strlen(dummy) -1] != '\n'){
         printf("\nNumero de caracteres digitados excedeu tamanho do campo.\n" );
         printf("Numero maximo de caracteres eh %d.\n", size_texto - 1);
         printf("Digite o conteudo novamente.\n");
         fflush(stdin);
         fgets(dummy, sizeof(dummy), stdin); // l� caracteres novamente
     }
     dummy[strlen(dummy)-1]= '\0'; // sempre precisa substituir o '\n'
     strcpy(texto, dummy); // transfere conte�do digitado e sem o '\n' para texto
}
