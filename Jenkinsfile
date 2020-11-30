
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
                // sh 'wget https://github.com/mozilla/geckodriver/releases/download/v0.25.0/geckodriver-v0.25.0-linux64.tar.gz '
                // sh 'tar xzf geckodriver-v0.25.0-linux64.tar.gz'
                // sh 'chmod +x geckodriver'
                // sh 'mv geckodriver /usr/bin/geckodriver'
                // sh 'apt update'
                // sh 'apt install firefox-esr -y'
                // sh 'python SeleniumTesting/seleniumscript.py '
                // sh 'pip freeze | safety check --stdin '
            }
        }

        stage('Build'){
                    steps {
                        sh 'docker build -t saveme:latest .'
                        sh 'docker ps -f name=revision | grep -o "revision" && docker kill $(docker ps -f name=revision | grep -o "revision")'
                        sh "printf 'y' | docker container prune"
                        sh 'docker run -d -p 5000:5000 --name revision saveme:latest'
                    }
                }

    }
}
