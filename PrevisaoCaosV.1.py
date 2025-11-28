# --1° def: extrairemos os dados necessarios ao nosso modelo preditativo--
class previsaoCaos:
    def __init__(self, umid, temp, prs): # --parametros de umidade, temperatura e pressao atmosferica--
        self.umid = umid
        self.temp = temp 
        self.prs = prs 
    
# --2° def: calculamos a instabilidade atmosferica baseada na diferença termica--
    def calcular_instabilidade(self):
        if self.temp >= 30:
            return "Alta"
        elif self.temp >= 25:
            return "Média-Alta"
        elif self.temp >= 25:
            return "Média"
        elif self.temp >= 15:
            return "Baixa"
        else:
            return "Muito baixa"
        
# --3° def: prever a formaçao das nuvens--
    # --umidade(combustivel)--
    def prever_formaçao(self):
        if self.umid < 40:
            base_umidade = "SEM nuvens. O ar está seco, assim como seus pulmões que insitem em trabalhar."
        elif self.umid < 60:
            base_umidade = "POUCAS nuvens. A esperança é a última que morre não é?"
        elif self.umid < 80:
            base_umidade = "Nuvens MODERADAS. Hoje a atmostera está mais indecisa do que você."
        else:
            base_umidade = "MUITAS nuvens. Isso pode ser bom, só depende de você e se tem café ou não."
            
    # --pressao atmosferica(estabilidade ou nao)--
        if self.prs > 1020:
            estabilidade = "ESTÁVEL -- Nuvens amigas da Terra se aproximam."
            tipo_nuvem = "Stratus/Cumulus humilis."
        elif self.prs > 1013:
            estabilidade = "POUCO INSTÁVEL -- Nuvens médias se decidem e tentam arrebentar."
            tipo_nuvem = "Cumulus mediocris/Altocumulus."
        else:
             estabilidade = "INSTANILIDADE -- Nuvens verticais amaçam seu dia, e se caírem é só a natureza das coisas."
    
    # --instabilidade(motor)--
        instab = self.calcular_instabilidade()
        if instab == "Alta" and self.umid > 70:
            desenvolvimento = "O caos é certo, mas a necessidade de guarda-chuva... nem sempre."
        elif instab == "Média-Alta" and self.umid > 65:
            desenvolvimento = "Observe as nuvens, talvez estejam menos nervosas do que você, mas só um pouco."
        elif instab == "Média" and self.umid > 60:
            desenvolvimento = "A umidade caminha lentamente e as nuvens estão com preguiça, assim como você em uma segunda-feira."
        elif instab == "Baixa":
            desenvolvimento = "As nuvens estão cansadas agora. Volte mais tarde... talvez."
        else:
            desenvolvimento = "Você está livre das nuvens por agora, no entanto, não está livre das suas 'obrigações', continue a rolar suas pedras."
        
        return "PREVISÃO DE NUVENS: \n"+ base_umidade + "\n"  + estabilidade + "\n"  + desenvolvimento + "\n" + "TIPO PREDOMINANTE: \n" + tipo_nuvem  


situacao = previsaoCaos (
    umid = 50,
    temp = 10,
    prs = 1025
)
print(situacao.prever_formaçao())

