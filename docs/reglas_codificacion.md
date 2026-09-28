# Cinco reglas de codificación del equipo

Estándar acordado para que el código sea legible, verificable y fácil de mantener. Cada regla se apoya en el atributo de mantenibilidad de ISO/IEC 25010.

1. **Nombres claros y descriptivos en español.** Las funciones y variables dicen lo que hacen (por ejemplo, `calcular_copago`, `valor_consulta`). Se evitan abreviaturas ambiguas como `x` o `tmp`.

2. **Funciones cortas con una sola responsabilidad.** Una función hace una cosa. Si supera unas 20 líneas o mezcla tareas, se divide. Esto mejora la capacidad de ser probado.

3. **Sin números mágicos.** Los valores con significado de negocio (por ejemplo, el 10 % del contributivo) viven en constantes con nombre, como el diccionario `PORCENTAJES`, y no repartidos por el código.

4. **Toda función pública lleva docstring y validación de entradas.** El docstring describe la especificación y los errores posibles. Las entradas inválidas lanzan excepciones claras (por ejemplo, `ValueError`) en lugar de devolver resultados incorrectos.

5. **Ningún cambio entra a main sin pruebas y revisión.** Cada cambio incluye pruebas unitarias, pasa el CI con cobertura mínima del 80 % y recibe la aprobación de al menos un compañero mediante pull request.

## Verificación
Las reglas 4 y 5 se comprueban automáticamente con pytest y el workflow de GitHub Actions. Las reglas 1 a 3 se revisan en cada pull request.
