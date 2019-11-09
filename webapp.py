import os
import sys
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

######### Rotas relacionadas a pontos #########
##Consulta de Pontos
@app.route("/pontos", methods=['GET'])
def getPontos():
    try:
        #Conecta com o Banco de dados
        con = sqlite3.connect('agendamento.db')
        cur = con.cursor()
        #Recebe todos os pontos em uma lista
        pontos = []
        #Transforma cada entrada em um Dicionario
        cur.execute("SELECT * FROM pontos")
        for linha in cur.fetchall():
            dicionario = {"ID": str(linha[0]),"Nome": str(linha[1]), "Endereco": str(linha[2])}
            pontos.append(dicionario)

        con.close()                   
        if len(pontos) != 0:
            return jsonify(pontos), 200
            con.close()
        else:
            return jsonify(pontos), 404   
            con.close()
    
    except Exception as ex:
        return jsonify({"status":"ERRO", "msg":str(ex)}), 500

######### Rotas relacionadas a agendamentos #########
##Consulta de Agendamentos
@app.route("/agendamento/<int:id>", methods=['GET'])
def getAgendamento(id):
    try:
        #Conecta com o Banco de dados
        con = sqlite3.connect('agendamento.db')
        cur = con.cursor()
        #Recebe todos os pontos em uma lista
        agendamentos = []
        #Monta a Query
        CSQL = "SELECT * FROM agendamento WHERE cd_agendamento = {}".format(id)
        #Transforma cada entrada em um Dicionario
        cur.execute(CSQL)
        for linha in cur.fetchall():
            dicionario = {"cd_agendamento": str(linha[0]),"cliente_nm": str(linha[1]), "dt_agendamento": str(linha[2])}
            agendamentos.append(dicionario)

        con.close()            
        if len(agendamentos) != 0:
            return jsonify(agendamentos), 200

        else:
            return jsonify(agendamentos), 404   
    
    except Exception as ex:
        return jsonify({"status":"ERRO", "msg":str(ex)}), 500

##Exclusão de Agendamentos
@app.route("/agendamento/<int:id>", methods=['DELETE'])
def deleteAgendamento(id):
    try:
        #Conecta com o Banco de dados
        con = sqlite3.connect('agendamento.db')
        cur = con.cursor()
        #Recebe todos os pontos em uma lista
        agendamentos = []
        #Monta a Query de retorno
        CSQL = "SELECT * FROM agendamento WHERE cd_agendamento = {}".format(id)
        #Transforma cada entrada em um Dicionario
        cur.execute(CSQL)
        for linha in cur.fetchall():
            dicionario = {"cd_agendamento": str(linha[0]),"cliente_nm": str(linha[1]), "dt_agendamento": str(linha[2])}
            agendamentos.append(dicionario)

        #Executa a deleção
        CSQL = "DELETE FROM agendamento WHERE cd_agendamento = {}".format(id)
        #Transforma cada entrada em um Dicionario
        cur.execute(CSQL)
        con.commit()
        con.close()
        if len(agendamentos) != 0:
            return jsonify(agendamentos), 200
        else:
            return jsonify(agendamentos), 404   
    
    except Exception as ex:
        return jsonify({"status":"ERRO", "msg":str(ex)}), 500

##Adição de Agendamentos
@app.route("/agendamento/", methods=['POST'])
def adicionaAgendamento():
    try:
        novo_agendamento = request.get_json()
        #Conecta com o Banco de dados
        con = sqlite3.connect('agendamento.db')
        cur = con.cursor()
        #Recebe todos os pontos em uma lista
        agendamentos = []
        #Monta a Query de adição
        CSQL = "INSERT INTO agendamento(cliente_nm, dt_agendamento) VALUES({},{})".format(novo_agendamento['cliente_nm'], novo_agendamento['dt_agendamento'])
        #Executa a adição
        cur.execute(CSQL)
        con.commit()
        #Pega o id da ultima linha adicionada
        lastId = cur.lastrowid()
        CSQL = "SELECT * FROM agendamento WHERE cd_agendamento = {}".format(lastId)
        #Transforma cada entrada em um Dicionario
        cur.execute(CSQL)


        #Executa uma busca desse id no banco
        for linha in cur.fetchall():
            dicionario = {"cd_agendamento": str(linha[0]),"cliente_nm": str(linha[1]), "dt_agendamento": str(linha[2])}
            agendamentos.append(dicionario)

        #Executa a deleção
        CSQL = "DELETE FROM agendamento WHERE cd_agendamento = {}".format(id)
        #Transforma cada entrada em um Dicionario
        cur.execute(CSQL)
        con.commit()
        con.close()
        if len(agendamentos) != 0:
            return jsonify(agendamentos), 200
        else:
            return jsonify(agendamentos), 404   
    
    except Exception as ex:
        return jsonify({"status":"ERRO", "msg":str(ex)}), 500

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)


