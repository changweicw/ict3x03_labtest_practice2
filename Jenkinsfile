
		// stage('OWASP DependencyCheck') {
		// 	steps {
		// 		dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'Default'
		// 	}
		// }

       
    
    // post {
	// 	success {
	// 		dependencyCheckPublisher pattern: 'dependency-check-report.xml'
	// 	}
	// }


pipeline {
    agent any
    stages {
         stage('Static Analysis') {
            steps {
                echo 'Run the static analysis to the code' 
            }
        }
        stage('test'){
            agent {
                docker {
                    image 'python:3.8'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                // sh 'python -m unittest Testing.UnitTesting.testunittest -v'
                // sh 'python -m unittest Testing.IntegrationTesting.testLoginReg -v'
                // sh 'python -m unittest Testing.IntegrationTesting.testProducts -v'
                // sh 'python -m unittest Testing.IntegrationTesting.testTransaction -v'
                // sh 'wget https://github.com/mozilla/geckodriver/releases/download/v0.25.0/geckodriver-v0.25.0-linux64.tar.gz '
                // sh 'tar xzf geckodriver-v0.25.0-linux64.tar.gz'
                // sh 'chmod +x geckodriver'
                // sh 'mv geckodriver /usr/bin/geckodriver'
                // sh 'apt update'
                // sh 'apt install firefox-esr -y'
                // sh 'python Testing/SeleniumTesting/testSeleniumUI.py '
                // sh 'pip freeze | safety check --stdin '
            }
        }

        stage("build"){
            steps{
                sh 'docker build -t changweicw/saveme:latest .'
                sh 'docker run -d -p 127.0.0.1:5000:5000 --name saveme changweicw/saveme:latest'
            }
        }
        
        stage("deploy"){
            steps{
                sh 'docker ps -f name=saveme | grep -o "saveme" && docker kill $(docker ps -f name=saveme | grep -o "saveme")'
                sh "printf 'y' | docker container prune"
                sh 'docker run -d -p 127.0.0.1:5000:5000 --name saveme changweicw/saveme:latest'
            }
        }

    }
}
