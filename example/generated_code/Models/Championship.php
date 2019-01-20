<?php

class Championship_Model{

	//Database
	private $conn;
	private $table = 'CHAMPIONSHIP';

	//Championship attributes
	private $champeionshipID;
	private $name;
	private $startDate;
	private $endDate;
	private $level;

	//Constructor
	function __construct($champeionshipID,$name,$startDate,$endDate,$level){
		$this->champeionshipID = $champeionshipID;
		$this->name = $name;
		$this->startDate = $startDate;
		$this->endDate = $endDate;
		$this->level = $level;
		include_once __DIR__.'/../config/Database.php';
		$this->conn = new Database()->connect();
	}

	//Getters
	function getChampeionshipid(){return $this->champeionshipID;}
	function getName(){return $this->name;}
	function getStartdate(){return $this->startDate;}
	function getEnddate(){return $this->endDate;}
	function getLevel(){return $this->level;}

	//Setters
	function setChampeionshipid($champeionshipID){$this->champeionshipID = $champeionshipID;}
	function setName($name){$this->name = $name;}
	function setStartdate($startDate){$this->startDate = $startDate;}
	function setEnddate($endDate){$this->endDate = $endDate;}
	function setLevel($level){$this->level = $level;}

	function readAll(){

		$query = 'SELECT * FROM ' . $this->table;

		$stmt = $this->conn->prepare($query);

		$stmt->execute();

		return $stmt;

	}

	function read(){

		$query = 'SELECT * FROM ' . $this->table . ' WHERE champeionshipID = ? ';

		$stmt = $this->conn->prepare($query);

		$stmt->bindParam(1, htmlspecialchars(strip_tags($this->champeionshipID)));

		$stmt->execute();

		return $stmt;

	}


	function insert(){

		$query = 'INSERT INTO ' . $this->table . '(champeionshipID, name, startDate, endDate, level)
		 VALUES (?, ?, ?, ?, ?)';

		$stmt = $this->conn->prepare($query);

		$stmt->bindParam(1, htmlspecialchars(strip_tags($this->champeionshipID)));
		$stmt->bindParam(2, htmlspecialchars(strip_tags($this->name)));
		$stmt->bindParam(3, htmlspecialchars(strip_tags($this->startDate)));
		$stmt->bindParam(4, htmlspecialchars(strip_tags($this->endDate)));
		$stmt->bindParam(5, htmlspecialchars(strip_tags($this->level)));

		$stmt->execute();

		return $stmt;

	}


	function update(){

		$query = 'UPDATE ' . $this->table . ' SET name = ? , startDate = ? , endDate = ? , level = ?  WHERE champeionshipID = ? ';

		$stmt = $this->conn->prepare($query);

		$stmt->bindParam(1, htmlspecialchars(strip_tags($this->name)));
		$stmt->bindParam(2, htmlspecialchars(strip_tags($this->startDate)));
		$stmt->bindParam(3, htmlspecialchars(strip_tags($this->endDate)));
		$stmt->bindParam(4, htmlspecialchars(strip_tags($this->level)));
		$stmt->bindParam(5, htmlspecialchars(strip_tags($this->champeionshipID)));

		$stmt->execute();

		return $stmt->rowCount() > 0;

	}


	function delete(){

		$query = 'DELETE FROM ' . $this->table . ' WHERE champeionshipID = ? ';

		$stmt = $this->conn->prepare($query);

		$stmt->bindParam(1, htmlspecialchars(strip_tags($this->champeionshipID)));

		$stmt->execute();

		return $stmt;

	}


}

