node{

    stage('Cloning the project'){
	    git branch: 'main', url: 'https://github.com/BINDU1822/sonar-jenkins.git'
        // git 'https://github.com/BINDU1822/ci-cd-jenkins.git'
    }
    stage('Sonarqube Static code analysis'){
        def scannerHome = tool 'sonarqube';
        withSonarQubeEnv('sonarqube'){
            sh "${scannerHome}/bin/sonar-scanner \
            -D sonar.login=admin \
            -D sonar.password=binduramesh@1822 \
            -D sonar.projectkey=sonartest \
	        -D sonar.exclusions=vendors/**,resources/**,**/*,java \
            -D sonar.host.url=http://117.208.152.165:9000/"
        }
    }
}

// pipeline {
//     agent any
    
//     stages {
//         stage('Checkout') {
//             steps {
//                 // Checkout your source code repository here
//                 // For example, with Git:
//                 checkout scm
//             }
//         }
        
//         stage('Build') {
//             steps {
//                 // Compile and build your project here
//                 // For example, with Maven:
//                 sh 'mvn clean install'
//             }
//         }
        
//         stage('SonarQube Analysis') {
//             steps {
//                 script {
//                     // Define SonarQube scanner properties
//                     def scannerHome = tool name: 'sonarqube', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
                    
//                     withSonarQubeEnv('sonarqube') {
//                         sh "${scannerHome}/bin/sonar-scanner"
//                     }
//                 }
//             }
//         }
//     }
// }
