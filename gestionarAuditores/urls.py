from django.urls import path, include

from gestionarAuditores import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('auditores/', views.auditores, name="auditores"),
    path('registrar/', views.registrarAuditor, name="registrarAuditor"),
    path('listar/', views.listarAuditores, name="listarAuditores"),
    path('eliminar/', views.eliminarAuditor, name="eliminarAuditor"),
]
