#Importação de funções criadas por terceiros
#from graphics import *

#Funções
#1)------------------------------------------------------------------------------------------------------------------------------------
def abertura_do_ficheiro_respostas(ficheiro_dados):
    '''Esta função faz a abertura e processamento do ficheiro com os resultados da pesquisa'''
    file=open(ficheiro_dados,'r',encoding='utf8')
    cabecalho=file.readline(); cabecalho=cabecalho.strip(); cabecalho=cabecalho.split(';')
    lista_respostas=[]
    lista_ingredientes=cabecalho[3:]                
    for linha in file:
        linha=linha.strip(); linha=linha.split(';')
        lista_temp=[]
        for item in linha:
            if item.isalpha():
                lista_temp.append(item)
                continue
            convertido=str(item)
            lista_temp.append(convertido)
        lista_respostas.append(lista_temp)   
    file.close()
    return (lista_respostas,lista_ingredientes,cabecalho)

def abertura_ficheiro_receitas(ficheiro_receitas):
    '''Esta função faz a abertura e processamento do ficheiro com informações das receitas'''
    file_2=open(ficheiro_receitas,'r',encoding='utf8')
    cabecalho_receitas=file_2.readline(); cabecalho_receitas=cabecalho_receitas.strip(); cabecalho_receitas=cabecalho_receitas.split(':')
    lista_receitas=[]
    while '' in cabecalho_receitas:
        cabecalho_receitas.remove('')
    for rec in file_2:
        rec=rec.strip(); rec=rec.split(':')
        while '' in rec:
            rec.remove('')
        lista_temp2=rec[2:]
        rec=rec[:2]
        rec.append(lista_temp2)
        rec[0:1]=[eval(rec[0])]
        lista_receitas.append(rec)
    file_2.close()
    return (cabecalho_receitas,lista_receitas)
#2)------------------------------------------------------------------------------------------------------------------------------------
def quant_alergia(lista_respostas,ingrediente,cabecalho):               
    ''' Esta função conta o número de pessoas que são alérgicas ao ingrediente escolhido'''
    indice=cabecalho.index(ingrediente)
    lista_contagem=[]
    for linha in lista_respostas:
        lista_contagem.append(linha[indice])
    resultado=lista_contagem.count(1)
    return resultado
#3)------------------------------------------------------------------------------------------------------------------------------------   
def ing_mais_alergicos(cabecalho,lista_ingredientes,lista_respostas):
    '''Esta função irá fornecer a informação sobre o ingrediente com maior número de alérgicos'''
    contagem={}
    for ingrediente in lista_ingredientes:
            contagem[ingrediente]=quant_alergia(lista_respostas,ingrediente,cabecalho)          
    lista_comparacao=list(contagem.values())
    mais_alergicos=max(lista_comparacao)
    lista_comparacao.count(mais_alergicos)
    dicionario_respostas={}
    if lista_comparacao.count(mais_alergicos) == 1:
        for chave,valor in contagem.items():
            if valor == mais_alergicos:
                dicionario_respostas[mais_alergicos]=chave
        return dicionario_respostas
    else:
        lista_ings_com_mais_alergicos=[]
        for chave,valor in contagem.items():
            if valor == mais_alergicos:
                lista_ings_com_mais_alergicos.append(chave)
        dicionario_respostas[mais_alergicos]=lista_ings_com_mais_alergicos 
        return dicionario_respostas
#4)--------------------------------------------------------------------------------------------------------------------------------- --  
def ing_menos_alergicos(cabecalho,lista_respostas,lista_ingredientes):
    '''Esta função irá fornecer a informação sobre o ingrediente com menor número de alérgicos'''
    contagem={}
    for ingrediente in lista_ingredientes:
        contagem[ingrediente]=quant_alergia(lista_respostas,ingrediente,cabecalho)
    lista_comparacao=list(contagem.values())
    menos_alergicos=min(lista_comparacao)
    lista_comparacao.count(menos_alergicos)
    dicionario_respostas={}
    if lista_comparacao.count(menos_alergicos) == 1:
        for chave,valor in contagem.items():
            if valor == menos_alergicos:
                dicionario_respostas[menos_alergicos]=chave
        return dicionario_respostas
    else:
        lista_ings_com_menos_alergicos=[]
        for chave,valor in contagem.items():
            if valor == menos_alergicos:
                lista_ings_com_menos_alergicos.append(chave)
        dicionario_respostas[menos_alergicos]=lista_ings_com_menos_alergicos  
        return dicionario_respostas
