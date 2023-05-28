# HiperLibertad Crawel
Primero realice un analisis de la pagina, para identificar las tecnologias
utilizadas y llegue a la conclución de que era una pagina hecha en React y Redux
por lo tanto deberia de consumir alguna ApiRest.

La cual es provista por https://vtex.com/ar-es/ y comence a leer la documentación
de la misma para poder consumirla.

Dado a que tengo la información nesesaria procedo Crear el codigo. 
Tendre que crear una achivo
json con las sucursales copiando la respueta de el action INIT, ya que no consigo encortrar el endPoind de las misma.

## Endpoinds
### Catogorias 
Devuelve el arbol de categorias y sub cateogrias  limitando a 50 subniveles
```
/api/catalog_system/pub/category/tree/50
```
Mapeo de valores de categorias
Se va agregando una una "c" al map por niviel de categoria que se desea mapear
Categoria Generarl
```
/api/catalog_system/pub/facets/search/tecnologia/?map=c
```
Subcategoria
```
/api/catalog_system/pub/facets/search/tecnologia/tv-y-video/?map=c,c
```