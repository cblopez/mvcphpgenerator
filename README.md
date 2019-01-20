# mvcphpgenerator 3.0
Python script for PHP file generator using MVC Paradigm for Python 2.7.  
Created by Christian Barral  

## NEW!  
- Database class creation  
- Deleted manual input  
- CRUD Functionalities generation  
- SQL Injection and XSS protection  
- Primary keys support  
- Input file parser with errors display  

## Instructions
Download the script and execute it via terminal  
Avaliable for:  
- Windows
- MacOS
- Linux  
  
  
Move to a desired directory via terminal  
```
 cd directory_path  
```
Execute the script and display help  
```
 python mvcPHPGenerator.py --help  
```  

You'll be asked to select an input file with all the info required to create the PHP scripts and classes. The script follows the following scheme for your project:  
- Controllers are scripts
- Models are classes
- Views are not created (obviously)
- The script for gathering data (from $_GET and $_POST) is situated under MVCPHPGenerator/Functions (MVCPHPGenerator is the default name, you'll be able to change it, read 'Arguments' section).  
- The index.php file is used as a common entry point. 
  
## Arguments  
Several arguments are now available for you script:  
```  
usage: mvcPHPGenerator.py [-h] -i INPUT_FILE [-o OUTPUT_DIRECTORY]
                          [--name OUTPUT_NAME] [--create-index]

mvcPHPGenerator. PHP file generator.

optional arguments:
  -h, --help           show this help message and exit
  -i INPUT_FILE        Select entities, attributes and actions from a
                       structured file. Visit
                       http://www.github.com/cblopez/mvcPHPGenerator for more
                       details.
  -o OUTPUT_DIRECTORY  Select the output directory of the resulting folder.
                       Default: '.'
  --name OUTPUT_NAME   Select the name of the output directory you want to
                       create. Default: 'MVCPHPGenerator'
  --create-index       Enable de index.php creation.
``` 
## Input file  
As you can see in the possible arguments section, you must use an input file for the application to work, which has to follow some syntax rules:   
- Entities MUST start with a '-' sign  
- Attributes and actions from an entity MUST be under that entity and before the next one, if you don't want to experiment some weird behavour.  
- Attributes MUST start with '+' sign  
- Actions MUST start with '\*' sign  
- Primary keys must have a '!' sign at the end of the attribute. At least one attribute from every entity needs one.  
- Any type of tab (\t) or blank line (\n) will be omitted.  

### Example  
So we have the following example: "I want to create a PHP file structure with three entities involved: Championship, User and User_Championship. My User has the following attributes: login (primary key), name, surname, email, password. The application will be able to register, login, edit and showProfile for every user. The Championship entity has the following attributes: championshipID (primary key), name, startDate, endDate and level. The applications will be able to add, edit, delete, showall, showcurrent and promote any championship. The User_Championship entity is used to save every player that is participating in any championship (From a database perspective, a single User can participate in n Championships and m Users can be in a single Championship, so this entity represents the (n, m) cardinality), so it must have a championshipID attribute (primary key) and a login attribute (primary key), plus an inscriptionDate. Last but not least, the controller for this entity must allow to add, search and delete anything related to the User-Championship relationship". Here's an example of how the input file should look like:  
``` 
-User
	+login!
	+name
	+surname
	+email
	+password
	*register
	*login
	*edit
	*showProfile

-User_Championship
	+championshipID!
	+login!
	+inscriptionDate
	*add
	*search
	*delete

-Championship
	+champeionshipID!
	+name
	+startDate
	+endDate
	+level
	*add
	*edit
	*delete
	*showall
	*showcurrent
	*promote
```  
Now all we have to do, is to execute the script using the -i option. Imagine that the above file is called 'skeleton_example.txt' and it is located in the /tmp/example/ folder. We'll also like to name our output directory as 'gitExample', and save it in /tmp/example/. Let's also generate an index.php to make our lifes easier:  
``` 
python mvcPHPGenerator.py -i /tmp/example/skeleton_example.txt -o /tmp/example --name gitExample --create-index
```  

The resulting directory should look something like this (entities taken from the above example):  
- gitExample
  - config
    - Database.php
  - Controllers
    - Championship_Controller.php
    - User_Championship_Controller.php
    - User_Controller.php
  - Functions
    - gatherData.php
  - Models
    - Championship_Model.php
    - User_Championship_Model.php
    - User_Model.php
  - Views  
  - index.php  
  
## Error handling  
In case you have any syntax error with your input file, the script will tell you if:  
- The input file does not exist  
- Any syntax error was found, like a line not starting with '-', '+' or '\*'  
- There is a missing primary key for any entity  

Example:  
If the input file does not exist:  
```
[!] The given file does not exist, please select a valid one. Exiting...
```  
If you have a syntax error:  
```
[!] Syntax error on line: 3. Check if there is a syntax error. Exiting...
```  
If you have missed a primary key:  
```
[!] The entity User has no Primary Key, please select at least one attribute as PK writting an exclamation '!' sign at the end of it.
```  

### For a complete example, feel free to check the 'example' folder in the repository  


## Controller Example: User_Championship_Controller.php   
```
<?php

/**
  * Controller generated by MVCPHPGenerator
  * Created by cblopez at https://github.com/cblopez/mvcphpgenerator  *
  * By default, all actions are divided by the possible existance of $_POST array.
  */


include __DIR__.'/../Functions/gatherData.php';


switch($_GET['action']){

	case 'add':
	if(!$_POST){
		//Fill
	} else {
		//Fill
	}
	break;

	case 'search':
	if(!$_POST){
		//Fill
	} else {
		//Fill
	}
	break;

	case 'delete':
	if(!$_POST){
		//Fill
	} else {
		//Fill
	}
	break;

}


```
## Model example: User_Model.php
```
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

?>
```
## gatherData Example  
```
<?php

include __DIR__.'/../Models/User_Championship.php';
include __DIR__.'/../Models/Championship.php';
include __DIR__.'/../Models/User.php';

function gatherDataUser_Championship(){

	$championshipID = '';
	$login = '';
	$inscriptionDate = '';

	if($_POST){

		if(!empty($_POST['championshipID'])) $championshipID = $_POST['championshipID'];
		if(!empty($_POST['login'])) $login = $_POST['login'];
		if(!empty($_POST['inscriptionDate'])) $inscriptionDate = $_POST['inscriptionDate'];

		return new User_Championship_Model($championshipID!,$login!,$inscriptionDate);

	} else {

		if(!empty($_GET['championshipID'])) $championshipID = $_GET['championshipID'];
		if(!empty($_GET['login'])) $login = $_GET['login'];
		if(!empty($_GET['inscriptionDate'])) $inscriptionDate = $_GET['inscriptionDate'];

		return new User_Championship_Model($championshipID!,$login!,$inscriptionDate);

	}

}


function gatherDataChampionship(){

	$champeionshipID = '';
	$name = '';
	$startDate = '';
	$endDate = '';
	$level = '';

	if($_POST){

		if(!empty($_POST['champeionshipID'])) $champeionshipID = $_POST['champeionshipID'];
		if(!empty($_POST['name'])) $name = $_POST['name'];
		if(!empty($_POST['startDate'])) $startDate = $_POST['startDate'];
		if(!empty($_POST['endDate'])) $endDate = $_POST['endDate'];
		if(!empty($_POST['level'])) $level = $_POST['level'];

		return new Championship_Model($champeionshipID!,$name,$startDate,$endDate,$level);

	} else {

		if(!empty($_GET['champeionshipID'])) $champeionshipID = $_GET['champeionshipID'];
		if(!empty($_GET['name'])) $name = $_GET['name'];
		if(!empty($_GET['startDate'])) $startDate = $_GET['startDate'];
		if(!empty($_GET['endDate'])) $endDate = $_GET['endDate'];
		if(!empty($_GET['level'])) $level = $_GET['level'];

		return new Championship_Model($champeionshipID!,$name,$startDate,$endDate,$level);

	}
	
}


function gatherDataUser(){

	$login = '';
	$name = '';
	$surname = '';
	$email = '';
	$password = '';

	if($_POST){

		if(isset($_POST['login'])) $login = $_POST['login'];
		if(isset($_POST['name'])) $name = $_POST['name'];
		if(isset($_POST['surname'])) $surname = $_POST['surname'];
		if(isset($_POST['email'])) $email = $_POST['email'];
		if(isset($_POST['password'])) $password = $_POST['password'];

		return new User_Model($login,$name,$surname,$email,$password);

	} else {

		if(isset($_GET['login'])) $login = $_GET['login'];
		if(isset($_GET['name'])) $name = $_GET['name'];
		if(isset($_GET['surname'])) $surname = $_GET['surname'];
		if(isset($_GET['email'])) $email = $_GET['email'];
		if(isset($_GET['password'])) $password = $_GET['password'];

		return new User_Model($login,$name,$surname,$email,$password);

	}

}

?>
```
## index.php
```
<?php

define("DEFAULT_CONTROLLER", "Index");
define("DEFAULT_ACTION", "index");



function run() {
	try {

		if (!isset($_GET["controller"])) {
			$_GET["controller"] = DEFAULT_CONTROLLER;
		}
		if (!isset($_GET["action"])) {
			$_GET["action"] = DEFAULT_ACTION;
		}

		$controller = loadController($_GET["controller"]);


		include (string)$controller;

	} catch(Exception $ex) {
		die("Ha habiedo una Exception: ".$ex->getMessage());
	}
} //Final run()

function loadController($controllerName) {
	$controllerClassName = __DIR__."/Controllers/".$controllerName."_Controller.php";
	return $controllerClassName;
}

run();

?>
```

## Disclaimer  
If you see any syntax error both in the Python script or any PHP files. Please contact me asap. Enjoy ^^  

## TODO  
- Convert functional script to Class based script.  
- Add functionalities to file parser.  
- Correctly comment all the functions.  

