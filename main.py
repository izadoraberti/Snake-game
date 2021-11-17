#include <stdio.h>
#include <windows.h>
#include <conio.h>
#include "ordena.h"
#include "menu.h"      //biblioteca criada para exibir menu

#define A 10           //altura,linha
#define L 35           //largura,coluna
#define PAREDE 219
#define COMIDA1 173
#define COMIDA2 184
#define COMIDA3 232
#define VIDAS 259
#define CABECA 258
#define CORPO 254
#define VELOCIDADE 100

COORD comida();
int cresce();
void movimenta();
void ranking();
void cobra_nova();
void traduz_mapa();
void comida_inicial();
void final();
void denovo();

typedef struct{         //informações das comidas
    COORD local;
    int valor;
}COMIDA;

int main(){
    int i=0,j=0, nlinha=0, cont=0,k=0, tamc=4, cobra_mais=0,comeu=0,testa=0,nova_com=0,h=0,vidas=3,total=0,reinicia=0,lar=0,comp=0;//largura e comprimento
    char mapa[1000][1000],tecla,linha[1002],l,dir='d';
    COORD cobra,parede[4000],c,corpo[4000],fimc,aux1,aux2,iniciotela,fimtela;
    COMIDA com[4]={0};
    FILE *m,*score;

    inicio();            // para imprimir menu
    system("cls");       //limpa tela
    system("color 0A");
    srand(time(NULL));

    traduz_mapa(mapa,&lar,&comp,parede,&k);
    comida_inicial(com,mapa,lar,comp);
    cobra_nova(&cobra, corpo, mapa, comp, lar, &tecla, &tamc, &reinicia);

    while(vidas>=0){
        imprime_mapa(&iniciotela,&fimtela,mapa,&cobra,comp,lar);
        dir=tecla;
        fflush(stdin);
        if(kbhit()) //verifica se teclado foi apertado (conio.h)
            dir=getch(); //dir recebe tecla apertada
        movimenta(mapa, &cobra, &tecla, &dir, corpo, tamc);
        teste_comeu(&cobra, com, &nova_com, &comeu, &cobra_mais);
        if(comeu)
            procedimentos_comeu(mapa, com, nova_com, lar, comp, parede, k, &comeu);
        if(cobra_mais){  //aumenta o tamanho da cobra, se ela tiver comido
            tamc++;
            total++;
            cobra_mais--;
        }
        se_bater(mapa,&cobra,corpo,parede,tamc,&vidas,&reinicia,k);
        if(reinicia){ //na funcao se_bater reinicia recebe valor
            vidas--;
            for(j=0;j<=tamc;j++)
                mapa[corpo[j].X] [corpo[j].Y]=' ';
            cobra_nova(&cobra, corpo, mapa, comp, lar, &tecla, &tamc, &reinicia);
        }
        printf("PONTOS: %d                ",total,vidas);
        imprime_vidas(vidas);
        Sleep(VELOCIDADE);
        system("cls");
    }
    final();
    printf("\nSua pontua%c%co %c: %d\n\nSeu nome %c: ",135,198,130,total,130);
    ordena(total);
    denovo();
}



void imprime_vidas(int vidas){
    int i;
    printf("VIDAS: ");
    if(vidas==0){
        printf(" %d",vidas);
    }else{
        for(i=0;i<vidas;i++)
            printf("%c ",VIDAS);
    }
}

void se_bater(char mapa[][1000],COORD *cobra,COORD corpo[4000], COORD parede[4000],int tamc,int *vidas, int *reinicia, int k){
    int i;
    i=1;
    while(i<tamc && vidas>=0){  //se bater no proprio corpo
        if((cobra->X==corpo[i].X)&&(cobra->Y==corpo[i].Y)){
            mapa[cobra->X][cobra->Y]=' ';
            *reinicia=1;//tentar fazer chamando reinicia
        }
        i++;
    }
    for(i=0;i<k;i++){            //se cobra bater na parede
        if((cobra->X==parede[i].X)&&(cobra->Y==parede[i].Y)){
            mapa[cobra->X][cobra->Y]=PAREDE;
            *reinicia=1;
        }
    }
}

