
    <h1>Algoritmo de Luhn</h1>
    <p>Este programa implementa el algoritmo de Luhn, también conocido como el algoritmo de verificación de número de tarjeta de crédito. El algoritmo de Luhn se utiliza para validar números de tarjetas de crédito y débito.</p>

    <h2>Descripción del código</h2>
    <p>El código se divide en los siguientes pasos:</p>

    <ol>
        <li>Se define una cadena de dígitos de tarjeta de crédito como "tarjeta".</li>
        <li>Se crea una cadena vacía llamada "tarjetaInvertida" para almacenar la tarjeta invertida.</li>
        <li>Se invierte la cadena "tarjeta" para obtener la tarjeta invertida utilizando un bucle for.</li>
        <li>Se inicializan las variables "par", "InvertidoMultiplicado" y "valorAValidar".</li>
        <li>Se itera a través de la tarjeta invertida de dos en dos elementos utilizando el bucle for.</li>
        <li>En cada iteración, se obtienen dos dígitos consecutivos y se almacenan en la variable "par".</li>
        <li>Se intenta multiplicar por 2 el segundo dígito de "par" utilizando un bloque try-except.</li>
            <ul>
                <li>Si no se produce un IndexError, se multiplica el segundo dígito por 2 y se almacena en la variable "numeroMultiplicado".</li>
                <li>Si se produce un IndexError, se asigna 0 a "numeroMultiplicado".</li>
            </ul>
        <li>Si "numeroMultiplicado" es mayor que 9, se descompone en dígitos individuales y se suman utilizando una comprensión de lista.</li>
        <li>Se construye una cadena llamada "InvertidoMultiplicado" concatenando el primer dígito de "par" y "numeroMultiplicado".</li>
        <li>Se itera a través de cada dígito en "InvertidoMultiplicado" y se suma a "valorAValidar".</li>
        <li>Se verifica si el resto de dividir "valorAValidar" por 10 es igual a 0.</li>
            <ul>
                <li>Si es igual a 0, se imprime "Valida" para indicar que la tarjeta es válida.</li>
                <li>Si no es igual a 0, se imprime "No valida" para indicar que la tarjeta no es válida.</li>
            </ul>
    </ol>

    <p>El algoritmo de Luhn es un método sencillo para validar números de tarjeta de crédito o débito. Se basa en la suma de los dígitos y verifica si el resultado es divisible por 10. Si lo es, se considera que el número de tarjeta es válido.</p>