#5)------------------------------------------------------------------------------------------------------------------------------------
#Função auxiliar 5.1)
def contagem_ingrediente_perigoso_genero(ingrediente,lista_respostas):
    '''Esta função retorna lista de tuplos, em que cada tuplo contém o género e a quantidade de casos de alergia para um dado ingrediente'''
    indice=cabecalho.index(ingrediente)
    lista_genero=[]
    for sujeito in lista_respostas:
        if sujeito[indice] == 1:
            lista_genero.append(sujeito[2])
    return ([ingrediente,lista_genero.count('M')],[ingrediente,lista_genero.count('F')])
#Função Principal 5
def ingrediente_perigoso_genero(genero,lista_ingredientes,lista_respostas):
    '''Esta função faz a contagem e comparação, devolvendo o nome do ingrediente (ou dos no caso de existir empate) mais perigoso para cada género''' 
    dic_masculino={}
    dic_feminino={}
    for ingrediente in lista_ingredientes:
        homens,mulheres=contagem_ingrediente_perigoso_genero(ingrediente,lista_respostas)
        dic_masculino[ingrediente]=homens[1]
        dic_feminino[ingrediente]=mulheres[1]
    if genero=='M':
        lista_comparacao=list(dic_masculino.values())
        mais_perigoso=max(lista_comparacao)             
        if lista_comparacao.count(mais_perigoso) != 1:
            lista_dos_maximos=[]
            for chave,valor in dic_masculino.items():
                if valor==mais_perigoso:
                    lista_dos_maximos.append(chave)
            chaves=','.join(lista_dos_maximos)
            return chaves
        else:
            for chave,valor in dic_masculino.items():
                if valor==mais_perigoso:
                    return chave
    elif genero=='F':
        lista_comparacao=list(dic_feminino.values())
        mais_perigoso=max(lista_comparacao)
        if lista_comparacao.count(mais_perigoso) != 1:
            lista_dos_maximos=[]
            for chave,valor in dic_feminino.items():
                if valor==mais_perigoso:
                    lista_dos_maximos.append(chave)
            chaves=','.join(lista_dos_maximos)
            return chaves
        else:                  
            for chave,valor in dic_feminino.items():
                if valor==mais_perigoso:
                    return chave
#6)------------------------------------------------------------------------------------------------------------------------------------
# Função auxiliar 6.1
def lista_ingredientes_com_pelo_menos_1_alergico(lista_respostas,cabecalho):
    '''Esta função retorna os ingredientes que têm pelo menos um caso de alergia'''
    contagem={}
    l_ing_minimo_1_alergico=[]
    for ingrediente in lista_ingredientes:
            contagem[ingrediente]=quant_alergia(lista_respostas,ingrediente,cabecalho)
    for chave,valor in contagem.items():
        if valor != 0:
            l_ing_minimo_1_alergico.append(chave)
    return l_ing_minimo_1_alergico
#Função Principal 6
def quantidade_alergenios_receita(codigo_receita,lista_respostas,cabecalho):
    '''Esta função irá retornar quantos alergénios tem uma dada receita'''
    d_alergenios_receita={}
    for produto in lista_receitas:
        if produto[0] == codigo_receita:
            acumulador=0
            l_ing_minimo_1_alergico=lista_ingredientes_com_pelo_menos_1_alergico(lista_respostas,cabecalho)
            for ingrediente_f5 in l_ing_minimo_1_alergico:
                if ingrediente_f5 in produto[2]:
                    acumulador=acumulador+1
                    d_alergenios_receita[produto[1]]=acumulador
    return d_alergenios_receita
