from django.urls import path
from . import views

app_name = 'chamada'

urlpatterns = [
	path('',views.viewdash1,name="viewdash1"),
	path('index',views.viewdash1,name="viewdash1"),
	# -------------------------------------------------------------------------------
	path('pAlunos/',views.viewpAlunos,name="viewpAlunos"),
	path('nvAluno/',views.viewnvaluno,name="viewnvaluno"),
	path('alunos/',views.viewalunos, name="viewalunos"),
	path('chamada/',views.viewchamada, name="viewchamada"),

	path('defcadAluno/',views.defcadAluno, name="defcadAluno"),
	path('defdelaluno/<int:alucodigo>',views.defdelaluno,name="defdelaluno"),
	path('defeditaluno/<int:alucodigo>',views.defeditaluno,name="defeditaluno"),
	path('deffaltaluno/<int:alucodigo>',views.deffaltaluno,name="deffaltaluno"),
	# -------------------------------------------------------------------------------
	path('pProfessores/',views.viewpProfessores, name="viewpProfessores"),
	path('nvProfessor/',views.viewnvProfessor, name="viewnvProfessor"),

	path('defcadProfessor/',views.defcadProfessor, name="defcadProfessor"),
	path('professores/',views.viewprofessores, name="viewprofessores"),
	path('defdelprofessor/<int:procodigo>',views.defdelprofessor,name="defdelprofessor"),
	path('defeditprofessor/<int:procodigo>',views.defeditprofessor,name="defeditprofessor"),
	# -------------------------------------------------------------------------------
	path('pTurmas/',views.viewpTurmas, name="viewpTurmas"),
	path('nvTurma/',views.viewnvTurma, name="viewnvTurma"),
	path('viewverTurma/<int:turcodigo>',views.viewverTurma, name="viewverTurma"),

	path('defcadturma/',views.defcadturma, name="defcadturma"),
	path('defdelturma/<int:turcodigo>',views.defdelturma, name="defdelturma"),
	path('defcadalunoadt/<int:mandaID>',views.defcadalunoadt,name="defcadalunoadt"),
	# -------------------------------------------------------------------------------
	path('materias/',views.viewmaterias, name="viewmaterias"),

	path('defnvmateria/',views.defnvmateria, name="defnvmateria"),
	path('defeditmateria/<int:matcodigo>',views.defeditmateria,name="defeditmateria"),
	path('defdeltmateria/<int:matcodigo>',views.defdeltmateria,name="defdeltmateria"),
]