void procedimentos_comeu(char mapa[][1000],COMIDA com[4],int nova_com,int lar,int comp,COORD parede[4000],int k,int *comeu){
    int j;
    com[nova_com].local=comida(lar,comp);
    for(j=0;j<k;j++) //se cobra bater na parede
        if(mapa[parede[j].X][parede[j].Y]==mapa[com[nova_com].local.X][com[nova_com].local.Y]){
            com[nova_com].local=comida(lar,comp); //gera um novo lugar para comida
            switch(1+(rand()%3)){ //gera valor randômico da comida
                case 1: mapa[com[nova_com].local.X][com[nova_com].local.Y]= COMIDA1;
                        com[nova_com].valor=1;
                        break;
                case 2: mapa[com[nova_com].local.X][com[nova_com].local.Y]= COMIDA2;
                        com[nova_com].valor=3;
                        break;
                case 3: mapa[com[nova_com].local.X][com[nova_com].local.Y]= COMIDA3;
                        com[nova_com].valor=5;
                        break;
            }
        *comeu=0; //reinicializa variável
        }
}

void teste_comeu(COORD *cobra,COMIDA com[4],int *nova_com, int *comeu, int *cobra_mais){
    int i;
    for(i=1;i<4;i++){
        if((cobra->X==com[i].local.X)&&(cobra->Y==com[i].local.Y)){ //se come comida
            *cobra_mais+=com[i].valor; //cresce determinado valor
            *nova_com=i;
            *comeu=i;
        }
    }
}

void arruma_co_cobra(COORD corpo[4000], int tamc){
    int h;
    COORD aux1,aux2={0,0};
    aux1.Y=corpo[1].Y;
    aux1.X=corpo[1].X;
    for(h=2;h<=tamc;h++){ //a partir do primeiro corpo corpo anterior troca de posição com o seguinte
        aux2.Y=corpo[h].Y; //corpo anterior troca de posição com o seguinte
        aux2.X=corpo[h].X;
        corpo[h].Y=aux1.Y;
        corpo[h].X=aux1.X;
        aux1.Y=aux2.Y;
        aux1.X=aux2.X;
    }
}

void movimenta(char mapa[][1000], COORD *cobra,char *t, char *dir, COORD corpo[4000], int tamc){
    atualiza_inicio_e_fim_do_corpo(mapa, cobra, corpo, tamc);
    switch(*dir){ //movimenta de acordo dir
    //    case 77:
        case 'd':
        case 'D':
            if(*t=='a')
                *t='a';
            else{
                *t='d';
                mapa[cobra->X][cobra->Y]=CORPO;
                cobra->Y++;
                mapa[cobra->X][cobra->Y]=CABECA;
            }
        break;
     //   case 75:
        case 'a':
        case 'A':
                if(*t=='d')
                    *t='d';
                else{
                    *t='a';
                    mapa[cobra->X][cobra->Y]=CORPO;
                    cobra->Y--;
                    mapa[cobra->X][cobra->Y]=CABECA;
                }
                break;
      //  case 72:
        case 'w':
        case 'W':
            if(*t=='s')
                *t='s';
            else{
                *t='w';
                mapa[cobra->X][cobra->Y]=CORPO;
                cobra->X--;
                mapa[cobra->X][cobra->Y]=CABECA;
            }
        break;
    //    case 80:
        case 's':
        case 'S':
            if(*t=='w')
                *t='w';
            else{
                *t='s';
                mapa[cobra->X][cobra->Y]=CORPO;
                cobra->X++;
                mapa[cobra->X][cobra->Y]=CABECA;
            }
        default: break;
    }
    arruma_co_cobra(corpo, tamc);
}

void atualiza_inicio_e_fim_do_corpo(char mapa[][1000], COORD *cobra, COORD corpo[4000], int tamc){
    mapa[corpo[tamc].X][corpo[tamc].Y]=' ';
    mapa[cobra->X][cobra->Y]=CABECA;
    corpo[1].X=cobra->X;
    corpo[1].Y=cobra->Y;
}

void testes_zoom(COORD *iniciotela,COORD *fimtela, COORD *cobra,int comp,int lar){
    iniciotela->Y=cobra->Y-L;
    if(iniciotela->Y<1)
        iniciotela->Y=1;
    iniciotela->X=cobra->X-A;
    if(iniciotela->X<1)
        iniciotela->X=1;
    fimtela->Y=cobra->Y+L;
    if(fimtela->Y<2*L+1)
        fimtela->Y=2*L+1;
    if(fimtela->Y>=lar){
        fimtela->Y=lar;
        iniciotela->Y=fimtela->Y-2*L;
    }
    fimtela->X=cobra->X+A;
    if(fimtela->X<2*A+1)
        fimtela->X=2*A+1;
    if(fimtela->X>=comp){
        fimtela->X=comp;
        iniciotela->X=fimtela->X-2*A;
    }
}

