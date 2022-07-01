class empresa:
    def __init__(self, nome = "SemNome", tipo = "SemTipo", id = "SemId",nome_repr = "SemRepresent",id_repr = "SemIdRepresent"):
        self.nome = nome
        self.tipo = tipo
        self.id = id

        self.nome_repr = nome_repr
        self.id_repr = id_repr
    
    class endereco:
        def __init__(self,rua,bairro,cep,complemento,cidade,estado,rua_repr,bairro_repr,cep_repr,complemento_repr,cidade_repr,estado_repr):
            self.rua = rua
            self.bairro = bairro
            self.cep = cep
            self.complemento = complemento
            self.cidade = cidade
            self.estado = estado
            
            self.rua_repr = rua_repr
            self.bairro_repr = bairro_repr
            self.cep_repr = cep_repr
            self.complemento_repr = complemento_repr
            self.cidade_repr = cidade_repr
            self.estado_repr = estado_repr


