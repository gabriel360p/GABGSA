from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404 as error404
from .models import Alunos, Professores, Turmas, Materias
from .models import Alunosdaturma as ADT
from . import urls

def viewdash1(request):
	return render(request,'dashboard.html')

# -------------------------------------------------------------------------------------------------

def viewpAlunos(request):
	return render(request,'aluno/pAlunos.html')

def viewnvaluno(request):
	return render(request,'aluno/nvAluno.html')

def viewalunos(request):
	allAlunos = Alunos.objects.all()
	return render(request,'aluno/alunos.html',{'alunos':allAlunos})

def viewchamada(request):
	allAlunos = Alunos.objects.all()
	return render(request,'aluno/chamada.html',{'alunos':allAlunos})

def defcadAluno(request):
	if request.method=="POST":
		nomeinput = request.POST.get('nome')
		matriculainput = request.POST.get('matricula')
		emailinput = request.POST.get('email')
		serieinput = request.POST.get('serie')

		try:
			pegaEmail = Alunos.objects.filter(aluemail=emailinput)
			if pegaEmail:
				return render(request,'aluno/nvAluno.html',{'messageAlert':"Email já Cadastrado",'saveNome':nomeinput,'saveEmail':emailinput,'saveMatricula':matriculainput,})
			else:
				try:
					aluno = Alunos(alunome=nomeinput,alumatricula=matriculainput,aluemail=emailinput,aluserie=serieinput)
					aluno.save()

					return render(request,'aluno/nvAluno.html',{'messageAlert':"Aluno Cadastrado"})
				except Exception as e101:
					print(e101)
					return render(request,'aluno/nvAluno.html',{'messageAlert':"Erro ao cadastrar Aluno (101)",'saveNome':nomeinput,'saveEmail':emailinput,'saveMatricula':matriculainput,'saveSerie':serieinput})
		
		except Exception as e105: 
			print(e105)
			return HttpResponse("Ocorreu um erro no banco (105)")
	else:
		return HttpResponse("Acesso Get Negado")

		

def defdelaluno(request,alucodigo):
	allAlunos = Alunos.objects.all()
	try: 
		selectaluno = error404(Alunos,alucodigo=alucodigo)
		selectaluno.delete()
		return render(request,'aluno/alunos.html',{'messageAlert2':"Aluno Apagado",'alunos':allAlunos})
	except: 
		return render(request,'aluno/alunos.html',{'alunos':allAlunos,'nothing':"Sem Alunos Cadastrados"})



def defeditaluno (request, alucodigo):
	allAlunos = Alunos.objects.all()	
	try: 
		alu=error404(Alunos,alucodigo=alucodigo)
		alu.alunome = request.POST.get('nome')
		alu.alumatricula = request.POST.get('matricula')
		alu.aluemail = request.POST.get('email')
		alu.aluserie = request.POST.get('serie')
		alu.save()
		print(allAlunos)
		return render(request,'aluno/alunos.html',{'messageAlert3':"Alterações Salvas",'alunos':allAlunos})

	except Exception as e110 :
		print(e110)
		print(allAlunos)
		return render(request,'aluno/alunos.html',{'messageAlert3':"Ocorreu um erro ao salvar",'alunos':allAlunos})


def deffaltaluno (request, alucodigo):
	allAlunos = Alunos.objects.all()	
	try: 
		alu=error404(Alunos,alucodigo=alucodigo)
		alu.alufaltas = request.POST.get('faltas')
		alu.save()
		return render(request,'aluno/chamada.html',{'messageAlert6':"Faltas Salvas",'alunos':allAlunos})

	except Exception as e111 :
		print(e111)
		return render(request,'aluno/chamada.html',{'messageAlert6':"Ocorreu um erro ao salvar Faltas",'alunos':allAlunos})

	
# -------------------------------------------------------------------------------------------------


def viewpProfessores(request):
	return render(request,'professor/pProfessores.html')

def viewnvProfessor(request):
	allmaterias = Materias.objects.all()
	
	return render(request,'professor/nvProfessor.html',{'materias':allmaterias})