#7)------------------------------------------------------------------------------------------------------------------------------------      
#Função auxiliar 7.1
def identificacao_alergenios_receita(codigo_receita,lista_receitas,lista_respostas,cabecalho):
    '''Esta função retornará quais os ingredientes alergénios, presentes numa dada receita'''
    d_lista_alergenios_receita={}
    lista_ingredientes_p_receita=[]
    for produto in lista_receitas:
        if produto[0] == codigo_receita:
            l_ing_minimo_1_alergico=lista_ingredientes_com_pelo_menos_1_alergico(lista_respostas,cabecalho)
            for ingrediente_f5 in l_ing_minimo_1_alergico:
                if ingrediente_f5 in produto[2]:
                    lista_ingredientes_p_receita.append(ingrediente_f5)
                    d_lista_alergenios_receita[codigo_receita]=lista_ingredientes_p_receita
    return d_lista_alergenios_receita
#Função Principal 7
def numero_alergicos_pelo_menos_um_ingrediente_receita(codigo_receita,lista_respostas,cabecalho):
    '''Esta função erá retornar o número de pessoas alérgicas a determinada receita'''
    d_lista_alergenios_receita=identificacao_alergenios_receita(codigo_receita,lista_receitas,lista_respostas,cabecalho)
    receita_f6=list(d_lista_alergenios_receita.keys())[0]
    l_alergenios=d_lista_alergenios_receita[receita_f6]
    lista_respostas_trabalho=lista_respostas[:]
    acumulador=0
    lista_contagem=[]
    for ingrediente_f6 in l_alergenios:
        indice=cabecalho.index(ingrediente_f6)
        for linha in lista_respostas_trabalho:
            if linha[indice] == 1:
                acumulador=acumulador+1
                lista_respostas_trabalho.remove(linha)
    return acumulador
#8)------------------------------------------------------------------------------------------------------------------------------------
def relatorio_perigosidade(lista_receitas,lista_respostas):
    '''Esta função irá criar um documento com todas as receitas e com os respectivos números de casos de alergia'''
    relatorio=open('perigo.txt','w')
    d_receitas_f7={}
    for produto_f7 in lista_receitas:
        d_receitas_f7[produto_f7[1]]=produto_f7[0]
    dicionario_f7={}
    for receita_2_f7 in d_receitas_f7:           
        codigo_receita=d_receitas_f7[receita_2_f7]
        n_alergicos_produto_f7=numero_alergicos_pelo_menos_um_ingrediente_receita(codigo_receita,lista_respostas,cabecalho)
        dicionario_f7[receita_2_f7]=n_alergicos_produto_f7
    ordenacao_perigosidade=list(dicionario_f7.values()); ordenacao_perigosidade.sort()
    conjunto_linhas_relatorio=[]
    lista_de_tuplos=list(dicionario_f7.items())
    for n_alergicos_l in ordenacao_perigosidade:
                if lista_de_tuplos != []:
                    for receita_final,n_alergicos_d in lista_de_tuplos:
                        if n_alergicos_l ==n_alergicos_d:
                            string_linha_ficheiro='%s:%d\n' %(receita_final.upper(),n_alergicos_l)
                            conjunto_linhas_relatorio.append(string_linha_ficheiro)
                            lista_de_tuplos.remove((receita_final,n_alergicos_d))
    relatorio.writelines(conjunto_linhas_relatorio)
    relatorio.close()
