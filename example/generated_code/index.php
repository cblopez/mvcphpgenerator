<?php

define("DEFAULT_CONTROLLER", "Index");
define("DEFAULT_ACTION", "index");


function run(){
	try{
		if(!isset($_GET["controller"])){
			$_GET["controller"] = DEFAULT_CONTROLLER;
		}
		if(!isset($_GET["action"])){
			$_GET["action"] = DEFAULT_ACTION;
		}

		$controller = loadController($_GET["controller"]);

		include (string)$controller;

	} catch(Exception $ex){
		die("An exception has occured: " . $ex->getMessage());
	}
}

function loadController($controllerName){
	$controllerClassName = __DIR__."/Controllers/".$controllerName."_Controller.php";
	return $controllerClassName;
}

run();
?>