def viewprofessores(request):
	allprofessores = Professores.objects.all()

	return render(request,'professor/professores.html',{'professores':allprofessores})
 
def defcadProfessor(request):
	if request.method=="POST":
		allmaterias = Materias.objects.all()

		nomeinput = request.POST.get('nome')
		matriculainput = request.POST.get('matricula')
		emailinput = request.POST.get('email')
		materiainput = request.POST.get('materia')

		try:
			pegaEmail = Professores.objects.filter(proemail=emailinput)
			if pegaEmail:
				return render(request,'professor/nvProfessor.html',{'messageAlert':"Email já Cadastrado",'saveNome':nomeinput,'saveEmail':emailinput,'saveMateria':materiainput,'materias':allmaterias})
			else:
				try:
					professor = Professores(pronome=nomeinput,promatricula=matriculainput,proemail=emailinput,promateria=materiainput)
					professor.save()

					return render(request,'professor/nvProfessor.html',{'messageAlert':" Professor Cadastrado",'materias':allmaterias})
				except Exception as e101:
					print(e101)
					return render(request,'professor/nvProfessor.html',{'messageAlert':"Erro ao cadastrar Professor (101)",'saveNome':nomeinput,'saveEmail':emailinput,'saveMatricula':matriculainput,'saveMateria':materiainput,'materias':allmaterias})
		
		except Exception as e105: 
			print(e105)
			return HttpResponse("Ocorreu um erro no banco (105)")
	else:
		return HttpResponse("Acesso Get Negado")


def defdelprofessor(request,procodigo):
	allprofessores = Professores.objects.all()
	try: 
		selectprofessor = error404(Professores,procodigo=procodigo)
		selectprofessor.delete()
		return render(request,'professor/professores.html',{'messageAlert2':"Professor Apagado",'professores':allprofessores})
	except: 
		return render(request,'professor/professores.html',{'professores':allprofessores,'nothing':"Sem Professores Cadastrados"})

def defeditprofessor(request, procodigo):
	allprofessores = Professores.objects.all()
	try: 
		pro=error404(Professores,procodigo=procodigo)
		pro.pronome = request.POST.get('nome')
		pro.promatricula = request.POST.get('matricula')
		pro.proemail = request.POST.get('email')
		pro.promateia = request.POST.get('materia')
		pro.save()
		return render(request,'professor/professores.html',{'messageAlert3':"Alterações Salvas",'professores':allprofessores})

	except Exception as e110 :
		print(e110)
		return render(request,'professor/professores.html',{'messageAlert3':"Ocorreu um erro ao salvar",'professores':allprofessores})

 # -------------------------------------------------------------------------------------------------

def viewpTurmas(request):
	allturmas = Turmas.objects.all()
	return render(request,'turma/pTurmas.html',{'turmas':allturmas})

def viewnvTurma(request):
	allmaterias=Materias.objects.all()
	allprofessores=Professores.objects.all()
	return render(request,'turma/nvTurma.html',{'materias':allmaterias,'professores':allprofessores})

def viewverTurma(request,turcodigo):
	adtalu = ADT.objects.all()
	allalunos = Alunos.objects.all()

	try:
		pegadt = ADT.objects.get(adtcodigo=turcodigo)
		return render(request,'turma/verTurma.html',{'levaadt':pegadt,'alunos':allalunos,'mandaID':turcodigo,'adtalunos':adtalu})
	except:
		allturmas = Turmas.objects.all()
		return render(request,'turma/pTurmas.html',{'turmas':allturmas,'messageAlert6':"Erro ao Acessar Turma"})

