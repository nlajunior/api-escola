from django.db.models import fields
from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'data_nacimento','cpf', 'foto']

class AlunoSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'data_nacimento','cpf', 'celular', 'foto']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    #representa o curso através da descrição dele
    curso = serializers.ReadOnlyField(source='curso.descricao')
    #representa o campo choice através da sua descrição
    periodo = serializers.SerializerMethodField()
    class Meta:
        model= Matricula
        fields = ['curso', 'periodo']
        #exclude = []
    #Retorna a descrição do período do campo tipo choice
    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source= 'aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']
