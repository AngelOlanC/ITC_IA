# Arbol de búsqueda binaria

Implementación en python de un árbol de búsqueda binaria (BST por sus siglas en inglés).

Cómo característica principal, se cuenta con que cada nodo que conforme el árbol puede tener de 0 a 2 hijos, donde siempre los nodos con valores menores se encontrarán a su izquierda y los de valores mayores a su derecha.

A pesar de que los nodos se encuentren ordenados, todos sus métodos tienen complejidad O(n).
La prueba es que los nodos se insertan, pero el árbol no cuenta con balanceo, por lo tanto, se puede contar con árboles que tengan mucho peso hacia un mismo lado. Esto causaría que al momento de buscar o insertar, se cuente con la complejidad de O(n).

En esta implementación se cuenta con dos clases:
- Node.
- BST.

## Node
Esta clase cuenta con tres atributos:
- data: Almacena algún valor en el nodo.
- left: Representa al hijo izquierdo del nodo actual.
- right: Representa al hijo derecho del nodo actual.

Si left o right son None, significa que no hay hijo hacia ese lado. Se inicializan ambos de esta forma.

Solamente se cuenta con un único constructor que recibe el dato a almacenar.

## Tree
Esta clase representa al árbol de búsqueda binaria, el cuál está conformado por nodos de la clase "Node".

Como único atributo de la clase, se cuenta con:
- root: Representa la raíz del árbol.

La clase cuenta con dos constructores:
- Constructor vacío: Crea un árbol vacío.
- Constructor recibiendo raíz: Crea un árbol tomando como raíz un nodo específico.

La clase cuenta con los siguiente métodos:
- find: Método para buscar en el árbol el nodo que contenga el dato deseado, retornando este nodo o None en caso de que no exista. Funciona recursivamente, primeramente verificando si el nodo actual es el deseado, en otro caso, se llama recursivamente al método find con el nodo izquierdo o derecho, según el dato buscado.
- insert: Método para insertar un nodo con el dato deseado al árbol. Funciona recursivamente buscando donde insertar el nuevo nodo, realiza una búsqueda aprovechando el ordenamiento y cuando localiza el lugar donde va, lo inserta ahí.
- preorder: Método recursivo de impresión que funciona en el orden nodo actual, hijo izquierdo, hijo derecho.
- inorder: Método recursivo de impresión que funciona en el orden hijo izquierdo, nodo actual, hijo derecho.
- postorder: Método recursivo de impresión que funciona en el orden hijo izquierdo, hijo derecho, nodo actual.