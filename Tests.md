# Documentación de Pruebas - Calculadora en Python

## Descripción del Proyecto
Este proyecto implementa una calculadora básica en Python con operaciones aritméticas simples. Incluye pruebas unitarias, de integración y una propuesta de rendimiento.

## Pruebas Implementadas

### 1. Prueba Unitaria: Suma Correcta
- **Objetivo**: Verificar que el método `add` funcione correctamente para casos básicos.
- **Casos de Prueba**:
  - `add(2, 3)` debe devolver `5`.
  - `add(-1, 1)` debe devolver `0`.
  - `add(0, 0)` debe devolver `0`.
- **Herramienta**: Módulo `unittest` de Python.
- **Resultado Esperado**: Todas las aserciones pasan sin errores.

### 2. Caso de Prueba de Integración: Operaciones Encadenadas
- **Objetivo**: Verificar que el método `chained_operation` evalúe expresiones aritméticas encadenadas correctamente, integrando múltiples operaciones.
- **Casos de Prueba**:
  - `"2 + 3 * 4"` debe devolver `14` (prioridad de operadores: 2 + (3*4)).
  - `"10 - 2 / 2"` debe devolver `9` (10 - (2/2)).
  - Expresiones inválidas deben lanzar `ValueError`.
- **Herramienta**: Módulo `unittest` de Python.
- **Resultado Esperado**: Las expresiones válidas se evalúan correctamente; las inválidas generan errores.

### 3. Propuesta de Prueba de Rendimiento: Repetición de Cálculos
- **Objetivo**: Evaluar el rendimiento al repetir una operación simple (como una suma) miles de veces, para detectar posibles cuellos de botella en eficiencia.
- **Descripción**: Usa `timeit` para medir el tiempo de ejecución de `calc.add(1, 1)` repetido 10,000 veces.
- **Herramienta**: Módulo `timeit` de Python.
- **Resultado Esperado**: El tiempo debe ser razonable (ej. menos de 1 segundo en una máquina típica). Imprime el tiempo en consola. En producción, podrías automatizar comparaciones con umbrales o benchmarks.
- **Nota**: Esta es una propuesta; en un entorno real, podrías expandirla para probar operaciones más complejas o bajo carga.
