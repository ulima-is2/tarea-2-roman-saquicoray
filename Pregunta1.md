### Single Responsibility

No se cumple el principio Single Responsability, ya que se puede ver con claridad quen en las clases CinePlaneta y CineStark tienen muchas
funcionalidades, cuando el principio se basa en la cohesión y promueve la modularización, para pode cumplir con dicho principio convendría conglomerar las funcionalidades con sus respectivas clases en vez de hacer codigo redundante. 

### Open Close 

Al no existir una clase padre para los cines, se estaría evidenciando, la no existencia del principio open close, con la creación de la clase padre y mediante la abstrabcion se podrian heredar metodos y propiedades a los cines hijos.

### Liskov Sustitution  

El principio no se cumple ya que el cliente tiene que interactuar por cada cine por separado, a pudiendo en el caso ideal comunicarse con la clase cine previa abstracción.

