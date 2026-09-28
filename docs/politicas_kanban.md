# Tablero Kanban: políticas por columna

Enlace o captura del tablero: PEGAR_AQUI_EL_ENLACE_O_LA_CAPTURA

## Columnas, límites WIP y políticas

| Columna | Límite WIP | Política de entrada | Política de salida |
|---|---|---|---|
| Por hacer | Sin límite | Historia con descripción y criterios de aceptación claros | Priorizada por el Product Owner |
| En desarrollo | 3 | Una persona la asume y escribe primero las pruebas (TDD) | Pruebas unitarias pasando en local |
| En revisión / pruebas | 2 | Pull request abierto y enlazado a la tarjeta | Revisión aprobada y CI en verde |
| Listo para desplegar | 2 | Cumple la Definition of Done completa | Se despliega en día hábil de martes a jueves, nunca en viernes |
| Hecho | Sin límite | Desplegada en producción y verificada | Se archiva al cierre del sprint |

## Justificación de los límites WIP
- **En desarrollo (3):** con un equipo de 3 a 4 personas, limitar el trabajo en curso evita que cada quien abra varias tareas a medias y reduce el tiempo de ciclo.
- **En revisión / pruebas (2):** mantiene la revisión como prioridad y evita acumulaciones que retrasan las entregas.
- **Listo para desplegar (2):** obliga a desplegar con frecuencia en lotes pequeños, lo que reduce el riesgo de cada despliegue.

## Políticas transversales
1. Si una columna llega a su límite WIP, nadie empieza trabajo nuevo: primero se ayuda a terminar lo que está en curso.
2. Los defectos que llegan a producción se atienden con prioridad y suben al inicio de "En desarrollo".
3. Se revisa el tablero en una reunión diaria corta y se mide el lead time de cada tarjeta.
4. Regla de despliegue: no se despliega los viernes ni en vísperas de festivo.
