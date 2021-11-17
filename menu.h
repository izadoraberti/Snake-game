#include<windows.h>
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
void gotoxy(int x, int y){
     SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),(COORD){x-1,y-1});
}
void creditos(){
    gotoxy(32,4);
    printf(" JOGO DA JIB%CIA",224);
    gotoxy(20,22);
    printf("CR%cDITOS A IZADORA E LETICIA - ECP 2016",144);
}
void manual(){
    system("cls");
    gotoxy(27,4);
    printf("BEM-VINDO AO JOGO DA JIB%cIA",224);
    printf("\n\n\n ----> Movimente-se com as teclas wasd\n\n\n");
    printf(" ----> Existem 3 tipos de comidas\n          %c vale 1 ponto\n          %c vale 3 pontos\n          %c vale 5 pontos\n\n\n",173,184,259);
    printf(" ----> Voc%c come%ca com 3 vidas e 0 pontos\n",136,135);
    printf("\n\n ----> Bater na parede e encostar em si mesmo te faz perder 1 vida");
    printf("\n\n\n ----> O objetivo %c n%co morrer, mas se isso acontecer, pode aparecer no ranking",130,198);
    gotoxy(32,25);
    printf("  BOA SORTE!");
    Sleep(1000);
    //system("pause");
}

void inicio(){
    int i,j;
    char menu[2][30]={"    Jogar   ","   Manual   "};
    system("color 0A");
    system("cls");
    char tecla[20],escolhe;
    system("cls");
    printf("\n\n\n\n\n\n                                %c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",220,220,220,220,220,220,220,220,220,220,220,220,220,220);
    printf("                                %c            %c\n",219,219);
    printf("                                %c%s%c\n",219,menu[0],219);
    printf("                                %c            %c\n",219,219);
    printf("                                %c%c%c%c%c%c%c%c%c%c%c%c%c%c",223,223,223,223,223,223,223,223,223,223,223,223,223,223);
    printf("\n\n\n                                %c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",201,205,205,205,205,205,205,205,205,205,205,205,205,187);
    printf("                                %c            %c\n",186,186);
    printf("                                %c%s%c\n",186,menu[1],186);
    printf("                                %c            %c\n",186,186);
    printf("                                %c%c%c%c%c%c%c%c%c%c%c%c%c%c",200,205,205,205,205,205,205,205,205,205,205,205,205,188);
    creditos();
    creditos();
    j=0;
    tecla[0]=72;
    while(j<20){
        if(kbhit())
            tecla[j]=getch();
        switch(tecla[j]){
            case 80:
                        j++;
                        system("cls");
                        printf("\n\n\n\n\n\n                                %c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",201,205,205,205,205,205,205,205,205,205,205,205,205,187);
                        printf("                                %c            %c\n",186,186);
                        printf("                                %c%s%c\n",186,menu[0],186);
                        printf("                                %c            %c\n",186,186);
                        printf("                                %c%c%c%c%c%c%c%c%c%c%c%c%c%c",200,205,205,205,205,205,205,205,205,205,205,205,205,188);
                        printf("\n\n\n                                %c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",220,220,220,220,220,220,220,220,220,220,220,220,220,220);
                        printf("                                %c            %c\n",219,219);
                        printf("                                %c%s%c\n",219,menu[1],219);
                        printf("                                %c            %c\n",219,219);
                        printf("                                %c%c%c%c%c%c%c%c%c%c%c%c%c%c",223,223,223,223,223,223,223,223,223,223,223,223,223,223);
                        creditos();
                        break;
            case 72: //norte
                        j++;
                        system("cls");
                        printf("\n\n\n\n\n\n                                %c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",220,220,220,220,220,220,220,220,220,220,220,220,220,220);
                        printf("                                %c            %c\n",219,219);
                        printf("                                %c%s%c\n",219,menu[0],219);
                        printf("                                %c            %c\n",219,219);
                        printf("                                %c%c%c%c%c%c%c%c%c%c%c%c%c%c",223,223,223,223,223,223,223,223,223,223,223,223,223,223);
                        printf("\n\n\n                                %c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",201,205,205,205,205,205,205,205,205,205,205,205,205,187);
                        printf("                                %c            %c\n",186,186);
                        printf("                                %c%s%c\n",186,menu[1],186);
                        printf("                                %c            %c\n",186,186);
                        printf("                                %c%c%c%c%c%c%c%c%c%c%c%c%c%c",200,205,205,205,205,205,205,205,205,205,205,205,205,188);
                        creditos();
                        break;
            case VK_BACK:
            case VK_RETURN:
                        if(tecla[j-1]==72)
                            return;

                        else manual();
            default:        break;
        }
        Sleep(10);
    }
    return 0;
}
