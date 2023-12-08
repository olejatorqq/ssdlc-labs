1. Необходимо найти участок кода, содержащий инъекцию SQL кода в задании Blind Sql Injection на сайте dvwa.local с использованием статического анализатора кода (Можно использовать официальный ресурс или виртуальную машину Web Security Dojo)
2. Проанализировать код и сделать кодревью, указав слабые места

```php
<?php

if( isset( $_GET[ 'Submit' ] ) ) {
	// Get input
	$id = $_GET[ 'id' ];

	// Check database
	$getid  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
	$result = mysqli_query($GLOBALS["___mysqli_ston"],  $getid ); // Removed 'or die' to suppress mysql errors

	// Get results
	$num = @mysqli_num_rows( $result ); // The '@' character suppresses errors
	if( $num > 0 ) {
		// Feedback for end user
		$html .= '<pre>User ID exists in the database.</pre>';
	}
	else {
		// User wasn't found, so the page wasn't!
		header( $_SERVER[ 'SERVER_PROTOCOL' ] . ' 404 Not Found' );

		// Feedback for end user
		$html .= '<pre>User ID is MISSING from the database.</pre>';
	}

	((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

?>
```

3. Разработать свою систему вывода информации об объекте на любом языке, исключающий взможность инъекции SQL кода. Возможно исправление участка кода из dvwa.local
    
    Требования к системе авторизации
    3.1 Система вывода информации об объекте должна использовать запросы GET с параметрами, аналогичными из задания Blind SQL injection dvwa