from constants import *

def createGatherData(absolute_output_path):
    '''
    Gather Data initial unfilled script creation
    @Param absolute_output_path: Path where the hole output is going to be written
    '''

    gather = open(absolute_output_path + '/Functions/gatherData.php', 'w')

    gather.write('<?php' + EOL)
    gather.write(EOL)
    gather.write('//Fill with includes' + EOL)
    gather.write(EOL)

    gather.close()

def appendToGatherData(entityName, attributesList, absolute_output_path):
    '''
    Append to gatherData.php file
    @Param entityName: Name of the entity.
    @Param attributesList: List of all attributes of the entity.
    @Param absolute_output_path: Path where the hole output is going to be written
    '''
    originalName = entityName
    originalName = originalName.lower()
    originalName = originalName.title()
    originalName = originalName.replace(" ", "_")
    entityName = entityName.lower()
    entityName = entityName.title()
    entityName = entityName.replace(" ", "")

    gather = open(absolute_output_path + '/Functions/gatherData.php', 'a+')

    gather.write('function gatherData' + entityName + '(){' + EOL)
    gather.write(EOL)
    for attribute in attributesList:
        gather.write(ST + '$' + attribute + ' = \'\';' + EOL)
    gather.write(EOL)
    gather.write(ST + 'if($_POST){' + EOL)
    gather.write(EOL)
    for attribute in attributesList:
        gather.write(DT + 'if(isset($_POST[\'' + attribute + '\'])) $' + attribute + ' = $_POST[\'' + attribute + '\'];' + EOL)
    gather.write(EOL)

    gather.write(DT + 'return new ' + originalName + '_Model(')
    for i in range(0, len(attributesList)):
        gather.write('$' + attributesList[i])
        if i != (len(attributesList) - 1):
            gather.write(',')
    gather.write(');' + EOL)
    gather.write(EOL)
    gather.write(ST + '} else {' + EOL)
    gather.write(EOL)
    for attribute in attributesList:
        gather.write(DT + 'if(isset($_GET[\'' + attribute + '\'])) $' + attribute + ' = $_GET[\'' + attribute + '\'];' + EOL)
    gather.write(EOL)
    gather.write(DT + 'return new ' + originalName + '_Model(')
    for i in range(0, len(attributesList)):
        gather.write('$' + attributesList[i])
        if i != (len(attributesList) - 1):
            gather.write(',')
    gather.write(');' + EOL)
    gather.write(EOL)
    gather.write(ST + '}' + EOL)
    gather.write(EOL)
    gather.write('}' + EOL)
    gather.write(EOL)

    gather.close()

def closeGatherData(absolute_output_path):
    '''
    Close PHP Tag on gatherData.php
    @Param absolute_output_path: Path where the hole output is going to be written
    '''
    gather = open(absolute_output_path + '/Functions/gatherData.php', 'a+')

    gather.write('?>')

    gather.close()
