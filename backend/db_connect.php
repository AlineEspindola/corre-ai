<?php
$host = 'postgres'; 
$dbname = 'db_corre_ai'; 
$user = 'aline'; 
$password = 'correai01';

try {
    $dsn = "pgsql:host=$host;dbname=$dbname"; 
    $pdo = new PDO($dsn, $user, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); 
    echo "Conexão bem-sucedida ao banco de dados PostgreSQL!";

    $query = "SELECT id, name, email FROM \"user\""; 
    $stmt = $pdo->query($query); 
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        echo "ID: " . $row['id'] . " - Name: " . $row['name'] . " - Email: " . $row['email'] . "<br>";
    }

} catch (PDOException $e) {
    echo "Erro na conexão: " . $e->getMessage();
}
?>