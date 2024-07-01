import os

directory = '{{ cookiecutter.__package.replace('.','/') }}'
srcDir = 'src/main/java/' + directory
srcControllerDir = srcDir + '/controller'
testDir = 'src/test/java/' + directory
testControllerDir = testDir + '/controller'

os.makedirs(srcDir, exist_ok=True)
os.makedirs(srcControllerDir, exist_ok=True)

if '{{ cookiecutter.junit }}' == 'yes':
	os.makedirs(testDir, exist_ok=True)
	os.makedirs(testControllerDir, exist_ok=True)

os.rename('{{ cookiecutter.artifactId }}Application.java', srcDir + '/{{ cookiecutter.artifactId }}Application.java')
os.rename('{{ cookiecutter.artifactId }}Controller.java', srcControllerDir + '/{{ cookiecutter.artifactId }}Controller.java')

os.rename('{{ cookiecutter.artifactId }}ApplicationTests.java', testDir + '/{{ cookiecutter.artifactId }}ApplicationTests.java')
os.rename('{{ cookiecutter.artifactId }}ControllerTests.java', testControllerDir + '/{{ cookiecutter.artifactId }}ControllerTests.java')

os.system('mvn wrapper:wrapper')

os.system('./mvnw verify')