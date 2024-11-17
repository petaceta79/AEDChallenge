## Proyecto: Datathon FME

### Descripción:
Este proyecto corresponde a la participación en la Datathon FME. En este repositorio encontrarás los archivos y recursos relacionados con nuestro análisis, procesamiento y visualización de datos.

### Archivos principales:
- **Codigo_final.py**: 
  Este es el archivo principal que contiene el algoritmo, el cual clasifica en grupos a las personas más similares.
El algoritmo divide en subconjuntos disjuntos las características más importantes, para luego dividir en grupos de 4 todas las intersecciones de estas, así obteniendo a los usuarios más parecidos.
Una vez agrupados estos, se vuelve a aplicar el algoritmo, pero obviando la característica que consideramos menos importante, para así eliminar una restricción y crear nuevos grupos parecidos lo máximo posible. Esto se repite hasta que no quede gente sin grupo o sean totalmente diferentes, donde se juntarán los restantes.
