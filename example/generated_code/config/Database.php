<?php

class Database{

	//Database attributes
	private $host = 'localhost';
	private $db_name = 'test';
	private $username = 'test';
	private $password = 'test';
	private $conn;

	//Database connection
	public function connect(){

		$this->conn = null;

		try{
			$this->conn = new PDO('mysql:host=' . $this->host . 'dbname=' . $this->db_name, $this->username, $this->password);
			$this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		} catch (PDOException $e){
			die('Connection Error: ' . $e->getMessage());
		}

		return $this->conn;

	}
}
