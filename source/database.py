from constants import *


def createDatabase(absolute_output_path):

    database = open(absolute_output_path + '/config/Database.php', 'w')

    database.write('<?php' + EOL)
    database.write(EOL)
    database.write('class Database{' + EOL)
    database.write(EOL)
    database.write(ST + '//Database attributes' + EOL)
    database.write(ST + 'private $host = \'localhost\';' + EOL)
    database.write(ST + 'private $db_name = \'test\';' + EOL)
    database.write(ST + 'private $username = \'test\';' + EOL)
    database.write(ST + 'private $password = \'test\';' + EOL)
    database.write(ST + 'private $conn;' + EOL)
    database.write(EOL)
    database.write(ST + '//Database connection' + EOL)
    database.write(ST + 'public function connect(){' + EOL)
    database.write(EOL)
    database.write(DT + '$this->conn = null;' + EOL)
    database.write(EOL)
    database.write(DT + 'try{' + EOL)
    database.write(TT + '$this->conn = new PDO(\'mysql:host=\' . $this->host . \'dbname=\' . $this->db_name, '
                        '$this->username, $this->password);' + EOL)
    database.write(TT + '$this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);' + EOL)
    database.write(DT + '} catch (PDOException $e){' + EOL)
    database.write(TT + 'die(\'Connection Error: \' . $e->getMessage());' + EOL)
    database.write(DT + '}' + EOL)
    database.write(EOL)
    database.write(DT + 'return $this->conn;' + EOL)
    database.write(EOL)
    database.write(ST + '}' + EOL)
    database.write('}' + EOL)

    database.close()
