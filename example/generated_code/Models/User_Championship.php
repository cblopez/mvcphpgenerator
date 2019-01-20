<?php

class User_Championship_Model{

	//Database
	private $conn;
	private $table = 'USER_CHAMPIONSHIP';

	//User_Championship attributes
	private $championshipID;
	private $login;
	private $inscriptionDate;

	//Constructor
	function __construct($championshipID,$login,$inscriptionDate){
		$this->championshipID = $championshipID;
		$this->login = $login;
		$this->inscriptionDate = $inscriptionDate;
		include_once __DIR__.'/../config/Database.php';
		$this->conn = new Database()->connect();
	}

	//Getters
	function getChampionshipid(){return $this->championshipID;}
	function getLogin(){return $this->login;}
	function getInscriptiondate(){return $this->inscriptionDate;}

	//Setters
	function setChampionshipid($championshipID){$this->championshipID = $championshipID;}
	function setLogin($login){$this->login = $login;}
	function setInscriptiondate($inscriptionDate){$this->inscriptionDate = $inscriptionDate;}

	function readAll(){

		$query = 'SELECT * FROM ' . $this->table;

		$stmt = $this->conn->prepare($query);

		$stmt->execute();

		return $stmt;

	}

	function read(){

		$query = 'SELECT * FROM ' . $this->table . ' WHERE championshipID = ? AND login = ? ';

		$stmt = $this->conn->prepare($query);

		$stmt->bindParam(1, htmlspecialchars(strip_tags($this->championshipID)));
		$stmt->bindParam(2, htmlspecialchars(strip_tags($this->login)));

		$stmt->execute();

		return $stmt;

	}


	function insert(){

		$query = 'INSERT INTO ' . $this->table . '(championshipID, login, inscriptionDate)
		 VALUES (?, ?, ?)';

		$stmt = $this->conn->prepare($query);

		$stmt->bindParam(1, htmlspecialchars(strip_tags($this->championshipID)));
		$stmt->bindParam(2, htmlspecialchars(strip_tags($this->login)));
		$stmt->bindParam(3, htmlspecialchars(strip_tags($this->inscriptionDate)));

		$stmt->execute();

		return $stmt;

	}


	function update(){

		$query = 'UPDATE ' . $this->table . ' SET inscriptionDate = ?  WHERE championshipID = ? AND login = ? ';

		$stmt = $this->conn->prepare($query);

		$stmt->bindParam(1, htmlspecialchars(strip_tags($this->inscriptionDate)));
		$stmt->bindParam(2, htmlspecialchars(strip_tags($this->championshipID)));
		$stmt->bindParam(3, htmlspecialchars(strip_tags($this->login)));

		$stmt->execute();

		return $stmt->rowCount() > 0;

	}


	function delete(){

		$query = 'DELETE FROM ' . $this->table . ' WHERE championshipID = ? AND login = ? ';

		$stmt = $this->conn->prepare($query);

		$stmt->bindParam(1, htmlspecialchars(strip_tags($this->championshipID)));
		$stmt->bindParam(2, htmlspecialchars(strip_tags($this->login)));

		$stmt->execute();

		return $stmt;

	}


}

