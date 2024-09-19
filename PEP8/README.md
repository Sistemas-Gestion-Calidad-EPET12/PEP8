# Actividad 4: Mejora de Código en Python según PEP8 y PEP257

## Descripción de la Actividad

En esta actividad, deberán trabajar en grupos para identificar y corregir errores de estilo en un código Python proporcionado. El código funciona correctamente, pero no sigue las buenas prácticas de codificación recomendadas por PEP8 y PEP257, los estándares de estilo y documentación de Python. El objetivo es mejorar la calidad del código siguiendo estas recomendaciones, lo que hará que el código sea más legible, mantenible y profesional.

## Objetivos de Aprendizaje

1. **Comprender las reglas de PEP8**: Aprenderán a aplicar las convenciones de estilo más importantes para escribir código Python de manera consistente.
2. **Comprender las reglas de PEP257**: Aprenderán a documentar correctamente el código utilizando docstrings según el estándar PEP257.
3. **Mejorar la legibilidad y mantenibilidad del código**: Reconocerán cómo la adherencia a un estándar de codificación y documentación puede mejorar la calidad del software.
4. **Practicar la revisión de código**: Desarrollarán habilidades para identificar y corregir errores de estilo y documentación en código existente.

## Tipos de Errores a Corregir

Durante la actividad, deberán buscar y corregir los siguientes tipos de errores:

1. **Nombres de Variables y Funciones:**
   - **Nombres descriptivos:** Asegúrate de que los nombres de las variables y funciones describan claramente su propósito.
   - **Convención de nombres:** Utiliza `snake_case` para los nombres de las variables y funciones.

2. **Espaciado y Sangrías:**
   - **Indentación:** Utiliza 4 espacios para cada nivel de sangría.
   - **Espaciado alrededor de operadores:** Asegúrate de que haya espacios alrededor de los operadores (`=`, `+`, `-`, etc.).

3. **Líneas en Blanco:**
   - **Separación de funciones y clases:** Utiliza líneas en blanco para separar funciones, clases y bloques de código dentro de una función.

4. **Longitud de Línea:**
   - **Máximo de 79 caracteres:** Las líneas de código no deben exceder los 79 caracteres para mejorar la legibilidad.

5. **Documentación según PEP257:**
   - **Docstrings:** 
     - **Descripción concisa:** Cada función, clase o módulo debe tener un docstring que describa brevemente su propósito.
     - **Estilo de docstring:** Utiliza triple comillas dobles `"""` para docstrings.
     - **Resumen en una sola línea:** Si la docstring es corta, debería consistir en una única línea con una breve descripción.
     - **Docstrings de varias líneas:** Si la docstring necesita más detalles, la primera línea debe ser un resumen corto seguido de una línea en blanco y luego una explicación más detallada.
     - **Documentación de clases y métodos:** Las clases deben tener un docstring al inicio que describa la clase y sus métodos principales. Los métodos deben tener docstrings que describan su funcionalidad, los argumentos que aceptan y lo que retornan.

## Descripción del Código

El código proporcionado realiza varias operaciones comunes, tales como:

- **Generación de Números Aleatorios:** Crea una lista de números aleatorios dentro de un rango especificado.
- **Ordenamiento:** Implementa un algoritmo de ordenamiento (bubble sort) para organizar los números.
- **Cálculo de Estadísticas:** Encuentra el valor mínimo, máximo, el promedio, y cuenta las ocurrencias de un número específico dentro de la lista.
- **Verificación de Palíndromos:** Comprueba si una palabra es un palíndromo (se lee igual al derecho y al revés).
- **Generación de Secuencias de Fibonacci:** Genera y muestra una secuencia de números de Fibonacci.
- **Cálculo de Factorial:** Calcula el factorial de un número dado.
- **Detección de Números Primos:** Encuentra todos los números primos hasta un valor dado.

Cada uno de estos componentes está estructurado en funciones individuales, y el código final se ejecuta a través de una función `main()` que llama a todas estas operaciones.
