# Bloque 1: problemas del caso y atributos ISO/IEC 25010:2023

## Contexto
La startup entrega una app de citas médicas cada 2 semanas. Tiene defectos que llegan a producción, pruebas solo manuales y despliegues los viernes. El modelo de calidad del producto ISO/IEC 25010:2023 define nueve atributos: adecuación funcional, eficiencia de desempeño, compatibilidad, capacidad de interacción, fiabilidad, seguridad, mantenibilidad, flexibilidad y seguridad operacional (safety). A continuación se asocia cada problema con el atributo más afectado.

## Tabla problema → atributo

| Problema del caso | Atributo afectado | Subcaracterística | Métrica propuesta |
|---|---|---|---|
| Defectos que llegan a producción | Adecuación funcional | Corrección funcional | Defectos escapados por release |
| Pruebas solo manuales | Mantenibilidad | Capacidad de ser probado | Porcentaje de cobertura de pruebas automatizadas |
| Despliegues los viernes sin control | Fiabilidad | Madurez y recuperabilidad | Tasa de fallo de cambios y tiempo medio de recuperación |
| Manejo de datos de pacientes sin controles verificables | Seguridad | Confidencialidad | Número de vulnerabilidades críticas abiertas |

## Justificación de cada asociación

1. **Defectos que llegan a producción → Adecuación funcional.** Si un error en el cálculo de un copago o en la asignación de una cita llega al usuario, el sistema no hace lo que debe hacer. Es un problema de corrección funcional, porque el resultado entregado no coincide con la especificación.

2. **Pruebas solo manuales → Mantenibilidad.** Sin pruebas automatizadas, cada cambio exige repetir revisiones a mano, es lento y deja pasar errores. La subcaracterística afectada es la capacidad de ser probado: el código no puede verificarse de forma rápida y repetible.

3. **Despliegues los viernes sin control → Fiabilidad.** Desplegar al cierre de la semana deja poco tiempo y poco personal para reaccionar si algo falla. Afecta la madurez (frecuencia de fallos) y la recuperabilidad (tiempo en restablecer el servicio). Los datos simulados lo confirman: los 3 despliegues realizados en viernes fallaron.

4. **Datos de pacientes → Seguridad.** Una app médica maneja información sensible. Sin controles verificables (revisión de dependencias, análisis de vulnerabilidades), no se puede demostrar confidencialidad ni integridad.

## Prioridad sugerida
1. Fiabilidad (impacto directo en pacientes y en la operación).
2. Adecuación funcional.
3. Mantenibilidad.
4. Seguridad.
