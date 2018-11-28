from constants import *


def createIndex(absolute_output_path):
    '''
    Creates an index.php on the root directory of the output folder
    Note: the index.php will be used as a common entry point
    @Param absolute_output_path: Path where the hole output is going to be written
    '''

    index = open(absolute_output_path + '/index.php', 'w')

    index.write('<?php' + EOL)
    index.write(EOL)
    index.write('define(\"DEFAULT_CONTROLLER\", \"Index\");' + EOL)
    index.write('define(\"DEFAULT_ACTION\", \"index\");' + EOL)
    index.write(EOL)
    index.write(EOL)
    index.write('function run(){' + EOL)
    index.write(ST + 'try{' + EOL)
    index.write(DT + 'if(!isset($_GET[\"controller\"])){' + EOL)
    index.write(TT + '$_GET[\"controller\"] = DEFAULT_CONTROLLER;' + EOL)
    index.write(DT + '}' + EOL)
    index.write(DT + 'if(!isset($_GET[\"action\"])){' + EOL)
    index.write(TT + '$_GET[\"action\"] = DEFAULT_ACTION;' + EOL)
    index.write(DT + '}' + EOL)
    index.write(EOL)
    index.write(DT + '$controller = loadController($_GET[\"controller\"]);' + EOL)
    index.write(EOL)
    index.write(DT + 'include (string)$controller;' + EOL)
    index.write(EOL)
    index.write(ST + '} catch(Exception $ex){' + EOL)
    index.write(DT + 'die(\"An exception has occured: \" . $ex->getMessage());' + EOL)
    index.write(ST + '}' + EOL)
    index.write('}' + EOL)
    index.write(EOL)
    index.write('function loadController($controllerName){' + EOL)
    index.write(ST + '$controllerClassName = __DIR__.\"/Controllers/\".$controllerName.\"_Controller.php\";' + EOL)
    index.write(ST + 'return $controllerClassName;' + EOL)
    index.write('}' + EOL)
    index.write(EOL)
    index.write('run();' + EOL)
    index.write('?>' + EOL)

    index.close()
