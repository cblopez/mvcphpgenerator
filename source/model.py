from constants import *

def generateModel(entityName, attributesList, absolute_output_path):
    '''
    Model Generator
    @Param entityName: Name of the entity.
    @Param attributesList: List of all attributes of the entity.
    @Param absolute_output_path: Path where the hole output is going to be written
    '''

    entityName = entityName.lower()
    entityName = entityName.title()
    entityName = entityName.replace(" ", "_")

    model = open(absolute_output_path +'/Models/' + entityName + ".php", 'w')

    model.write('<?php' + EOL)
    model.write(EOL)
    model.write('class ' + entityName + '_Model{' + EOL)
    model.write(EOL);
    model.write(ST + '//Database' + EOL)
    model.write(ST + 'private $conn;' + EOL);
    model.write(ST + 'private $table = \'' + entityName.upper() + '\';' + EOL)
    model.write(EOL)
    model.write(ST + '//' + entityName + ' attributes' + EOL);
    for attribute in attributesList:
        attributeCleaned = attribute.replace('!', '')
        model.write(ST + 'private $' + attributeCleaned +';' + EOL)
    model.write(EOL)
    model.write(ST + '//Constructor' + EOL);
    model.write(ST + 'function __construct(')
    for i in range(0,len(attributesList)):
        attributeCleaned = attributesList[i].replace('!', '')
        model.write('$' + attributeCleaned)
        if i != (len(attributesList) - 1):
            model.write(',')
    model.write('){' + EOL)
    for attribute in attributesList:
        attributeCleaned = attribute.replace('!', '')
        model.write(DT + '$this->' + attributeCleaned + ' = $' + attributeCleaned + ';' + EOL)
    model.write(DT + 'include_once __DIR__.\'/../config/Database.php\';' + EOL)
    model.write(DT + '$this->conn = new Database()->connect();' + EOL)
    model.write(ST + '}' + EOL)
    model.write(EOL)

    # ----------Getters Generation start-----------
    model.write(ST + '//Getters' + EOL)
    for attribute in attributesList:
        attributeCleaned = attribute.replace('!', '')
        model.write(ST + 'function get' + attributeCleaned.title() + '(){return $this->' + attributeCleaned + ';}' + EOL)
    # ----------Getters Generation end-----------
    model.write(EOL)
    # ----------Setters Generation start-----------
    model.write(ST + '//Setters' + EOL)
    for attribute in attributesList:
        attributeCleaned = attribute.replace('!', '')
        model.write(ST + 'function set' + attributeCleaned.title() + '($' + attributeCleaned + '){$this->' + attributeCleaned + ' = $' + attributeCleaned + ';}' + EOL)
    # ----------Setters Generation end-----------
    model.write(EOL)
    # formation of list of Primay Keys of the entity
    primaryKeys = []
    for attribute in attributesList:
        if '!' in attribute:
            primaryKeys.append(attribute.replace('!', ''))
    # ----------CRUD Generation start-----------
    createSelectFunction(entityName, attributesList, primaryKeys, model)
    model.write(EOL)
    createInsertFunction(entityName, attributesList, primaryKeys, model)
    model.write(EOL)
    createUpdateFunction(entityName, attributesList, primaryKeys, model)
    model.write(EOL)
    createDeleteFunction(entityName, primaryKeys, model)
    model.write(EOL)
    # ----------CRUD Generation end-----------
    model.write('}' + EOL)
    model.write(EOL)

def createSelectFunction(entityName, attributesList, primaryKeys, model):
    model.write(ST + 'function readAll(){' + EOL)
    model.write(EOL)
    model.write(DT + '$query = \'SELECT * FROM \' . $this->table;' + EOL)
    model.write(EOL)
    model.write(DT + '$stmt = $this->conn->prepare($query);' + EOL)
    model.write(EOL)
    model.write(DT + '$stmt->execute();' + EOL)
    model.write(EOL)
    model.write(DT + 'return $stmt;' + EOL)
    model.write(EOL)
    model.write(ST + '}' + EOL)
    model.write(EOL)
    model.write(ST + 'function read(){' + EOL)
    model.write(EOL)
    model.write(DT + '$query = \'SELECT * FROM \' . $this->table . \' WHERE ')
    for i in range(len(primaryKeys)):
        model.write(primaryKeys[i] + ' = ? ')
        if i != (len(primaryKeys) - 1):
            model.write('AND ')
    model.write('\';' + EOL)
    model.write(EOL)
    model.write(DT + '$stmt = $this->conn->prepare($query);' + EOL)
    model.write(EOL)
    counter = 1
    for primaryKey in primaryKeys:
        model.write(DT + '$stmt->bindParam(' + str(counter) + ', ' + 'htmlspecialchars(strip_tags($this->' + primaryKey + ')));' + EOL)
        counter += 1
    model.write(EOL)
    model.write(DT + '$stmt->execute();' + EOL)
    model.write(EOL)
    model.write(DT + 'return $stmt;' + EOL)
    model.write(EOL)
    model.write(ST + '}' + EOL)
    model.write(EOL)

