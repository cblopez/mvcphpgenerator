# mvcphpgenerator 2.0
Python script for PHP file generator using MVC Paradigm for Python 2.7.  
Created by Christian Barral

## Fixed  
Fixed indentations that were causing the manual input to not behave as intended.  

## NEW!    
End of line '\r\n', as well as single, double and triple tabulations are now defined as constants in their particular file  

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
- The script for gathering data is situated under MVCPHPGenerator/Functions (MVCPHPGenerator is the default name, you'll be able to change it, read 'Arguments' section).  
- The index.php file is used as a common entry point. 
  
## Arguments  
Several arguments are now available for your script:  
```  
usage: mvcPHPGenerator.py [-h] [-o OUTPUT_DIRECTORY] [-i INPUT_FILE]
                          [--name OUTPUT_NAME] [--create-index]

mvcPHPGenerator. PHP file generator.

optional arguments:
  -h, --help           show this help message and exit
  -o OUTPUT_DIRECTORY  Select the output directory of the PHP files
  -i INPUT_FILE        Select entities, attributes and actiones from a
                       structured file. Visit
                       http://www.github.com/cblopez/mvcPHPGenerator for more
                       details.
  --name OUTPUT_NAME   Select the name of the output directory you want to
                       create
  --create-index       Enable de index.php creation.
``` 
## Two input modes  
As you can see in the possible arguments section, you can either use an input file, or use the manual input. I highly recommend you using an input file as it's quicker and easy to modify, but be careful, the input file must follow some strict syntax rules:  
- Entities MUST start with a '-' sign  
- Attributes and actions from an entity MUST be under that entity and before the next one, if you don't want to experiment some weird behavour.  
- Attributes MUST start with '+' sign  
- Actions MUST start with '\*' sign
- NO blanck lines are permitted.
- Any type of tab (\t) will be omitted.  

### Example (input file)  
So we have the following example: "I want to create a PHP file structure with two entities involved: User and Post. My User has the following attributes: login, name, surname, email, password. The application will be able to add, edit, show and delete users. My Post has the following attributes: idPost, title, content, author, date. The applications will be able to add, delete and showall posts.". Here's an example of how the input file should look like:  
``` 
-User
	+login
	+name
	+surname
	+email
	+password
	*add
	*edit
	*show
	*delete
-Post
	+idPost
	+title
	+content
	+author
	+date
	*add
	*delete
	*showall
```  
Now all we have to do, is to execute the script using the -i option. Imagine that the above file is called 'example.txt' and it's on the current directory of the script. We'll also like to name our output directory as 'gitExample', and save it in the current execution path. Let's also generate an index.php to make our lifes easier:  
``` 
python mvcPHPGenerator.py -i example.txt --name gitExample --create-index
```  

### Example (manual input)  
If you decide not to use a strutured input file (you should, btw), you can execute the script without the -i option and enter all the information manually. Let's now create a manual input and export all tha information to a folder called 'manualInputExample' on the directory '/tmp/myDir'. If a given directory does not exist, the script will ask you if you would like to create it. Example
``` 
python mvcPHPGenerator.py -o /tmp/myDir --name manualIinputExample --create-index
``` 
We can now fill all the information we want, following the instruction displayed in the terminal:  

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
Insert attribute name (exit to stop): title
Insert attribute name (exit to stop): content
Insert attribute name (exit to stop): author
Insert attribute name (exit to stop): date
Insert attribute name (exit to stop): exit
Insert action (none to stop): add
Insert action (none to stop): delete
Insert action (none to stop): showall
Insert action (none to stop): none
[+] Creating Controller for POST
[+] Creating Model for POST
[+] Appending to gatherData.php for POST
Would you like to add more entities? (yes/no): no
[+] Finished successfully.
IMPORTANT: Go to the Functions folder and fill the models includes from gatherData.php manually.
```

##### Please notice the last line: IMPORTANT: Go to the Functions folder and fill the models includes from gatherData.php manually.  

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

include __DIR__.'/../Functions/gatherData.php';


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
		//include_once __DIR__.'/../Functions/FillWithDBConnection.php';
		$this->db = "something";//Fill with connection method
	}

}

?>
```
## gatherData Example  
```
<?php

//Fill with includes

function gatherDataPost(){

	$idPost = '';
	$title = '';
	$content = '';
	$author = '';
	$date = '';

	if($_POST){

		if(isset($_POST['idPost'])) $idPost = $_POST['idPost'];
		if(isset($_POST['title'])) $title = $_POST['title'];
		if(isset($_POST['content'])) $content = $_POST['content'];
		if(isset($_POST['author'])) $author = $_POST['author'];
		if(isset($_POST['date'])) $date = $_POST['date'];

		return new Post_Model($idPost,$title,$content,$author,$date);

	} else {

		if(isset($_GET['idPost'])) $idPost = $_GET['idPost'];
		if(isset($_GET['title'])) $title = $_GET['title'];
		if(isset($_GET['content'])) $content = $_GET['content'];
		if(isset($_GET['author'])) $author = $_GET['author'];
		if(isset($_GET['date'])) $date = $_GET['date'];

		return new Post_Model($idPost,$title,$content,$author,$date);

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
