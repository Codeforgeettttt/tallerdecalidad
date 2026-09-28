# Definition of Done (6 criterios)

La Definition of Done (DoD) es el acuerdo del equipo sobre cuándo un trabajo se considera terminado. Cada criterio es verificable con sí o no, está ligado a un atributo de calidad ISO/IEC 25010 y tiene una evidencia concreta.

| # | Criterio | Atributo ISO 25010 | Evidencia |
|---|---|---|---|
| 1 | El código fue revisado y aprobado por al menos un compañero | Mantenibilidad (analizabilidad) | Pull request con aprobación registrada |
| 2 | Las pruebas unitarias del cambio están escritas y pasan | Adecuación funcional (corrección) | Ejecución de pytest en verde |
| 3 | La cobertura de pruebas es mayor o igual al 80 % | Mantenibilidad (capacidad de ser probado) | Reporte de pytest-cov en el workflow de Actions |
| 4 | El workflow de CI termina en verde | Fiabilidad (madurez) | Check verde en la pestaña Actions |
| 5 | No hay vulnerabilidades críticas conocidas en el cambio ni en sus dependencias | Seguridad (confidencialidad) | Reporte de análisis de dependencias sin hallazgos críticos |
| 6 | El Product Owner validó los criterios de aceptación de la historia | Adecuación funcional (completitud) | Comentario de aprobación en la tarjeta del tablero |

## Reglas de uso
- Una historia solo pasa a la columna "Hecho" si cumple los 6 criterios. Si falta uno, no está terminada.
- La DoD se revisa en cada retrospectiva y puede ajustarse con acuerdo del equipo.
- Los despliegues solo se hacen desde código que cumple la DoD.
