#Alunos: MARIANA BRITO e VITOR GONCALVES
Operador = 0
Operando = 1
NULL = None
#-------------------------------------------CLASSES--------------------------------------------------- 
	#1 - Pilha
	#2 - Transicoes
	#3 - Automato (base, une_alfabeto, concatenacao, uniao, fechodeKleene)
class Stack: #Constructor creates a list 
    def __init__(self):     
        self.stack = list()
         #Adding elements to stack 
    def push(self,data): #Checking to avoid duplicate entries 
            self.stack.append(data) 
            return True  
    def pop(self): 
        if len(self.stack)<=0: 
            return "" 
        return self.stack.pop() #Getting the size of the stack 
    def size(self): 
        return len(self.stack) 
    def top(self):
        top=self.pop()
        self.push(top)
        return top
           
class Automato:
    def __init__(self):
        self.alfabeto = []
        self.estados = []
        self.qtEstados =int
        self.Matrix={}
        self.estadoInicial = int
        self.estadofinal = int
        self.estadosfinais = []
        self.qtEstadosFinais = int
        
    def une_alfabeto(self,a,b):
        i=0
        j=0
        alfabtotal=[]
        alfabtotal.append(a)
        while i < len(alfabtotal):
            while j<len(b):
                if alfabtotal[i] != b[j]:
                    j+=1
                else:
                    k=j
                    while k < len(b)-1:
                        b[k]=b[k+1]
                        k+=1 
                    del(b[len(b)-1])
            i+=1
                       
        if len(b) != 0:    
            alfabtotal.append(b)
        return alfabtotal

    def base(self, simbolo):
        base=Automato()
        base.alfabeto.append(simbolo)
        base.qtEstados=2
        base.estados.append(0)
        base.estados.append(1)
        
        base.Matrix[(0,simbolo)]=1
        
        #print(" 00:",self.Matrix[0][0].qtEstados )
        #print(" 10:",self.Matrix[1][0].qtEstados )
        base.estadoInicial=0
        base.qtEstadosFinais=1
        base.estadosfinais.append(1)
        return base
        
    def concatenacao(self,a,b):
        novo=Automato()
        novo.alfabeto.append(novo.une_alfabeto(a.alfabeto,b.alfabeto))
        print("Alfabeto TOTAL: ",novo.alfabeto)
        
        novo.qtEstados=a.qtEstados+b.qtEstados
        novo.estados.append(a.estados)
        for x in range(0,len(b.estados)):
            b.estados[x] += a.qtEstados 
        novo.estados.append(b.estados)
        print("Estados TOTAIS: ",novo.estados)
        
        novo.Matrix=a.Matrix.copy()
        for i in b.Matrix.keys():
            try:
                novo.Matrix[(i[0] + a.qtEstados, i[1])]= b.Matrix.get(i) + a.qtEstados
            except:
                b= list(b.Matrix.get(i)) 
                new_list = [x + a.qtEstados for x in b]
                novo.Matrix[(i[0] +a.qtEstados,i[1])]=tuple(new_list)
        novo.Matrix[(a.qtEstados - 1,'&')] = a.qtEstados
        print(novo.Matrix)      
        novo.estadoInicial=0
        novo.estadosfinais.append(novo.qtEstados - 1)
        novo.qtEstadosFinais=1
        return novo
        
    def uniao(self,a,b):
        novo=Automato()
        novo.alfabeto=novo.une_alfabeto(a.alfabeto,b.alfabeto)
        novo.qtEstados=a.qtEstados+b.qtEstados + 2
        
        for i in range(novo.qtEstados):
            novo.estados.append(i)

        novo.Matrix[(0,'&')] = a.estadoInicial + 1, b.estadoInicial + a.qtEstados +1 
        for i in a.Matrix.keys():
            try:
                novo.Matrix[ (i[0]+1, i[1] ) ] = a.Matrix.get(i) + 1
                print(novo.Matrix)
            except TypeError :
                print(a.Matrix.get(i))
                b = list(a.Matrix.get(i))
                new_list = [x+1 for x in b]
                a.Matrix[ (i[0]+1, i[1] ) ] = tuple(new_list)
        print("Transicao 1", novo.Matrix)
        # transicao do automato 2       
        for i in b.Matrix.keys():
            try: 
                novo.Matrix[ (i[0]+a.qtEstados + 1, i[1] ) ] = b.Matrix.get(i) + a.qtEstados + 1
            except TypeError :
                b = list(b.Matrix.get(i))
                new_list = [x+a.qtEstados + 1 for x in b]
                novo.Matrix[ (i[0]+a.qtEstados + 1, i[1] ) ] = tuple(new_list)
        print("Transicao 2", novo.Matrix)
        print (a.qtEstados)
        if ((a.qtEstados, '&')) in novo.Matrix.keys():
            novo.Matrix[(a.qtEstados,'&')] = a.Matrix.get((a.qtEstados, '&')), novo.qtEstados-1
        else:
            novo.Matrix[(a.qtEstados,'&')] = novo.qtEstados-1
        print("Transicao 1.1", novo.Matrix)
        # chave existe automato 2
        print (b.qtEstados+a.qtEstados)
        if (b.qtEstados+a.qtEstados, '&') in novo.Matrix.keys():
            novo.Matrix[( b.qtEstado+a.qtEstados,'&')] = b.Matrix.get((b.qtdEstados+a.qtEstados, '&')), novo.qtEstados-1
        else:
            novo.Matrix[(b.qtEstados + a.qtEstados,'&')] = novo.qtEstados-1
        print("Transicao 2.1", novo.Matrix)
        
        novo.estadoInicial=0
        novo.estadosfinais.append(novo.qtEstados - 1)
        novo.qtEstadosFinais=1
        return novo
        
    def fechoDeKleene(self,a):
        novo=Automato()
        novo.alfabeto=novo.une_alfabeto(a.alfabeto,[""])
        novo.qtEstados=a.qtEstados + 2
        for i in range(len(novo.estados)):
            novo.estados.append(i)
        
        for i in novo.Matrix.keys():
            try:
                novo.Matrix[(i[0]+1,i[1])] = novo.Matrix.get(i) + (novo.qtd_Estados - a.qtEstados) - 1
            except:
                print(i)
                b=list(a.Matrix.get(i))
                print(b)
                new_list=[x+1 for x in b]
                print('Transicoes', new_list)
                novo.Matrix[(i[0]+1,i[1])] =tuple(new_list)
                print(novo.Matrix[i[0]+1,i[1]])
        novo.Matrix[(0,'&')]=(1,novo.qtEstados-1)
        novo.Matrix[(novo.qtEstados,'&')]=(novo.qtEstados-a.qtEstados-1,novo.qtEstados-1)
        novo.estadoInicial=0
        novo.estadosfinais.append(novo.qtEstados - 1)
        novo.qtEstadosFinais=1
        return novo
