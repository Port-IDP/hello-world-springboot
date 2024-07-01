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

os.rename("MainApplication.java", srcDir + '/{{ cookiecutter.artifactId }}Application.java')
os.rename("MainController.java", srcControllerDir + '/MainController.java')

os.rename("MainApplicationTests.java", testDir + '/MainApplicationTests.java')
os.rename("MainControllerTests.java", testControllerDir + '/MainControllerTests.java')

os.system('mvn wrapper:wrapper')

os.system('./mvnw verify')