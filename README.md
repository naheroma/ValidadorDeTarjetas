<h1>Algoritmo de Luhn</h1>
    <p>Este programa implementa el algoritmo de Luhn, también conocido como el algoritmo de verificación de número de tarjeta de crédito. El algoritmo de Luhn se utiliza para validar números de tarjetas de crédito y débito.</p>

   <h2>Descripción del código</h2>
    <p>El código se divide en los siguientes pasos:</p>

<ol>
    <ul>
    <li>Invierte el número de la tarjeta para empezar a procesarlo desde la posición más a la derecha.</li> 
    <li>Itera sobre los dígitos de la tarjeta invertida.</li>
    <li>Si el índice del dígito es impar, se multiplica por 2.</li>
    <li>Si el resultado de la multiplicación es mayor a 9, se resta 9 al resultado.</li>
    <li>Suma los dígitos (o los dígitos modificados) al valor a validar.</li>
    <li>Si el valor a validar es divisible por 10 sin dejar residuo, la tarjeta se considera válida.</li>
</ol>

   <p>El algoritmo de Luhn es un método sencillo para validar números de tarjeta de crédito o débito. Se basa en la suma de los dígitos y verifica si el resultado es divisible por 10. Si lo es, se considera que el número de tarjeta es válido.</p>