def defcadturma(request):
	allprofessores=Professores.objects.all()
	allmaterias=Materias.objects.all()
		
	if request.method=="POST":
		professorinput = request.POST.get('professor')
		materiainput = request.POST.get('materia')

		try:
			turma=Turmas(turmatnome=materiainput,turpronome=professorinput)
			turma.save();
			pegaturma = error404(Turmas,turmatnome=materiainput)

			adt = ADT(adtturnome=materiainput,adtpronome=professorinput,adtturcodigo=pegaturma.turcodigo)
			adt.save()

			return render(request,'turma/nvTurma.html',{'messageAlert':"Turma Cadastrada",'materias':allmaterias,'professores':allprofessores})

		except Exception as e211:
			print(e211)
			return render(request,'turma/nvTurma.html',{'messageAlert':"Erro ao Cadastrar Turma",'materias':allmaterias,'professores':allprofessores})
	else:
		return HttpResponse("Acesso Get Negado")

def defdelturma(request,turcodigo):
	allturmas = Turmas.objects.all()

	try:
		selectturma = error404(Turmas,turcodigo=turcodigo)
	except:
		return render(request,'turma/pTurmas.html',{'turmas':allturmas,'messageAlert':"Turma Desativada"})

	try:
		selectturma.delete()
		return render(request,'turma/pTurmas.html',{'turmas':allturmas,'messageAlert':"Turma Desativada"})
	except Exception as e123:
		print(e123)
		return render(request,'turma/pTurmas.html',{'turmas':allturmas})


#funcionou mais ou menos, não do jeito que estava previsto a funcionar

def defcadalunoadt(request,mandaID):
	allalunos = Alunos.objects.all()
	adtalu = ADT.objects.all()
	adtpega = error404(ADT,adtcodigo = mandaID )
	
	alunoinput = request.POST.get('aluno')
	
	adtpega = ADT(adtalunome=alunoinput)
	adtpega.save()

	allalunos = Alunos.objects.all()
	pegadt = error404(ADT,adtcodigo=mandaID)
	return render(request,'turma/verTurma.html',{'mandaID':mandaID,'levaadt':pegadt,'adtalunos':adtalu,'messageAlert5':"Aluno Cadastrado na Turma",'alunos':allalunos})


 # -------------------------------------------------------------------------------------------------

def viewmaterias(request):
	allmaterias=Materias.objects.all()		

	return render(request,'materia/materias.html',{'materias':allmaterias})

def defnvmateria(request):
	if request.method=="POST":
		allmaterias=Materias.objects.all()
		materiainput = request.POST.get('materia')
		try:
			pegaMateria = Materias.objects.filter(matnome = materiainput)
			if pegaMateria:
				return render(request,'materia/materias.html',{'messageAlert':"Matéria já Cadastrado",'saveMateria':materiainput,'materias':allmaterias})
			else:
				try:
					materia = Materias(matnome=materiainput)
					materia.save()

					return render(request,'materia/materias.html',{'messageAlert':"Matéria Cadastrada",'materias':allmaterias})
				except Exception as e101:
					print(e101)
					return render(request,'materia/materias.html',{'messageAlert':"Erro ao Cadastrar Matéria",'saveMateria':materiainput,'materias':allmaterias})
		
		except Exception as e105: 
			print(e105)
			return HttpResponse("Ocorreu um erro no banco (105)")
	else:
		return HttpResponse("Acesso Get Negado")


def defeditmateria(request, matcodigo):
	allmaterias=Materias.objects.all()
	try: 
		mat=error404(Materias,matcodigo=matcodigo)
		mat.matnome = request.POST.get('materia')
		mat.save()
		return render(request,'materia/materias.html',{'messageAlert3':"Alterações Salvas",'materias':allmaterias})

	except Exception as e110 :
		print(e110)
		return render(request,'materia/materias.html',{'messageAlert3':"Ocorreu um erro ao salvar",'materias':allmaterias})

def defdeltmateria(request,matcodigo):
	allmaterias = Materias.objects.all()
	try: 
		selectmateria = error404(Materias,matcodigo=matcodigo)
		selectmateria.delete()
		return render(request,'materia/materias.html',{'messageAlert2':"Matéria Apagado",'materias':allmaterias})
	except: 
		return render(request,'materia/materias.html',{'materias':allmaterias,'nothing':"Sem Matérias Cadastradas"})