void imprime_mapa(COORD *iniciotela,COORD *fimtela,char mapa[][1000],COORD *cobra,int comp,int lar){
    int i=0,j=0;
    testes_zoom(iniciotela,fimtela,cobra,comp,lar);
    for(j=0;j<2*L+3;j++)
        printf("%c",PAREDE);
    printf("\n");
    for(i=iniciotela->X;i<=fimtela->X;i++){ //printa mapa por caractere
        printf("%c",PAREDE);
        for(j=iniciotela->Y;j<=fimtela->Y;j++)
            printf("%c",mapa[i][j]);
        printf("%c\n",PAREDE);
    }
    for(j=0;j<2*L+3;j++)
        printf("%c",PAREDE);
    printf("\n");
}

COORD comida(int lar, int comp){
    COORD c;
    c.X=1+(rand()%(comp-1));
    c.Y=1+(rand()%(lar-1));
    return c;
}

void cobra_nova(COORD *cobra, COORD corpo[4000], char mapa[][1000], int comp, int lar, char *tecla, int *tamc, int *reinicia){
    int i=1;
    *tamc=4; //tamanho inicial da cobra recebe 4
    cobra->X=comp/2-1;  //coloca a cabeça da cobra no centro
    cobra->Y=lar/2-1;
    mapa[cobra->X][cobra->Y]=CABECA;   //salva cabeça
    for(i=1;i<(*tamc);i++){
        mapa[cobra->X][cobra->Y-i]=CORPO; //salva corpo
        corpo[i].X=cobra->X;
        corpo[i].Y=cobra->Y-i;
    }
    *tecla='d';  //direção inicial
    *reinicia=0;
}

void traduz_mapa(char mapa[][1000],int *lar,int *comp,  COORD parede[4000], int *k){
    char linha[1002];
    FILE *m;
    int i=0,nlinha=0,np;
    m=fopen("GRANDE.txt","r");
    if (!m){
        printf("Erro na abertura do arquivo.");
    }else{
        np=0;
        while(!feof(m)){        //transforma o arquivo txt em bin
            fgets (linha,sizeof(linha),m);  //le linha
            i=0;
            while(i<(strlen(linha))){     //analiza cada caractere da linha
                switch(linha[i]){
                    case '0': mapa[nlinha][i]=' '; break;
                    case '1': mapa[nlinha][i]=PAREDE; //parede
                              parede[np].X=nlinha;   //salva as coordenadas das paredes
                              parede[np].Y=i;
                              np++;
                    default: break;
                }
                i++;
            }
            nlinha++;
        }
        *lar=strlen(linha)-2; //largura recebe tamanho da string
        *comp=nlinha-2;
        *k=np;
    }
}

void comida_inicial(COMIDA com[4],char mapa[][1000],int lar,int comp){
    int i;
    for(i=1;i<4;i++){
        com[i].local=comida(lar,comp);        //GERA COMIDA INICIAL
        switch(i){
            case 1: mapa[com[i].local.X][com[i].local.Y]= COMIDA1; com[i].valor=1; break;
            case 2: mapa[com[i].local.X][com[i].local.Y]= COMIDA2; com[i].valor=3; break;
            case 3: mapa[com[i].local.X][com[i].local.Y]= COMIDA3; com[i].valor=5; break;
        }
    }
}

void final(){
    system("color 0C");
    puts("\n\n");
    puts("                            ______     _______   _______");
    puts("                \\        / |      |   |         |       ");
    puts("                 \\      /  |      |   |         |       ");
    puts("                  \\    /   |      |   |         |----   ");
    puts("                   \\  /    |      |   |         |       ");
    puts("                    \\/     |______|   |_______  |_______");
    puts("\n");
    puts("         _______    ______   ______     _____   ______  ___   ___  ||| ");
    puts("        |       )  |        |      )   |     \\ |        ---   ---  |||");
    puts("        |------´   |___     |------\\   |      ||___     ---   ---  |||");
    puts("        |          |        |       \\  |      ||         --   --   |||");
    puts("        |          |______  |        | |_____/ |______    -___-     0 ");
    puts("\n\n\n\n");
    Sleep(1000);
    system("cls");
    system("color 5E");
}

void denovo(){ //para jogar de novo ou fechar jogo
    int i=100;
    char tecla;
    Sleep(3000);
    system("cls");
    gotoxy(30,10);
    printf("Deseja jogar novamente?\n                                      S-sim\n                                      N-nao\n\n");
    while(i>0){ //testa i vezes se uma das teclas foi pressionada
        i--;
        kbhit();
        tecla=getch();
        if(tecla=='S'||tecla=='s')
            main();
        else if(tecla=='N'||tecla=='n')
            return 0;
    }
}