#9)------------------------------------------------------------------------------------------------------------------------------------
# Função auxiliar do grafico
def funcao_auxiliar_grafico(lista_receitas,lista_respostas):
    '''Esta função devolderá o nome de cada receita e o respectivo número de casos de alergia'''
    d_receitas_f7={}
    for produto_f7 in lista_receitas:
        d_receitas_f7[produto_f7[1]]=produto_f7[0]
    dicionario_f7={}
    for receita_2_f7 in d_receitas_f7:           
        codigo_receita=d_receitas_f7[receita_2_f7]
        n_alergicos_produto_f7=numero_alergicos_pelo_menos_um_ingrediente_receita(codigo_receita,lista_respostas,cabecalho)
        dicionario_f7[receita_2_f7]=n_alergicos_produto_f7
    ordenacao_perigosidade=list(dicionario_f7.values()); ordenacao_perigosidade.sort()
    lista_de_tuplos=list(dicionario_f7.items())
    lista_eixo_x=[]
    lista_eixo_y=[]
    for n_alergicos_l in ordenacao_perigosidade:
                if lista_de_tuplos != []:
                    for receita_final,n_alergicos_d in lista_de_tuplos:
                        if n_alergicos_l ==n_alergicos_d:
                            lista_eixo_x.append(receita_final)
                            lista_eixo_y.append(n_alergicos_d)
                            lista_de_tuplos.remove((receita_final,n_alergicos_d))
    return lista_eixo_x,lista_eixo_y
# Função principal grafico
def grafico_perigosidade(lista_receitas,lista_respostas):
    '''Esta função irá criar um gráfico de barras com o código de cada receita e o número de casos de alergia para cada uma'''
    lista_eixo_x,lista_eixo_y=funcao_auxiliar_grafico(lista_receitas,lista_respostas)
    lista_de_codigos=[]
    lista_receitas_trabalho=lista_receitas[:]
    for receita in lista_eixo_x:
        for produto in lista_receitas_trabalho:
            if produto[1] == receita:
                lista_de_codigos.append(produto[0])
    
    janela=GraphWin('Gráfico de perigosidade',720,350); janela.setBackground('white')
    janela.setCoords(0,0,720,350)       
    eixo_y= Line(Point(40,40), Point(40,320)); eixo_y.draw(janela); eixo_y.setArrow('last'); Text(Point(60,340),'Nº de alérgicos').draw(janela)
    eixo_x= Line(Point(40,40), Point(700,40)); eixo_x.draw(janela); eixo_x.setArrow('last'); Text(Point(650,10),'Código da receita').draw(janela)

    escala=250/max(lista_eixo_y)    
    marcacoes_escala=250/10  
    numeros_escala=max(lista_eixo_y)//10  

    P1_i_e_x=0;P1_i_e_x_acumulador=50
    P1_i_e_y=40
    P2_s_d_x=50;P2_s_d_x_acumulador=640/len(lista_eixo_x)
    ld=40
    le=40
    acumulador_escala=0
    salto=0
    while le <= 310:
        Line(Point(38,le), Point(43,ld)).draw(janela)
        if salto%2 ==0:
            Text(Point(30,le), '%d' %(acumulador_escala)).draw(janela)
        le=le+marcacoes_escala
        ld=ld+marcacoes_escala
        acumulador_escala=acumulador_escala+numeros_escala
        salto=salto+1
    
    for altura_barra in lista_eixo_y:
        P1_i_e_x=P1_i_e_x+P1_i_e_x_acumulador   
        P1_i_e_y=40
        P2_s_d_x=P2_s_d_x+P2_s_d_x_acumulador
        P2_s_d_y_variavel_altura=40+((escala*altura_barra)+(max(lista_eixo_y)%10)) 
        R=Rectangle(Point(P1_i_e_x,P1_i_e_y),Point(P2_s_d_x,P2_s_d_y_variavel_altura)); R.setFill('blue'); R.draw(janela)
        P1_i_e_x_acumulador=P2_s_d_x_acumulador
        codigo_receita_grafico=lista_de_codigos[0]
        lista_de_codigos.remove(codigo_receita_grafico)
        atraso=P2_s_d_x_acumulador/2
        Text(Point(P2_s_d_x-atraso,30), '%s' %(codigo_receita_grafico)).draw(janela)
    
    fechar_grafico=input('\n Para fechar a janela e voltar ao menu principal digite 0: ')
    while fechar_grafico != '0':
                fechar_grafico=input('\n Para fechar a janela e voltar ao menu principal digite 0: ')
    janela.close()
