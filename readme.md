# HiperLibertad Crawel
Es un pequeño programa que permite obtener csv con los productos de todas las sucursales, con soporte para proxy y configuarción de reintentos.

Primero realice un analisis de la pagina, para identificar las tecnologias
utilizadas y llegue a la conclución de que era una pagina hecha en React
por lo tanto deberia de consumir alguna ApiRest.

La cual es provista por https://vtex.com/ar-es/ y comence a leer la documentación
de la misma para poder consumirla.

Dado a que tengo la información nesesaria procedo Crear el codigo. 
Tendre que crear una achivo json con las sucursales copiando la respueta de el action INIT, ya que no consigo encortrar el endPoind de las misma, con los datos de configuracion de peticiones, ya que solo cuenta con información de la misma como dirección, horarios, etc que no son de utilidad para este programa

Luego de investigar y descubrir que algunas rutas estaban en privado construi mi propio mapa del sitio en categoria_completa.json 
para que pueda servir en un futuro, para poder aplicar filtros por marcas y categoria y subcateogria

Dado que se me pedia que no use seleinium, deduje que tampoco ROBOCORP asi que lo realice con el
minimo de librerias posibles
## Librerias

1- tqdm -> Para realizar los progresBar

2- requests -> Para realizar peticones a la api
````bash
  pip install tqdm
  pip install requests
````

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
Busqueda de producto
```
/api/catalog_system/pub/products/search/?fq=paramtro
```
Parametros

    - Marca -> brandId:2000012
    - Sku -> skuId:10346
    - Producto -> productId:455983

Busqueda por Categoria
```
/api/catalog_system/pub/products/search/tecnologia/tv-y-video?O=filtro&limite&sc=sucursal_id
```
Filtro
    Ordenar:

	-OrderByPrice menor precio
	-OrderByTopSaleDESC mas vedido
	-OrderByReviewRateDESC mas valorrado
	-OrderByNameASC ordenar de A a Z
	-OrderByNameDESC odenar de Z a A
	-OrderByReleaseDateDESC fecha de lanzamiento
	-OrderByBestDiscountDESC mejor descuento

Limitar Resultados

Se define los limtes de siendo 0 el inicio y 49 el maximo da un total de 50 productos

	-_from=inicio&_to=fin