def createInsertFunction(entityName, attributesList, primaryKeys, model):
    model.write(ST + 'function insert(){' + EOL)
    model.write(EOL)
    model.write(DT + '$query = \'INSERT INTO \' . $this->table . \'(')
    for i in range(len(attributesList)):
        attributeCleaned = attributesList[i].replace('!', '')
        model.write(attributeCleaned)
        if i != (len(attributesList) - 1):
            model.write(', ')
    model.write(')' + EOL)
    model.write(DT + ' VALUES (')
    for i in range(len(attributesList)):
        model.write('?')
        if i != (len(attributesList) - 1):
            model.write(', ')
    model.write(')\';' + EOL)
    model.write(EOL)
    model.write(DT + '$stmt = $this->conn->prepare($query);' + EOL)
    model.write(EOL)
    counter = 1
    for attribute in attributesList:
        attributeCleaned = attribute.replace('!', '')
        model.write(DT + '$stmt->bindParam(' + str(counter) + ', ' + 'htmlspecialchars(strip_tags($this->' + attributeCleaned + ')));' + EOL)
        counter+=1
    model.write(EOL)
    model.write(DT + '$stmt->execute();' + EOL)
    model.write(EOL)
    model.write(DT + 'return $stmt;' + EOL)
    model.write(EOL)
    model.write(ST + '}' + EOL)
    model.write(EOL)

def createUpdateFunction(entityName, attributesList, primaryKeys, model):
    model.write(ST + 'function update(){' + EOL)
    model.write(EOL)
    model.write(DT + '$query = \'UPDATE \' . $this->table . \' SET ')
    for i in range(len(attributesList)):
        attributeCleaned = attributesList[i].replace('!', '')
        if attributeCleaned not in primaryKeys:
            model.write(attributeCleaned + ' = ? ')
            if i != (len(attributesList) - 1):
                model.write(', ')
    model.write(' WHERE ')
    for i in range(len(primaryKeys)):
        model.write(primaryKeys[i] + ' = ? ')
        if i != (len(primaryKeys) - 1):
            model.write('AND ')
    model.write('\';' + EOL)
    model.write(EOL)
    model.write(DT + '$stmt = $this->conn->prepare($query);' + EOL)
    model.write(EOL)
    counter = 1
    for attribute in attributesList:
        attributeCleaned = attribute.replace('!', '')
        if attributeCleaned not in primaryKeys:
            model.write(DT + '$stmt->bindParam(' + str(counter) + ', ' + 'htmlspecialchars(strip_tags($this->' + attributeCleaned + ')));' + EOL)
            counter += 1
    for primaryKey in primaryKeys:
        model.write(DT + '$stmt->bindParam(' + str(counter) + ', ' + 'htmlspecialchars(strip_tags($this->' + primaryKey + ')));' + EOL)
        counter += 1
    model.write(EOL)
    model.write(DT + '$stmt->execute();' + EOL)
    model.write(EOL)
    model.write(DT + 'return $stmt->rowCount() > 0;' + EOL)
    model.write(EOL)
    model.write(ST + '}' + EOL)
    model.write(EOL)

def createDeleteFunction(entityName, primaryKeys, model):
    model.write(ST + 'function delete(){' + EOL)
    model.write(EOL)
    model.write(DT + '$query = \'DELETE FROM \' . $this->table . \' WHERE ')
    for i in range(len(primaryKeys)):
        model.write(primaryKeys[i] + ' = ? ')
        if i != (len(primaryKeys) - 1):
            model.write('AND ')
    model.write('\';' + EOL)
    model.write(EOL)
    model.write(DT + '$stmt = $this->conn->prepare($query);' + EOL)
    model.write(EOL)
    counter = 1
    for primaryKey in primaryKeys:
        model.write(DT + '$stmt->bindParam(' + str(counter) + ', ' + 'htmlspecialchars(strip_tags($this->' + primaryKey + ')));' + EOL)
        counter += 1
    model.write(EOL)
    model.write(DT + '$stmt->execute();' + EOL)
    model.write(EOL)
    model.write(DT + 'return $stmt;' + EOL)
    model.write(EOL)
    model.write(ST + '}' + EOL)
    model.write(EOL)
