#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TAM 30

char **funcao_de_transicao_estendida(char estado[3],char palavra[TAM]);
int estados_finais(char **estado);
int palavra_vazia(char palavra[TAM]);
int simbolo_diferente(char palavra[TAM]);
char **funcao_de_transicao(char estado[3],char simbolo);
//////////////////////////////////////////////////////////////////////////////
int main(int argc, char** argv) {

    char w[TAM],**resultado;

    printf("**********EH OU NAO DA LINGUAGEM?********** \n");
    printf("Palavra:");
    scanf("%[^\n]s",&w);

if(palavra_vazia(w)==1 || simbolo_diferente(w))
{
    return (EXIT_SUCCESS);
}
else{
    resultado=funcao_de_transicao_estendida("q0",w);
    if(estados_finais(resultado)==1)
    {
        printf("\n Eh da linguagem! \n Estado Final:%s*",resultado);
    }
    else{printf("\n Nao eh da linguagem!");}
}
    return (EXIT_SUCCESS);
}
//////////////////////////////////////////////////////////////////////////////
int palavra_vazia(char palavra[TAM])
{
    if(strcmp(palavra,"")==0)
    {printf("Palavra vazia!");
    return 1 ;}
    return 0;
}
//////////////////////////////////////////////////////////////////////////////
int simbolo_diferente(char palavra[TAM])
{
    int i;
    for(i=0;i<strlen(palavra);i++)
    {
       if(palavra[i]!='a' && palavra[i]!='b')
        {
            printf("Nao eh da linguagem!");
            return 1 ;
        }
    }
    return 0;
}
char **funcao_de_transicao_estendida(char estado[3],char palavra[TAM])
{
    if(palavra[0]==NULL){return (estado);}
    int tamanho=strlen(palavra);
    char a=palavra[tamanho-1];
    palavra[tamanho-1]=NULL;
    return (funcao_de_transicao(funcao_de_transicao_estendida("q0",palavra),a));
}
//////////////////////////////////////////////////////////////////////////////////
char **funcao_de_transicao(char estado[3], char simbolo){
    printf("-> %s ",estado);

     if(estado =="q0" && simbolo == 'b'){
        estado ="q1";
        return estado;
    }
	 if (estado == "q0" && simbolo == 'a'){
		estado = "q2";
		return estado;
	}
     if(estado =="q1" && simbolo == 'a'){
        estado ="q4";
        return estado;
    }
     if(estado =="q1" && simbolo == 'b'){
        estado ="q3";
        return estado;
    }
     if(estado =="q2" && simbolo == 'a'){
        estado ="q6";
        return estado;
    }
     if(estado =="q2" && simbolo == 'b'){
        estado ="q5";
        return estado;
    }
     if(estado =="q3" && simbolo == 'a'){
        estado ="q8";
        return estado;
    }
     if(estado =="q3" && simbolo == 'b'){
        estado ="q7";
        return estado;
    }
     if(estado =="q4" && simbolo == 'a'){
        estado ="q8";
        return estado;
    }
     if(estado =="q4" && simbolo == 'b'){
        estado ="q9";
        return estado;
    }
     if(estado =="q5" && simbolo == 'a'){
        estado ="q8";
        return estado;
    }
     if(estado =="q5" && simbolo == 'b'){
        estado ="q10";
        return estado;
    }
     if(estado =="q6" && simbolo == 'a'){
        estado ="q8";
        return estado;
    }
     if(estado =="q6" && simbolo == 'b'){
        estado ="q11";
        return estado;
    }
     if(estado =="q7" && simbolo == 'a'){
        estado ="q12";
        return estado;
    }
     if(estado =="q7" && simbolo == 'b'){
        estado ="q7";
        return estado;
    }
     if(estado =="q8" && simbolo == 'a'){
        estado ="q8";
        return estado;
    }
     if(estado =="q8" && simbolo == 'b'){
        estado ="q8";
        return estado;
    }
     if(estado =="q9" && simbolo == 'a'){
        estado ="q13";
        return estado;
    }
     if(estado =="q9" && simbolo == 'b'){
        estado ="q10";
        return estado;
    }
     if(estado =="q10" && simbolo == 'a'){
        estado ="q12";
        return estado;
    }
     if(estado =="q10" && simbolo == 'b'){
        estado ="q7";
        return estado;
    }
     if(estado =="q11" && simbolo == 'a'){
        estado ="q13";
        return estado;
    }
     if(estado =="q11" && simbolo == 'b'){
        estado ="q10";
        return estado;
    }
     if(estado =="q12" && simbolo == 'a'){
        estado ="q14";
        return estado;
    }
     if(estado =="q12" && simbolo == 'b'){
        estado ="q9";
        return estado;
    }
     if(estado =="q13" && simbolo == 'a'){
        estado ="q14";
        return estado;
    }
     if(estado =="q13" && simbolo == 'b'){
        estado ="q9";
        return estado;
    }
     if(estado =="q14" && simbolo == 'a'){
        estado ="q15";
        return estado;
    }
     if(estado =="q14" && simbolo == 'b'){
        estado ="q11";
        return estado;
    }
     if(estado =="q15" && simbolo == 'a'){
        estado ="q15";
        return estado;
    }
     if(estado =="q15" && simbolo == 'b'){
        estado ="q11";
        return estado;
    }

    return estado;
}

int estados_finais(char **estado)
{
    if(estado=="q7" ||estado=="q9" ||estado=="q12"||estado=="q14")
        return 1;
    else
        return 0;
}
