#include <stdio.h>
#include <stdlib.h>
#include "texto.h"


typedef struct{
    char nome[11];
    int pontos;
}P;

int ordena(int pont){
    P jog, lido;
    FILE *arq1;
    int inseriu=0, cont=0;
    jog.pontos=pont;
    le_texto(jog.nome,11);
    if ((arq1 = fopen("ranking3", "rb")) != NULL)
        fclose(arq1);
    else fclose ( fopen("ranking3", "wb") );
    if ((arq1 = fopen("ranking3", "r+b")) == NULL)
        printf("Erro ao abrir arquivo entrada \n");
    else{
        fseek( arq1, 0*sizeof(P), SEEK_END );
        while (!feof(arq1) && !inseriu ){
            fseek( arq1, -1*sizeof(P), SEEK_CUR );
            if (fread(&lido, 1, sizeof(P), arq1) != NULL ){
                if( jog.pontos < lido.pontos ){
                    fseek( arq1, 0*sizeof(P), SEEK_CUR );
                    fwrite(&jog, 1, sizeof(P), arq1 );
                    inseriu = 1;
                }else{
                    fseek( arq1, 0*sizeof(P), SEEK_CUR );
                    fwrite( &lido, 1, sizeof(P), arq1 );
                    fseek( arq1, -2*sizeof(P), SEEK_CUR );
                    if(ftell(arq1)==0){
                        fwrite( &jog, 1, sizeof(P), arq1 );
                        inseriu = 1;
                    }
                }
            }else if( !inseriu ){
                fseek( arq1, -1*sizeof(P), SEEK_CUR );
                fwrite( &jog, 1, sizeof(P), arq1 );
                inseriu = 1;
            }
            fflush(arq1);
        }
        if ((arq1 = fopen("ranking3", "rb")) == NULL)
            printf("Erro ao abrir arquivo saida \n");
        else{
            rewind(arq1);
            printf("\n\n\n\n                       RANKING\n\n");
            // || !feof(arq1)
            for (cont=1;cont<=10;cont++)
                if (fread(&lido, 1, sizeof(P), arq1) != NULL )
                    printf( "%2d%c  %10s..........................%4d pontos\n", cont, 167, lido.nome, lido.pontos );
            fclose (arq1);
        }
    }
}
