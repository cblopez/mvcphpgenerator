<?php

class User_Model{

	//Database
	private $conn;
	private $table = 'USER';

	//User attributes
	private $login;
	private $name;
	private $surname;
	private $email;
	private $password;

	//Constructor
	function __construct($login,$name,$surname,$email,$password){
		$this->login = $login;
		$this->name = $name;
		$this->surname = $surname;
		$this->email = $email;
		$this->password = $password;
		include_once __DIR__.'/../config/Database.php';
		$this->conn = new Database()->connect();
	}

	//Getters
	function getLogin(){return $this->login;}
	function getName(){return $this->name;}
	function getSurname(){return $this->surname;}
	function getEmail(){return $this->email;}
	function getPassword(){return $this->password;}

	//Setters
	function setLogin($login){$this->login = $login;}
	function setName($name){$this->name = $name;}
	function setSurname($surname){$this->surname = $surname;}
	function setEmail($email){$this->email = $email;}
	function setPassword($password){$this->password = $password;}

	function readAll(){

		$query = 'SELECT * FROM ' . $this->table;

		$stmt = $this->conn->prepare($query);

		$stmt->execute();

		return $stmt;

	}

	function read(){

		$query = 'SELECT * FROM ' . $this->table . ' WHERE login = ? ';

		$stmt = $this->conn->prepare($query);

		$stmt->bindParam(1, htmlspecialchars(strip_tags($this->login)));

		$stmt->execute();

		return $stmt;

	}


	function insert(){

		$query = 'INSERT INTO ' . $this->table . '(login, name, surname, email, password)
		 VALUES (?, ?, ?, ?, ?)';

		$stmt = $this->conn->prepare($query);

		$stmt->bindParam(1, htmlspecialchars(strip_tags($this->login)));
		$stmt->bindParam(2, htmlspecialchars(strip_tags($this->name)));
		$stmt->bindParam(3, htmlspecialchars(strip_tags($this->surname)));
		$stmt->bindParam(4, htmlspecialchars(strip_tags($this->email)));
		$stmt->bindParam(5, htmlspecialchars(strip_tags($this->password)));

		$stmt->execute();

		return $stmt;

	}


	function update(){

		$query = 'UPDATE ' . $this->table . ' SET name = ? , surname = ? , email = ? , password = ?  WHERE login = ? ';

		$stmt = $this->conn->prepare($query);

		$stmt->bindParam(1, htmlspecialchars(strip_tags($this->name)));
		$stmt->bindParam(2, htmlspecialchars(strip_tags($this->surname)));
		$stmt->bindParam(3, htmlspecialchars(strip_tags($this->email)));
		$stmt->bindParam(4, htmlspecialchars(strip_tags($this->password)));
		$stmt->bindParam(5, htmlspecialchars(strip_tags($this->login)));

		$stmt->execute();

		return $stmt->rowCount() > 0;

	}


	function delete(){

		$query = 'DELETE FROM ' . $this->table . ' WHERE login = ? ';

		$stmt = $this->conn->prepare($query);

		$stmt->bindParam(1, htmlspecialchars(strip_tags($this->login)));

		$stmt->execute();

		return $stmt;

	}


}