#-------------------------------------------FUNCOES---------------------------------------------------    
	#1 - Eh operador ou operando
	#2 - Concatenacao implicita
def ehop(simb):
    if simb == '(' or simb == ')' or simb == '*' or simb == '.' or simb == '+':
        return Operador    
    else:
        return Operando

def imp(exp):
    aux = ""
    x = 0
    if len(exp) > 1:

        for x in range(0, len(exp)-1):
            # while (x < (len(exp)-1)) :
            if (exp[x] == '.' and ehop(exp[x + 1]) == 1) or (exp[x] == '.' and exp[x + 1] == '(') or (
                    ehop(exp[x]) == 1 and exp[x + 1] == '.') or (exp[x] == '*' and exp[x + 1] == '.') or (
                    exp[x] == '.' and exp[x + 1] == '*') or (exp[x] == ')' and exp[x + 1] == '.'):
                return exp
            if exp[x] == '*' and ehop(exp[x + 1]) == 1:  # *a
                aux += exp[x] + "." #+ exp[x + 1]

            elif exp[x] == '*' and exp[x + 1] == '(':  # *(
                aux += exp[x] + "." #+ exp[x + 1]

            elif exp[x] == ')' and exp[x + 1] == '(':  # )(
                aux += exp[x] + "." #+ exp[x + 1]

            elif ehop(exp[x]) == 1 and ehop(exp[x + 1]) == 1:  # aa
                aux += exp[x] + "." #+ exp[x + 1]

            elif ehop(exp[x]) == 1 and exp[x + 1] == '(':  # a(
                aux += exp[x] + "." #+ exp[x + 1]

            elif exp[x] == ')' and ehop(exp[x + 1]) == 1:  # )a
                aux += exp[x] + "." #+ exp[x + 1]


            else:
                aux += exp[x]
        aux += exp[-1]
        return aux
    else:
        return exp
#-------------------------------------------TRABALHO_1---------------------------------------------------


expressao=input('Entre com a expressão\n')
aux = imp(expressao)
expressao = aux
print('expressão: ', aux)
posfixa = ""
pilha = Stack()
for x in range(0,len(expressao)):
    if ehop(expressao[x]) == 1:
        posfixa += expressao[x]
    else:
        #print('pilha: ', pilha.top())
        if expressao[x] == '(':
            pilha.push(expressao[x])
        elif expressao[x] == ')':
            while (pilha.top() != '(') :
                print('pilha: ', pilha.top())
                posfixa += pilha.pop()
            
            pilha.pop()
        else:
            while expressao[x] == '*' and pilha.top() =='*' or expressao[x] == '+' and pilha.top() =='+' or expressao[x] == '.' and pilha.top() =='.' or expressao[x] == '+' and pilha.top() =='*' or expressao[x] == '.' and pilha.top() =='*' or expressao[x] == '+' and pilha.top() =='.':
               # print('pilha: ', pilha.top())
                posfixa += pilha.pop()
            pilha.push(expressao[x])
    
while pilha.size() != 0 :
    #print('pilha: ', pilha.top())
    posfixa += pilha.pop()
    
p2 =Stack()
for y in range(0, len(posfixa)):
    simbolo = posfixa[y]
    if ehop(simbolo) == 1:
        p2.push(simbolo)
    else:
        if p2.top() != NULL:
            op2 = p2.pop()
            if simbolo == '*':
                valor = "asdasd"
                p2.push(valor)
            else:
                if p2.top() != NULL:
                    op1 = p2.pop()
                    valor = "asdasdasd2"
                    p2.push(valor)
                else:
                    print("deu ruim")
        else:   
            print("deu ruim")            
op1 = p2.pop()
if p2.top() == NULL:
    print('Deu bom')
    
print('posfixa:final ', posfixa)
print('pilha:final ',pilha.size())
#-------------------------------------------TRABALHO_2---------------------------------------------------
aut=Automato()
for x in range(0,len(posfixa)):
    simbolo=posfixa[x]
    print("Simbolo da vez:", simbolo)
    if ehop(simbolo) == 1:
        pilha.push(aut.base(simbolo))
    else:
        if pilha.top() != NULL:
            if simbolo == '*':
                pilha.push(aut.fechoDeKleene(pilha.pop()))
            else:
                op2=pilha.pop()
                if pilha.top() != NULL:
                    op1=pilha.pop()
                    if simbolo == '.':
                        pilha.push(aut.concatenacao(op1,op2))
                    else:
                        if simbolo == '+':
                            pilha.push(aut.uniao(op1,op2))
afd=pilha.pop()
#if pilha.top() == NULL:
#   print ('AFD: final ',afd)