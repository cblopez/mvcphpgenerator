from constants import *

def createGatherData(absolute_output_path, entities):
    '''
    Gather Data initial unfilled script creation
    @Param absolute_output_path: Path where the hole output is going to be written
    '''

    gather = open(absolute_output_path + '/Functions/gatherData.php', 'w')

    gather.write('<?php' + EOL)
    gather.write(EOL)
    for entity in entities:
        properly_named_entity = entity.lower()
        properly_named_entity = entity.title()
        properly_named_entity = entity.replace(" ", "_")
        gather.write('include __DIR__.\'/../Models/' + properly_named_entity + '.php\';' + EOL)
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
        attributeCleaned = attribute.replace('!', '')
        gather.write(ST + '$' + attributeCleaned + ' = \'\';' + EOL)
    gather.write(EOL)
    gather.write(ST + 'if($_POST){' + EOL)
    gather.write(EOL)
    for attribute in attributesList:
        attributeCleaned = attribute.replace('!', '')
        gather.write(DT + 'if(!empty($_POST[\'' + attributeCleaned + '\'])) $' + attributeCleaned + ' = $_POST[\'' + attributeCleaned + '\'];' + EOL)
    gather.write(EOL)

    gather.write(DT + 'return new ' + originalName + '_Model(')
    for i in range(0, len(attributesList)):
        attributeCleaned = attributesList[i].replace('?', '')
        gather.write('$' + attributeCleaned)
        if i != (len(attributesList) - 1):
            gather.write(',')
    gather.write(');' + EOL)
    gather.write(EOL)
    gather.write(ST + '} else {' + EOL)
    gather.write(EOL)
    for attribute in attributesList:
        attributeCleaned = attribute.replace('!', '')
        gather.write(DT + 'if(!empty($_GET[\'' + attributeCleaned + '\'])) $' + attributeCleaned + ' = $_GET[\'' + attributeCleaned + '\'];' + EOL)
    gather.write(EOL)
    gather.write(DT + 'return new ' + originalName + '_Model(')
    for i in range(0, len(attributesList)):
        attributeCleaned = attributesList[i].replace('?', '')
        gather.write('$' + attributeCleaned)
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
