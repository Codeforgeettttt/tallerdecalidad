# Bloque 5: métricas

## Métricas DORA (datos en `datos/despliegues.csv`, periodo de 28 días)

- **Frecuencia de despliegue:** 20 despliegues en 28 días, aproximadamente 5 por semana (0,71 por día).
- **Lead time de cambios (mediana, en horas):** 20 horas. El promedio es de 24,7 horas, más alto por algunos cambios que tardaron dos días o más en llegar a producción.
- **Tasa de fallo de cambios:** 20 % (4 de 20 despliegues fallaron).
- **Tiempo medio de recuperación (horas):** 4,5 horas (recuperaciones de 5, 3, 2 y 8 horas).

### Cómo se calculó
- Frecuencia: número de filas del CSV dividido entre las 4 semanas del periodo.
- Lead time: diferencia entre `fecha_despliegue` y `fecha_commit` de cada despliegue; se toma la mediana.
- Tasa de fallo: despliegues con `exitoso = no` dividido entre el total.
- Recuperación: promedio de `horas_recuperacion` en los despliegues fallidos.

### Interpretación
- La frecuencia es razonable, pero la tasa de fallo del 20 % es alta frente a las referencias de DORA para equipos de alto rendimiento, que suelen estar por debajo del 15 %.
- Hallazgo clave: los 3 despliegues realizados en viernes (4, 11 y 25 de septiembre) fallaron los tres, y de los 4 fallos totales, 3 ocurrieron en viernes. Esto respalda la política de no desplegar los viernes.
- Un lead time mediano de 20 horas es bueno, pero muestra dispersión: hay cambios que esperan dos días o más antes de llegar a producción.
- Recuperar en promedio 4,5 horas es aceptable, pero mejora con pruebas automatizadas, despliegues pequeños y rollback rápido.

## Cuatro métricas por enfoque

| Enfoque | Métrica | Qué mide | Atributo ISO 25010 que respalda |
|---|---|---|---|
| Scrum | Defectos escapados por sprint | Errores detectados en producción por cada sprint | Adecuación funcional |
| Scrum | Cumplimiento de la Definition of Done | Porcentaje de historias entregadas que cumplen los 6 criterios | Fiabilidad |
| Kanban | Lead time y tiempo de ciclo | Tiempo desde que una tarjeta entra hasta que se termina | Eficiencia de desempeño |
| Kanban | WIP promedio y violaciones de límite | Cuánto trabajo en curso hay frente al límite acordado | Eficiencia de desempeño |
| XP | Cobertura de pruebas unitarias | Porcentaje de código cubierto por pruebas automáticas | Mantenibilidad |
| XP | Proporción de pruebas que pasan en el primer intento | Estabilidad del código y disciplina TDD | Mantenibilidad |
| DevOps | Tasa de fallo de cambios | Porcentaje de despliegues que causan fallo | Fiabilidad |
| DevOps | Tiempo medio de recuperación | Horas necesarias para restablecer el servicio | Fiabilidad |

Como el taller pide una métrica principal por enfoque, la sugerida para cada uno es la primera fila de su grupo. Las segundas filas quedan como complemento.

## Plan de mejora derivado
1. Prohibir despliegues los viernes (política del tablero Kanban).
2. Exigir cobertura mínima del 80 % en CI antes de cualquier merge.
3. Desplegar en lotes pequeños para bajar la tasa de fallo y el tiempo de recuperación.
4. Revisar estas métricas cada sprint en la retrospectiva.
