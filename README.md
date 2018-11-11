# mvcphpgenerator 1.1.1  
Python script for PHP file generator using MVC Paradigm for Python 2.7.  
Created by Christian Barral

## Fixed
Fixed a syntax error on includes of every Controllers  
Fixed a missing value for $this->db in every Model constructor.  
include_once of DB authentication function example is now commented at first.

## NEW!  
index.php generator!  

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
Execute the script  
```
 python mvcPHPGenerator.py
```

You'll be asked to type on terminal all the info required to create de PHP scripts and classes. The script follows this scheme for your project:  
- Controllers are scripts
- Models are classes
- Views are not created (obviously)
- The script for gathering data is situated under MVCPHPGenerator/Functions  
- the index.php is used as a common entry point (new)  

With that being said, you'll need to fill the information asked. It looks something like this:
``` 
*_*_*_*_*_*_*_*_*_*
MVC PHP Generator
by Christian Barral
*_*_*_*_*_*_*_*_*_*

[+] Starting MVC PHP Generator
[+] Creating directory structure
[+] Created MVCPHPGenerator folder
[+] Created Controllers folder
[+] Created Functions folder
[+] Created Models folder
[+] Created Views folder
[+] Creating gatherData.php
Entity name: USER
Insert attribute name (exit to stop): login
Insert attribute name (exit to stop): name
Insert attribute name (exit to stop): surname
Insert attribute name (exit to stop): email
Insert attribute name (exit to stop): password
Insert attribute name (exit to stop): exit
Insert action (none to stop): add
Insert action (none to stop): edit
Insert action (none to stop): show
Insert action (none to stop): delete
Insert action (none to stop): none
[+] Creating Controller for USER
[+] Creating Model for USER
[+] Appending to gatherData.php for USER
Would you like to add more entities? (yes/no): yes
Entity name: POST
Insert attribute name (exit to stop): idPost
Insert attribute name (exit to stop): content
Insert attribute name (exit to stop): author
Insert attribute name (exit to stop): exit
Insert action (none to stop): add
Insert action (none to stop): edit
Insert action (none to stop): show
Insert action (none to stop): delete
Insert action (none to stop): none
[+] Creating Controller for POST
[+] Creating Model for POST
[+] Appending to gatherData.php for POST
Would you like to add more entities? (yes/no): no
[+] Finished successfully.
```

Note that the resulting directory is created on the path you executed the script. I'll add the functionality of changing that path on following versions.  
The resulting directory should look something like this (entities taken from the above example):  
- MVCPHPGenerator
  - Controllers
    - Post_Controller.php
    - User_Controller.php
  - Functions
    - gatherData.php
  - Models
    - Post_Model.php
    - User_Model.php
  - Views  
  - index.php  


## Controller Example: User_Controller.php   
```
<?php

include __DIR__.'/../Functions/gatherData.php


if(!$_GET){
	//Fill
}

else{

	switch($_GET['action']){

		case 'add':
		if(!$_POST){
			//Fill
		} else {
			//Fill
		}
		break;

		case 'edit':
		if(!$_POST){
			//Fill
		} else {
			//Fill
		}
		break;

		case 'show':
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
}

?>

```
## Model example: User_Model.php
```
<?php

class User_Model{

	var $login;
	var $name;
	var $surname;
	var $email;
	var $password;
	var $db;

	function __construct($login,$name,$surname,$email,$password){
		$this->login = $login;
		$this->name = $name;
		$this->surname = $surname;
		$this->email = $email;
		$this->password = $password;
		//include_once __DIR__.'/../Functions/FillWithDBConnectioin.php';
		$this->db = 0;//Fill with connection method
	}

}
?>

```
## gatherData Example  
```
<?php

//Fill with includes

function gatherDataUser(){

	$login = ''
	$name = ''
	$surname = ''
	$email = ''
	$password = ''

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

function gatherDataPost(){

	$idPost = ''
	$content = ''
	$author = ''

	if($_POST){

		if(isset($_POST['idPost'])) $idPost = $_POST['idPost'];
		if(isset($_POST['content'])) $content = $_POST['content'];
		if(isset($_POST['author'])) $author = $_POST['author'];

		return new Post_Model($idPost,$content,$author);

	} else {

		if(isset($_GET['idPost'])) $idPost = $_GET['idPost'];
		if(isset($_GET['content'])) $content = $_GET['content'];
		if(isset($_GET['author'])) $author = $_GET['author'];

		return new Post_Model($idPost,$content,$author);

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