#Menu----------------------------------------------------------------------------------------------------------------------------------
def menu():
    '''Esta função devolverá um menu para que se possa escolher qual ou quais as funções que se quer executar, sem precisar de as executar todas, para se obter a informação desejada'''
    funcionalidade='controlomenuBCP'
    while funcionalidade == 'controlomenuBCP':
        funcionalidade=input("\n Para obter:\n \n O número de pessoas são alérgicas a um ingrediente, digite: 1 \n O ingrediente com maior ou/e menor número de alérgicos, digite: 2 \n O ingrediente mais perigoso para um genero ou para ambos digite: 3 \n Número de alergénios que uma receita contém digite: 4 \n Número de pessoas no estudo que têm alergia a pelo menos um dos ingredientes de um produto\receita digite: 5\n Para obter um relatório de perigosidade com nome da receita e número de alérgicos a mesma digite: 6\n Para visualizar a informação de um relatório de perigosidade graficamente digite: 7 \n \n Para sair do programa digite: 0\n \n Opção: ")
        lista_funcionalidades=['0','1','2','3','4','5','6','7']         #Inicio da Verificação de erros (menu)
        if funcionalidade not in lista_funcionalidades: 
                print('\n A opção selecionada o não existe, por favor tente outra vez!'); menu()  #Fim da verificação de erros (menu)
        #Funcionalidade 1)
        if funcionalidade=='1': 
                ingrediente=input('\n Qual é o ingrediente? ')     
                while ingrediente not in lista_ingredientes:        #Inicio da verificação de erros (funcionalidade 1)
                    print('\n O nome do ingrediente digitado não foi encontrado na base de dados, por favor tente outra vez ou digite 0 para voltar ao menu principal')
                    ingrediente=input(' \n Qual é o ingrediente? ')
                    if ingrediente=='0':
                        menu()      #fim da verificação de erros (funcionalidade 1)
                resultado_funcao1=quant_alergia(lista_respostas,ingrediente,cabecalho)
                print("\n %d pessoa(s) é(são) alérgicas a(o) %s " % (resultado_funcao1,ingrediente))
        #Funcionalidade 2)
        elif funcionalidade=='2':
                subfuncionalidade=input('\n Para saber o:\n \n Ingrediente com mais alérgicos digite: 1\n Ingrediente com menos alérgicos digite: 2\n Ambos digite: 3\n \n Opção:')
                lista_subfuncionalidades=['1','2','3']      #inicio da verificacao de erros (funcionalidade 2)
                while subfuncionalidade not in lista_subfuncionalidades:
                    print('\n A opção selecionada não existe, por favor tente outra vez ou digite 0 para voltar ao menu principal')
                    subfuncionalidade=input('\n Para o:\n \n Ingrediente com mais alérgicos digite: 1\n Ingrediente com menos alérgicos digite: 2\n Ambos digite: 3\n \n Opção:')
                    if subfuncionalidade == '0':
                        menu()          #fim da verificação de erros (funcionalidade 2)
                if subfuncionalidade=='1':
                    resultado_funcao2=ing_mais_alergicos(cabecalho,lista_ingredientes,lista_respostas)
                    string_formatacao=list(resultado_funcao2.values())[0]
                    if type(list(resultado_funcao2.values())[0]) == str:
                        print('\n Ingrediente com maior número de pessoas alérgicas: %s' %(string_formatacao))
                    else:
                        print('\n Ingredientes com maior número de pessoas alérgicas: %s' %(','.join(string_formatacao)))
                elif subfuncionalidade=='2':
                    resultado_funcao3=ing_menos_alergicos(cabecalho,lista_respostas,lista_ingredientes)
                    string_formatacao=list(resultado_funcao3.values())[0]
                    if type(list(resultado_funcao3.values())[0]) == str:
                        print('\n Ingrediente com menor número de pessoas alérgicas: %s' %(string_formatacao))
                    else:
                        print('\n Ingredientes com menor número de pessoas alérgicas: %s' %(','.join(string_formatacao)))
                elif subfuncionalidade=='3':
                    resultado_funcao2=ing_mais_alergicos(cabecalho,lista_ingredientes,lista_respostas)
                    string_formatacao=list(resultado_funcao2.values())[0]
                    if type(list(resultado_funcao2.values())[0]) == str:
                        print('\n Ingrediente com maior número de pessoas alérgicas: %s' %(string_formatacao))
                    else:
                        print('\n Ingredientes com maior número de pessoas alérgicas: %s' %(','.join(string_formatacao)))
                    resultado_funcao3=ing_menos_alergicos(cabecalho,lista_respostas,lista_ingredientes)
                    string_formatacao=list(resultado_funcao3.values())[0]
                    if type(list(resultado_funcao3.values())[0]) == str:
                        print(' Ingrediente com menor número de pessoas alérgicas: %s' %(string_formatacao))
                    else:
                        print(' Ingredientes com menor número de pessoas alérgicas: %s' %(','.join(string_formatacao)))
        #Funcionalidade 3)
        elif funcionalidade == '3':
                subfuncionalidade=input('\n Para saber saber o:\n \n Ingrediente mais perigoso para o género masculino digite: 1\n Ingrediente mais perigoso para o género feminino digite: 2\n Ingrediente mais perigoso para ambos os géneros digite: 3\n \n Opção:')
                lista_subfuncionalidades=['1','2','3']      #Inicio da verificação de erros (funcionalidade 3)
                while subfuncionalidade not in lista_subfuncionalidades:
                    print('\n A opção selecionada não existe, por favor tente outra vez ou digite 0 para voltar ao menu principal')
                    subfuncionalidade=input('\n Para saber o:\n \n Ingrediente mais perigoso para o género masculino digite: 1\n Ingrediente mais perigoso para o género feminino digite: 2\n Ingrediente mais perigoso para ambos os géneros digite: 3\n \n Opção:')
                    if subfuncionalidade == '0':
                        menu()          #Fim da verificação de erros (funcionalidade 3)
                if subfuncionalidade=='1':
                    genero='M'
                    resultado=ingrediente_perigoso_genero(genero,lista_ingredientes,lista_respostas)
                    print('\n Ingrediente(s) mais perigoso(s) para os homens: %s' %(resultado))
                elif subfuncionalidade=='2':
                    genero='F'
                    resultado=ingrediente_perigoso_genero(genero,lista_ingredientes,lista_respostas)
                    print('\n Ingrediente(s) mais perigoso(s) para as mulheres: %s' %(resultado))
                else:
                    genero='M'
                    resultado=ingrediente_perigoso_genero(genero,lista_ingredientes,lista_respostas)
                    print('\n Ingrediente(s) mais perigoso(s) para os homens: %s' %(resultado))
                    genero='F'
                    resultado=ingrediente_perigoso_genero(genero,lista_ingredientes,lista_respostas)
                    print(' Ingrediente(s) mais perigoso(s) para as mulheres: %s' %(resultado))
        #Funcionalidade 4)            
        elif funcionalidade == '4':
                print('\n Escolha uma receita da seguinte lista e digite o código:')
                for lista_de_cada_receita in lista_receitas:
                    print('\n Receita %s, código: %d' %( lista_de_cada_receita[1],lista_de_cada_receita[0]))
                codigo_receita=input('\n Código: ')
                while codigo_receita.isalpha():     #Inicio primeira verificação de erros (Para o caso da opção digitada ser uma string)
                    print('\n O código é composto apenas por número(s), por favor tente outra vez ou digite 0 para voltar ao menu principal')
                    codigo_receita=input('\n Código: ')
                    if codigo_receita == '0':
                        menu()             #fim da primeira verificação de erros (Para o caso da opção digitada ser uma string)
                codigo_receita=eval(codigo_receita)
                lista_opcoes=[]         # Inicio da segunda verificação de erros
                for codigo in lista_receitas:
                    lista_opcoes.append(codigo[0])
                while codigo_receita not in lista_opcoes:
                    print('\n A opção selecionada não existe, por favor tente outra vez ou digite 0 para voltar ao menu principal')
                    codigo_receita=eval(input('\n Código: '))
                    if codigo_receita == 0:
                        menu()          # Fim da segunda verificação de erros
                resultado_funcao4=quantidade_alergenios_receita(codigo_receita,lista_respostas,cabecalho)
                receita_f3=(resultado_funcao4.keys()); receita_f3=list(receita_f3)[0]
                n_alergenios=resultado_funcao4[receita_f3]
                print('\n %d ingrediente(s) da receita %s estão sinalizados com casos de alergias' %(n_alergenios,receita_f3))         
        #Funcionalidade 5)
        elif funcionalidade == '5':
                print('\n Escolha uma receita da seguinte lista e digite o código:')
                for lista_de_cada_receita in lista_receitas:
                    print('\n Receita %s, código: %d' %( lista_de_cada_receita[1],lista_de_cada_receita[0]))
                codigo_receita=input('\n Código: ')
                while codigo_receita.isalpha():     #Inicio primeira verificação de erros (Para o caso da opção digitada ser uma string)
                    print('\n O código é composto apenas por número(s), por favor tente outra vez ou digite 0 para voltar ao menu principal')
                    codigo_receita=input('\n Código: ')
                    if codigo_receita == '0':
                        menu()             #fim da primeira verificação de erros (Para o caso da opção digitada ser uma string)
                codigo_receita=eval(codigo_receita)
                lista_opcoes=[]         # Inicio da segunda verificação de erros
                for codigo in lista_receitas:
                    lista_opcoes.append(codigo[0])
                while codigo_receita not in lista_opcoes:
                    print('\n A opção selecionada não existe, por favor tente outra vez ou digite 0 para voltar ao menu principal')
                    codigo_receita=eval(input('\n Código: '))
                    if codigo_receita == 0:
                        menu()          # Fim da segunda verificação de erros
                resultado_funcao5=numero_alergicos_pelo_menos_um_ingrediente_receita(codigo_receita,lista_respostas,cabecalho)
                receita_funcao5=list(quantidade_alergenios_receita(codigo_receita,lista_respostas,cabecalho).keys())[0]
                print('\n %d pessoa(s) do estudo têm alergia a pelo menos um ingrediente da receita %s' %(resultado_funcao5,receita_funcao5))
        #Funcionalidade 6)
        elif funcionalidade == '6':
                relatorio_perigosidade(lista_receitas,lista_respostas)
                print(' \n O seu relatório esta pronto e encontra-se na pasta do programa. \n Obrigado.')
        #Funcionalidade 7)
        elif funcionalidade == '7':
                print('\n Lista das receitas e respectivos códigos:')
                for lista_de_cada_receita in lista_receitas:
                    print('\n Receita %s, código: %d' %( lista_de_cada_receita[1],lista_de_cada_receita[0]))
                grafico_perigosidade(lista_receitas,lista_respostas)
        elif funcionalidade == '0':
            break       
        funcionalidade= 'controlomenuBCP'
#Main program--------------------------------------------------------------------------------------------------------------------------

#Abertura e processamento dos ficheiros
print('\n Bem vindo, \n Por favor introduza os nomes dos ficheiros a serem usados')
ficheiro_dados=input('\n Nome do ficheiro com os dados:')
lista_respostas,lista_ingredientes,cabecalho=abertura_do_ficheiro_respostas(ficheiro_dados)
ficheiro_receitas=input('\n Nome do ficheiro com os dados das receitas:')
cabecalho_receitas,lista_receitas=abertura_ficheiro_receitas(ficheiro_receitas)

#Função menu
menu()
exit()
